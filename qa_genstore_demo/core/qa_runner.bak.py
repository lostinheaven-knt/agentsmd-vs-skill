"""
QA Runner for Genstore Help Documentation.

Implements both Skills mode (active retrieval) and AGENTS.md mode (passive context)
for QA scenarios, similar to the original agents_md_vs_skill demo.
"""

import os
import sys
from typing import Dict, List, Optional, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.docs_loader import DocsLoader, build_agents_md_index


class BaselineQARunner:
    """
    Baseline runner - no documentation access.
    Tests LLM's pre-training knowledge only.
    """
    
    def __init__(self, agent):
        """
        Initialize baseline runner.
        
        Args:
            agent: LLM agent instance
        """
        self.agent = agent
    
    def run_task(self, question: str) -> str:
        """
        Run a QA task without any documentation context.
        
        Args:
            question: The question to answer
            
        Returns:
            LLM's answer
        """
        return self.agent.generate_code(question, context="")
    
    def reset(self):
        """No state to reset."""
        pass


class SkillsQARunner:
    """
    Skills mode runner - active retrieval pattern.
    
    The LLM must decide whether to invoke a skill (tool) to retrieve
    relevant documentation.
    """
    
    def __init__(self, agent, docs_loader: DocsLoader, trigger_instruction: Optional[str] = None):
        """
        Initialize skills mode runner.
        
        Args:
            agent: LLM agent instance
            docs_loader: DocsLoader instance with loaded documentation
            trigger_instruction: Type of trigger instruction to use
                - None: No explicit instruction
                - "must_invoke": "You MUST invoke the search_docs skill"
                - "explore_first": "First explore the documentation, then answer"
        """
        self.agent = agent
        self.docs_loader = docs_loader
        self.trigger_instruction = trigger_instruction
        self.invoked_skill = False
        self.retrieved_docs: List[str] = []
    
    def run_task(self, question: str) -> str:
        """
        Run a QA task using skills mode.
        
        Args:
            question: The question to answer
            
        Returns:
            LLM's answer
        """
        self.invoked_skill = False
        self.retrieved_docs = []
        
        # Build context based on trigger instruction
        context = self._build_context(question)
        
        # Simulate skill invocation decision
        # In real scenario, LLM would decide; here we simulate based on instruction
        if self.trigger_instruction:
            self.invoked_skill = True
        else:
            # Simulate 44% chance of invoking skill (based on original research)
            import random
            self.invoked_skill = random.random() < 0.44
        
        if self.invoked_skill:
            # Retrieve relevant docs
            search_results = self.docs_loader.search(question, max_results=3)
            
            for doc_path, score in search_results:
                keys = doc_path.split("/")
                content = self.docs_loader.get_doc(*keys)
                if content:
                    self.retrieved_docs.append(f"=== {doc_path} ===\n{content}")
        
        # Build final context
        if self.retrieved_docs:
            full_context = context + "\n\n" + "\n\n".join(self.retrieved_docs)
        else:
            full_context = context
        
        return self.agent.generate_code(question, context=full_context)
    
    def _build_context(self, question: str) -> str:
        """
        Build the context based on trigger instruction.
        
        Args:
            question: The question to answer
            
        Returns:
            Context string
        """
        base_context = f"""Question: {question}

You have access to a 'search_docs' skill that can search the Genstore documentation.
"""
        
        if self.trigger_instruction is None:
            # No explicit instruction
            return base_context
        
        elif self.trigger_instruction == "must_invoke":
            return base_context + """

IMPORTANT: You MUST invoke the 'search_docs' skill to find relevant documentation before answering.
Do not rely solely on your pre-training knowledge for this question.
"""
        
        elif self.trigger_instruction == "explore_first":
            return base_context + """

IMPORTANT: First explore the documentation using the 'search_docs' skill, then answer the question.
This ensures your answer is based on the most accurate and up-to-date information.
"""
        
        return base_context
    
    def get_invocation_rate(self) -> float:
        """
        Get the skill invocation rate.
        
        Returns:
            1.0 if skill was invoked, 0.0 otherwise
        """
        return 1.0 if self.invoked_skill else 0.0
    
    def reset(self):
        """Reset the runner state."""
        self.invoked_skill = False
        self.retrieved_docs = []


class AgentsMdQARunner:
    """
    AGENTS.md mode runner - passive context pattern.
    
    A compressed documentation index is always present in the context.
    The LLM can reference it without needing to make a tool-use decision.
    """
    
    def __init__(self, agent, docs_loader: DocsLoader):
        """
        Initialize AGENTS.md mode runner.
        
        Args:
            agent: LLM agent instance
            docs_loader: DocsLoader instance with loaded documentation
        """
        self.agent = agent
        self.docs_loader = docs_loader
        
        # Build compressed index
        self.agents_md_content = build_agents_md_index(docs_loader)
    
    def run_task(self, question: str) -> str:
        """
        Run a QA task using AGENTS.md mode.
        
        Args:
            question: The question to answer
            
        Returns:
            LLM's answer
        """
        # Build system prompt with AGENTS.md always present
        context = f"""{self.agents_md_content}

---

Question: {question}

When you need specific details, the relevant documentation sections are provided below.
"""
        
        # Retrieve most relevant docs based on question keywords
        # Increased max_results from 2 to 3 for better coverage
        search_results = self.docs_loader.search(question, max_results=3)
        
        if search_results:
            context += "\n\n=== Relevant Documentation ===\n\n"
            for doc_path, score in search_results:
                keys = doc_path.split("/")
                content = self.docs_loader.get_doc(*keys)
                if content:
                    # Inject FULL document content (not truncated)
                    # This matches the behavior in demo/agents_md_runner.py
                    context += f"=== {doc_path} ===\n{content}\n\n"
        
        return self.agent.generate_code(question, context=context)
    
    def reset(self):
        """No state to reset."""
        pass
    
    def get_index_size(self) -> int:
        """Get the size of the compressed index in bytes."""
        return len(self.agents_md_content.encode('utf-8'))
    
    def get_full_docs_size(self) -> int:
        """Get the size of full docs for comparison."""
        stats = self.docs_loader.get_stats()
        return stats["total_size_bytes"]


class QAEvaluator:
    """
    Evaluates QA answers against expected keywords and patterns.
    """
    
    def evaluate_answer(
        self,
        answer: str,
        expected_keywords: List[str],
        forbidden_keywords: List[str] = None,
        expected_patterns: List[str] = None
    ) -> Dict:
        """
        Evaluate an answer against expected criteria.
        
        Args:
            answer: The answer to evaluate
            expected_keywords: Keywords that should appear in the answer
            forbidden_keywords: Keywords that should NOT appear
            expected_patterns: Regex patterns that should match
            
        Returns:
            Evaluation result dictionary
        """
        answer_lower = answer.lower()
        
        # Check expected keywords
        matched_keywords = []
        missing_keywords = []
        
        for keyword in expected_keywords:
            if keyword.lower() in answer_lower:
                matched_keywords.append(keyword)
            else:
                missing_keywords.append(keyword)
        
        # Check forbidden keywords
        forbidden_found = []
        if forbidden_keywords:
            for keyword in forbidden_keywords:
                if keyword.lower() in answer_lower:
                    forbidden_found.append(keyword)
        
        # Check expected patterns
        matched_patterns = []
        if expected_patterns:
            import re
            for pattern in expected_patterns:
                if re.search(pattern, answer_lower):
                    matched_patterns.append(pattern)
        
        # Calculate score
        keyword_score = len(matched_keywords) / len(expected_keywords) if expected_keywords else 1.0
        penalty = len(forbidden_found) * 0.2  # 20% penalty per forbidden keyword
        final_score = max(0, keyword_score - penalty)
        
        passed = final_score >= 0.8
        
        return {
            "passed": passed,
            "score": final_score,
            "matched_keywords": matched_keywords,
            "missing_keywords": missing_keywords,
            "forbidden_found": forbidden_found,
            "matched_patterns": matched_patterns
        }


def create_runner(
    mode: str,
    agent,
    docs_loader: DocsLoader,
    trigger_instruction: Optional[str] = None
):
    """
    Factory function to create the appropriate runner.
    
    Args:
        mode: "baseline", "skills_default", "skills_must_invoke", 
              "skills_explore_first", or "agents_md"
        agent: LLM agent instance
        docs_loader: DocsLoader instance
        trigger_instruction: Trigger instruction for skills mode
        
    Returns:
        Appropriate runner instance
    """
    if mode == "baseline":
        return BaselineQARunner(agent)
    
    elif mode == "skills_default":
        return SkillsQARunner(agent, docs_loader, trigger_instruction=None)
    
    elif mode == "skills_must_invoke":
        return SkillsQARunner(agent, docs_loader, trigger_instruction="must_invoke")
    
    elif mode == "skills_explore_first":
        return SkillsQARunner(agent, docs_loader, trigger_instruction="explore_first")
    
    elif mode == "agents_md":
        return AgentsMdQARunner(agent, docs_loader)
    
    else:
        raise ValueError(f"Unknown mode: {mode}")
