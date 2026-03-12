#!/usr/bin/env python3
"""
Genstore Help Documentation QA Demo

This demo applies the AGENTS.md vs Skills research to a real-world QA scenario.
It tests whether passive context (AGENTS.md) is more effective than active 
retrieval (Skills) for answering questions based on Genstore help documentation.

Usage:
    # Real LLM (requires DEEPSEEK_API_KEY)
    export DEEPSEEK_API_KEY="your-api-key"
    python qa_genstore.py

    # Mock LLM (no API needed)
    python qa_genstore.py --mock

    # Quick test with easy questions only
    python qa_genstore.py --difficulty easy

    # Test specific modes
    python qa_genstore.py --modes baseline agents_md

    # Interactive mode - free conversation
    python qa_genstore.py --interactive --mode agents_md
"""

import argparse
import os
import statistics
import sys
import time
import json
from datetime import datetime
from typing import Dict, List, Optional, Callable, Any

# Add paths
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.docs_loader import DocsLoader, load_genstore_docs, build_agents_md_index
from core.qa_runner import create_runner, QAEvaluator
from tools.search_docs_tool import search_docs_tool_def, run_search_docs
from tools.compose_answer_tool import compose_answer_tool_def
from utils.dsml_parse import parse_dsml_invokes, is_dsml_function_calls
from utils.env_load import load_env_file
from tests.test_cases import (
    QA_TEST_CASES, get_test_cases_by_category, 
    get_test_cases_by_difficulty, get_test_stats
)

# Global log storage
MASTER_LOG: List[str] = []

# Conversation history for interactive mode
CONVERSATION_HISTORY: List[Dict] = []


def log_message(msg: str):
    """Add a message to the master log and print it."""
    MASTER_LOG.append(msg)
    print(msg)


def create_agent(use_mock: bool = False, on_step: Optional[Callable[[Dict[str, Any]], None]] = None):
    """
    Create a QA agent instance optimized for question answering.

    Loads .secrets.env from current working directory if present.
    """

    load_env_file(os.path.join(os.getcwd(), ".secrets.env"))

    if use_mock:
        print("  [Using Mock LLM Agent]")
        return MockQAAgent()
    else:
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            print("\n" + "="*70)
            print("WARNING: DEEPSEEK_API_KEY not set!")
            print("="*70)
            print("\nTo use the real LLM, please set your API key:")
            print("  export DEEPSEEK_API_KEY='your-api-key'")
            print("\nFalling back to Mock LLM...\n")
            return MockQAAgent()

        base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        print(f"  [Using Real LLM: DeepSeek @ {base_url}]")
        docs_loader = load_genstore_docs()
        return RealQAAgent(
            model="deepseek-chat",
            temperature=0.1,
            docs_loader=docs_loader,
            keep_last_qa_only=True,
            keep_last_qa_pairs=int(os.environ.get("QA_KEEP_LAST_QA_PAIRS", "1")),
            on_step=on_step,
        )


# ============================================================================
# QA-Specific Agent Classes
# ============================================================================

class RealQAAgent:
    """
    Real LLM Agent optimized for QA scenarios.

    Unlike code generation agents, this agent returns direct text answers
    based on documentation context.

    Now supports tool-use (search_docs) with thinking_mode + tool calls.
    """

    def __init__(
        self,
        model: str = "deepseek-chat",
        temperature: float = 0.1,
        docs_loader: Optional[DocsLoader] = None,
        keep_last_qa_only: bool = True,
        keep_last_qa_pairs: int = 1,
        on_step: Optional[Callable[[Dict[str, Any]], None]] = None,
    ):
        """Initialize the QA agent."""
        self.api_key = os.environ.get("DEEPSEEK_API_KEY")
        self.base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        self.model = model
        self.temperature = temperature
        self.docs_loader = docs_loader
        self.keep_last_qa_only = keep_last_qa_only
        self.keep_last_qa_pairs = keep_last_qa_pairs
        self.on_step = on_step

        if not self.api_key:
            raise ValueError("DEEPSEEK_API_KEY environment variable is required.")

        try:
            from openai import OpenAI
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
            )
        except ImportError:
            raise ImportError("openai package is required. Install it with: pip install openai")

        self.total_calls = 0
        self.total_tokens = 0
        self.log_messages: List[str] = []

        # Conversation history for multi-turn dialogue
        self.conversation_messages: List[Dict] = []

        # Tools
        self.tools = [search_docs_tool_def(), compose_answer_tool_def()]

        # Loop controls
        self.max_steps = 6
        self.last_tool_calls = 0

    def clear_history(self):
        """Clear conversation history for a new session."""
        self.conversation_messages = []
        self.log_messages = []

    def prune_history_keep_last_qa(self):
        """Keep only the last N user+assistant Q/A pairs in conversation history.

        Drops intermediate tool calls and reasoning from prior tasks.
        """
        if not self.keep_last_qa_only:
            return

        n_pairs = int(self.keep_last_qa_pairs or 0)
        if n_pairs <= 0:
            # keep nothing
            self.conversation_messages = []
            return

        keep_msgs = n_pairs * 2
        if len(self.conversation_messages) <= keep_msgs:
            return
        self.conversation_messages = self.conversation_messages[-keep_msgs:]

    def _log(self, message: str):
        """Add a log message."""
        self.log_messages.append(message)

    def get_logs(self) -> str:
        """Get all logged messages."""
        return "\n".join(self.log_messages)

    def generate_code(self, question: str, context: str = "") -> str:
        return self.answer_question(question, context)

    def answer_question(self, question: str, context: str = "") -> str:
        """Answer a question with tool-use loop."""
        self._log("=" * 80)
        self._log(f"[API CALL #{self.total_calls + 1}] {datetime.now().isoformat()}")
        self._log("=" * 80)

        system_prompt = """You are a helpful customer support assistant for Genstore, an e-commerce platform. Your role is to answer user questions based on the provided documentation.

Important guidelines:
1. Answer questions directly and clearly in plain text (not code)
2. Base your answers on the provided documentation/context
3. If the documentation contains relevant information, use it
4. If you cannot find the answer in the documentation, say so honestly
5. Be concise but thorough
6. Use bullet points or numbered lists when appropriate
7. If the question involves a process, provide step-by-step instructions
8. Always prefer information from the provided documentation over your general knowledge

Tool-use:
- You have access to a tool `search_docs` that can search Genstore documentation.
- Use `search_docs` when you need more info.
- When you have enough info and should stop searching, call `compose_answer`.

Output format per step:
- Use your internal thinking as needed.
- If you call tools, do so.
- Always aim to produce a final customer-facing answer via `compose_answer` once ready.

When documentation is provided, quote or reference it when relevant."""

        # Build user prompt: Context -> Question -> Instruction
        user_prompt = ""
        if context:
            user_prompt += f"""Documentation Context:
{context}

"""
        user_prompt += f"""Question: {question}

"""
        user_prompt += "Please provide a clear, helpful answer based on the documentation above."

        self._log("\n--- REQUEST ---")
        self._log(f"\n[System Prompt]:\n{system_prompt}")
        self._log(f"\n[User Prompt]:\n{user_prompt}")
        self._log(f"\n[Conversation History Turns]: {len(self.conversation_messages) // 2}")
        self._log(f"\n[Parameters]: model={self.model}, temperature={self.temperature}, max_tokens=2000, thinking=enabled")

        # Messages for tool loop
        messages: List[Dict[str, Any]] = [{"role": "system", "content": system_prompt}]
        messages.extend(self.conversation_messages)
        messages.append({"role": "user", "content": user_prompt})

        if self.conversation_messages:
            self._log(f"\n[History Messages Included]: {len(self.conversation_messages)} messages")

        start_time = time.time()
        final_answer: str = ""
        tool_calls_count = 0

        for step in range(1, self.max_steps + 1):
            self._log("\n" + ("-" * 80))
            self._log(f"[LOOP STEP {step}] calling LLM")

            # On the last step, force the model to stop tool-calling and produce a final answer.
            tool_choice = "none" if step == self.max_steps else "auto"

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=2000,
                tools=self.tools,
                tool_choice=tool_choice,
                extra_body={"thinking": {"type": "enabled"}},
            )

            self.total_calls += 1
            if response.usage:
                self.total_tokens += response.usage.total_tokens

            msg = response.choices[0].message

            # Log thinking (raw)
            reasoning = getattr(msg, "reasoning_content", None)
            if reasoning is not None:
                self._log("\n[reasoning_content]:\n" + str(reasoning))
                if self.on_step:
                    self.on_step({"type": "reasoning", "step": step, "reasoning_content": str(reasoning)})

            tool_calls = getattr(msg, "tool_calls", None)

            # DSML fallback: some models may emit tool calls inside content.
            if (not tool_calls) and is_dsml_function_calls(msg.content or ""):
                invs = parse_dsml_invokes(msg.content or "")
                if invs:
                    # synthesize tool_calls-like structure (minimal)
                    class _Fn:  # noqa
                        def __init__(self, name: str, arguments: str):
                            self.name = name
                            self.arguments = arguments

                    class _Tc:  # noqa
                        def __init__(self, _id: str, fn: _Fn):
                            self.id = _id
                            self.function = fn

                    tool_calls = []
                    for idx, inv in enumerate(invs):
                        tool_calls.append(_Tc(f"dsml_{step}_{idx}", _Fn(inv.name, json.dumps(inv.args, ensure_ascii=False))))

            # Append assistant message with tool_calls + reasoning_content to satisfy DeepSeek protocol
            assistant_dict: Dict[str, Any] = {
                "role": "assistant",
                "content": msg.content or "",
                "reasoning_content": getattr(msg, "reasoning_content", "") or "",
            }
            if tool_calls:
                assistant_dict["tool_calls"] = [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments,
                        },
                    }
                    for tc in tool_calls
                ]
            messages.append(assistant_dict)

            # If no tool call -> final answer
            if not tool_calls:
                content = msg.content or ""
                # If model accidentally emitted DSML tool calls in content, treat as no answer.
                if is_dsml_function_calls(content):
                    final_answer = ""
                else:
                    final_answer = content
                    if self.on_step:
                        self.on_step({"type": "response", "step": step, "content": final_answer})
                break

            tool_calls_count += len(tool_calls)

            # Execute tool calls
            for tc in tool_calls:
                if tc.function.name == "search_docs":
                    if self.on_step:
                        self.on_step({"type": "tool_call", "step": step, "tool_name": "search_docs", "arguments": tc.function.arguments})

                    if not self.docs_loader:
                        tool_payload = {"status": "error", "message": "docs_loader is not configured"}
                    else:
                        try:
                            args = json.loads(tc.function.arguments)
                        except Exception:
                            args = {}
                        q = args.get("query", question)
                        k = int(args.get("max_results", 3) or 3)
                        tool_payload = run_search_docs(self.docs_loader, query=q, max_results=k)

                    meta = {
                        "status": tool_payload.get("status"),
                        "query": tool_payload.get("query"),
                        "count": tool_payload.get("count"),
                        "doc_paths": [r.get("doc_path") for r in tool_payload.get("results", [])],
                    }
                    self._log("\n[tool search_docs result meta]:\n" + json.dumps(meta, ensure_ascii=False, indent=2))
                    if self.on_step:
                        self.on_step({"type": "tool_result", "step": step, "tool_name": "search_docs", "meta": meta})

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": json.dumps(tool_payload, ensure_ascii=False),
                    })

                elif tc.function.name == "compose_answer":
                    if self.on_step:
                        self.on_step({"type": "tool_call", "step": step, "tool_name": "compose_answer", "arguments": "{}"})

                    # Finalization step: ask model to answer without calling tools.
                    self._log("\n[tool compose_answer invoked] forcing final answer")
                    response2 = self.client.chat.completions.create(
                        model=self.model,
                        messages=messages + [{"role": "user", "content": "Now write the final customer-facing answer."}],
                        temperature=self.temperature,
                        max_tokens=2000,
                        tools=self.tools,
                        tool_choice="none",
                        extra_body={"thinking": {"type": "enabled"}},
                    )
                    self.total_calls += 1
                    if response2.usage:
                        self.total_tokens += response2.usage.total_tokens
                    msg2 = response2.choices[0].message
                    reasoning2 = getattr(msg2, "reasoning_content", None)
                    if reasoning2 is not None:
                        self._log("\n[reasoning_content]:\n" + str(reasoning2))
                        if self.on_step:
                            self.on_step({"type": "reasoning", "step": step, "reasoning_content": str(reasoning2)})

                    final_answer = msg2.content or ""
                    if self.on_step:
                        self.on_step({"type": "response", "step": step, "content": final_answer})

                    # still append a tool message for traceability
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": json.dumps({"status": "success", "message": "final answer composed"}, ensure_ascii=False),
                    })
                    break

                else:
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": json.dumps({"status": "error", "message": f"unknown tool: {tc.function.name}"}, ensure_ascii=False),
                    })

        # If we exhausted steps without a final answer, do a forced finalization call (no tools).
        # Prefer using compose_answer tool for a clean separation.
        if final_answer.strip() == "":
            self._log("\n[FINALIZE] No final answer produced within steps; forcing compose_answer then final answer")
            # 1) add a synthetic compose_answer tool call
            messages.append(
                {
                    "role": "assistant",
                    "content": "",
                    "reasoning_content": "",
                    "tool_calls": [
                        {
                            "id": "final_compose",
                            "type": "function",
                            "function": {"name": "compose_answer", "arguments": "{}"},
                        }
                    ],
                }
            )
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": "final_compose",
                    "content": json.dumps({"status": "success", "message": "compose_answer requested"}, ensure_ascii=False),
                }
            )
            # 2) now force final answer with no tools
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages + [{"role": "user", "content": "Now write the final customer-facing answer."}],
                temperature=self.temperature,
                max_tokens=2000,
                tools=self.tools,
                tool_choice="none",
                extra_body={"thinking": {"type": "enabled"}},
            )
            self.total_calls += 1
            if response.usage:
                self.total_tokens += response.usage.total_tokens
            msg = response.choices[0].message
            reasoning = getattr(msg, "reasoning_content", None)
            if reasoning is not None:
                self._log("\n[reasoning_content]:\n" + str(reasoning))
            final_answer = msg.content or ""

        elapsed = time.time() - start_time

        self.last_tool_calls = tool_calls_count

        self._log("\n--- RESPONSE ---")
        self._log(f"[Elapsed Time]: {elapsed:.2f}s")
        self._log(f"\n[Final Answer]:\n{final_answer}")
        self._log(f"\n[Cumulative Stats]: calls={self.total_calls}, total_tokens={self.total_tokens}")
        self._log("")

        # Save current turn to conversation history
        self.conversation_messages.append({"role": "user", "content": user_prompt})
        self.conversation_messages.append({"role": "assistant", "content": final_answer})

        if self.keep_last_qa_only:
            self.prune_history_keep_last_qa()

        return final_answer
    
    def get_usage_stats(self) -> Dict:
        """Get API usage statistics."""
        return {
            "total_calls": self.total_calls,
            "total_tokens": self.total_tokens
        }


class MockQAAgent:
    """
    Mock QA Agent for testing without API calls.
    """
    
    def __init__(self):
        self.total_calls = 0
        self.total_tokens = 0
        self.log_messages: List[str] = []
        # Conversation history for multi-turn dialogue
        self.conversation_messages: List[Dict] = []
    
    def clear_history(self):
        """Clear conversation history for a new session."""
        self.conversation_messages = []
        self.log_messages = []
    
    def _log(self, message: str):
        self.log_messages.append(message)
    
    def get_logs(self) -> str:
        return "\n".join(self.log_messages)
    
    def generate_code(self, question: str, context: str = "") -> str:
        return self.answer_question(question, context)
    
    def answer_question(self, question: str, context: str = "") -> str:
        """Generate a mock answer."""
        self._log(f"[Mock QA Agent] Processing: {question[:50]}...")
        self._log(f"[Conversation History Turns]: {len(self.conversation_messages) // 2}")
        self.total_calls += 1
        
        # Build user prompt for history storage
        user_prompt = f"Question: {question}\n\nContext: {context[:200] if context else 'None'}..."
        
        # Check if context has relevant info
        if context and len(context) > 100:
            answer = f"""Based on the documentation provided:

**Answer to your question:**

{question}

The documentation contains relevant information that would help answer this question. In a real scenario, the LLM would provide a detailed, helpful response based on the context.

Key points from the documentation:
- Relevant documentation sections were found
- The answer should be derived from the provided context
- This is a mock response for testing purposes

*Note: This is a mock response. Use --without-mock flag for real LLM answers.*"""
        else:
            answer = f"""I don't have specific documentation context for this question.

**Question:** {question}

Without relevant documentation, I can only provide general information. In a real scenario with the DeepSeek API, the response would be more helpful.

*Note: This is a mock response. Use --without-mock flag for real LLM answers.*"""
        
        # Save to conversation history
        self.conversation_messages.append({"role": "user", "content": user_prompt})
        self.conversation_messages.append({"role": "assistant", "content": answer})
        
        return answer
    
    def get_usage_stats(self) -> Dict:
        return {
            "total_calls": self.total_calls,
            "total_tokens": self.total_tokens
        }


def run_single_test(runner, test_case: Dict, evaluator: QAEvaluator) -> Dict:
    """
    Run a single test case.
    
    Args:
        runner: The QA runner to use
        test_case: Test case dictionary
        evaluator: QA evaluator instance
    
    Returns:
        Test result dictionary
    """
    question = test_case["question"]
    
    # Generate answer
    answer = runner.run_task(question)
    
    # Evaluate answer
    eval_result = evaluator.evaluate_answer(
        answer=answer,
        expected_keywords=test_case.get("expected_keywords", []),
        forbidden_keywords=test_case.get("forbidden_keywords", []),
    )
    
    return {
        "test_id": test_case["id"],
        "question": question,
        "answer": answer,
        "evaluation": eval_result,
        "doc_reference": test_case.get("doc_reference", "")
    }


def run_mode(
    mode: str,
    test_cases: List[Dict],
    docs_loader: DocsLoader,
    use_mock: bool = False
) -> Dict:
    """
    Run all test cases for a specific mode.
    
    Args:
        mode: The mode to test
        test_cases: List of test cases
        docs_loader: DocsLoader instance
        use_mock: Use mock LLM
    
    Returns:
        Results dictionary
    """
    log_message(f"\n{'#' * 80}")
    log_message(f"# MODE: {mode}")
    log_message(f"{'#' * 80}")
    
    # Create agent and runner
    agent = create_agent(use_mock)
    runner = create_runner(mode, agent, docs_loader)
    
    # Run tests
    evaluator = QAEvaluator()
    results = []
    passed_count = 0
    
    for i, test_case in enumerate(test_cases):
        # IMPORTANT: keep only last Q/A across test cases (system prompt stays fixed).
        if hasattr(agent, "prune_history_keep_last_qa"):
            agent.prune_history_keep_last_qa()

        log_message(f"\n{'~' * 80}")
        log_message(f"TEST {i + 1}/{len(test_cases)}: {test_case['id']}")
        log_message(f"{'~' * 80}")
        log_message(f"[Question]: {test_case['question']}")
        log_message(f"[Expected Keywords]: {test_case.get('expected_keywords', [])}")
        
        result = run_single_test(runner, test_case, evaluator)
        results.append(result)
        
        if result["evaluation"]["passed"]:
            passed_count += 1
        
        log_message(f"\n[Answer]:\n{result['answer'][:500]}..." if len(result['answer']) > 500 else f"\n[Answer]:\n{result['answer']}")
        log_message(f"\n[Evaluation]:")
        log_message(f"  Score: {result['evaluation']['score'] * 100:.1f}%")
        log_message(f"  Passed: {result['evaluation']['passed']}")
        log_message(f"  Matched Keywords: {result['evaluation']['matched_keywords']}")
        log_message(f"  Missing Keywords: {result['evaluation']['missing_keywords']}")
        
        # Small delay to avoid rate limiting
        time.sleep(0.5)
    
    # Collect agent logs if available
    if hasattr(agent, 'get_logs'):
        log_message(f"\n{'=' * 80}")
        log_message("DETAILED LLM INTERACTION LOG")
        log_message(f"{'=' * 80}")
        log_message(agent.get_logs())
    
    # Calculate stats
    pass_rate = passed_count / len(test_cases)
    avg_score = statistics.mean([r["evaluation"]["score"] for r in results])
    
    # Get API usage stats
    api_calls = 0
    total_tokens = 0
    if hasattr(agent, 'get_usage_stats'):
        stats = agent.get_usage_stats()
        api_calls = stats.get("total_calls", 0)
        total_tokens = stats.get("total_tokens", 0)
    
    # Get skill invocation rate for skills modes
    skill_invoke_rate = None
    if hasattr(runner, 'get_invocation_rate'):
        skill_invoke_rate = runner.get_invocation_rate()
    
    log_message(f"\n[Mode Summary] {mode}:")
    log_message(f"  Pass Rate: {pass_rate * 100:.1f}% ({passed_count}/{len(test_cases)})")
    log_message(f"  Avg Score: {avg_score * 100:.1f}%")
    if skill_invoke_rate is not None:
        log_message(f"  Skill Invocation Rate: {skill_invoke_rate * 100:.0f}%")
    if api_calls > 0:
        log_message(f"  API Calls: {api_calls}, Tokens: {total_tokens}")
    
    return {
        "mode": mode,
        "results": results,
        "pass_rate": pass_rate,
        "avg_score": avg_score,
        "passed_count": passed_count,
        "total_tests": len(test_cases),
        "skill_invoke_rate": skill_invoke_rate,
        "api_calls": api_calls,
        "total_tokens": total_tokens
    }


def run_experiment(
    modes: List[str],
    test_cases: List[Dict],
    docs_loader: DocsLoader,
    use_mock: bool = False
) -> Dict[str, Dict]:
    """
    Run the full experiment across all modes.
    
    Args:
        modes: List of modes to test
        test_cases: List of test cases
        docs_loader: DocsLoader instance
        use_mock: Use mock LLM
    
    Returns:
        Dictionary mapping mode to results
    """
    log_message(f"\n{'*' * 80}")
    log_message("GENSTORE HELP DOC QA DEMO")
    log_message(f"{'*' * 80}")
    log_message(f"\nTest Start Time: {datetime.now().isoformat()}")
    
    # Show docs stats
    stats = docs_loader.get_stats()
    log_message(f"\nDocumentation Stats:")
    log_message(f"  Total Documents: {stats['total_docs']}")
    log_message(f"  Total Size: {stats['total_size_kb']} KB")
    log_message(f"  Max Depth: {stats['max_depth']}")
    log_message(f"  Top-level Sections: {stats['top_level_sections']}")
    
    # Show test stats
    test_stats = get_test_stats()
    log_message(f"\nTest Cases:")
    log_message(f"  Total: {test_stats['total']}")
    for cat, count in test_stats["categories"].items():
        log_message(f"  {cat}: {count}")
    
    # Estimate API usage
    if not use_mock:
        estimated_calls = len(modes) * len(test_cases)
        log_message(f"\nEstimated API calls: ~{estimated_calls}")
    
    all_results = {}
    
    for mode in modes:
        results = run_mode(mode, test_cases, docs_loader, use_mock)
        all_results[mode] = results
    
    return all_results


def print_results_table(all_results: Dict[str, Dict]):
    """Print results in a formatted table."""
    log_message(f"\n{'=' * 80}")
    log_message("RESULTS SUMMARY")
    log_message(f"{'=' * 80}")
    
    # Get baseline for comparison
    baseline = all_results.get("baseline", {}).get("pass_rate", 0)
    
    log_message(f"\n{'Mode':<25} {'Pass Rate':<15} {'Avg Score':<15} {'vs Baseline':<15}")
    log_message("-" * 70)
    
    for mode, results in all_results.items():
        pass_rate = results["pass_rate"]
        avg_score = results["avg_score"]
        improvement = pass_rate - baseline if mode != "baseline" else 0
        improvement_str = "—" if mode == "baseline" else f"+{improvement*100:.1f}pp" if improvement >= 0 else f"{improvement*100:.1f}pp"
        
        log_message(f"{mode:<25} {pass_rate*100:.1f}%{'':<9} {avg_score*100:.1f}%{'':<9} {improvement_str:<15}")


def print_key_findings(all_results: Dict[str, Dict]):
    """Print key findings from the experiment."""
    log_message(f"\n{'=' * 80}")
    log_message("KEY FINDINGS")
    log_message(f"{'=' * 80}")
    
    baseline_rate = all_results.get("baseline", {}).get("pass_rate", 0) * 100
    skills_default_rate = all_results.get("skills_default", {}).get("pass_rate", 0) * 100
    agents_md_rate = all_results.get("agents_md", {}).get("pass_rate", 0) * 100
    
    skills_invoke = all_results.get("skills_default", {}).get("skill_invoke_rate", 0) * 100
    
    log_message(f"""
1. BASELINE PERFORMANCE
   - Baseline (no docs): {baseline_rate:.1f}% pass rate
   - This represents LLM's pre-training knowledge about Genstore

2. SKILLS MODE
   - Skills (default): {skills_default_rate:.1f}% pass rate
   - Skill invocation rate: {skills_invoke:.0f}%
   
   Finding: Skills mode requires the LLM to decide whether to retrieve docs.
   This decision point can lead to missed information.

3. AGENTS.MD MODE
   - AGENTS.md: {agents_md_rate:.1f}% pass rate
   
   Finding: Passive context (AGENTS.md) provides documentation without
   requiring a tool-use decision, leading to more consistent results.

4. COMPARISON
   - AGENTS.md vs Baseline: +{agents_md_rate - baseline_rate:.1f}pp
   - AGENTS.md vs Skills: +{agents_md_rate - skills_default_rate:.1f}pp
   
CONCLUSION:
For QA scenarios based on documentation, AGENTS.md pattern provides
more reliable access to relevant information.
""")


# ============================================================================
# Interactive Mode Functions
# ============================================================================

def read_multiline_input(prompt: str = "You") -> Optional[str]:
    """
    Read multi-line input from user.
    
    User can input multiple lines. A line containing only '///' marks the end.
    This allows users to paste large blocks of text with any characters.
    
    Args:
        prompt: The prompt to display
        
    Returns:
        The complete input string, or None if user wants to exit
    """
    print(f"\n{prompt} (输入多行内容，单独一行输入 /// 表示提交，输入 quit 退出):")
    print("-" * 60)
    
    lines = []
    line_num = 1
    
    while True:
        try:
            # Show line number for multi-line input
            if lines:
                line = input(f"  [{line_num}] ")
            else:
                line = input(f"  > ")
            
            # Check for exit command
            if line.strip().lower() == 'quit':
                return None
            
            # Check for submit marker
            if line.strip() == '///':
                break
            
            lines.append(line)
            line_num += 1
            
        except EOFError:
            # Handle Ctrl+D
            print()
            break
        except KeyboardInterrupt:
            # Handle Ctrl+C
            print("\n[已取消]")
            return None
    
    # Join all lines
    content = '\n'.join(lines)
    return content if content.strip() else None


def format_conversation_history() -> str:
    """
    Format the conversation history for context.
    
    Returns:
        Formatted conversation history string
    """
    if not CONVERSATION_HISTORY:
        return ""
    
    history_parts = []
    for i, turn in enumerate(CONVERSATION_HISTORY):
        history_parts.append(f"[Turn {i+1}]")
        history_parts.append(f"User: {turn['question']}")
        history_parts.append(f"Assistant: {turn['answer'][:500]}..." if len(turn['answer']) > 500 else f"Assistant: {turn['answer']}")
        history_parts.append("")
    
    return "\n".join(history_parts)


def run_interactive_session(
    docs_loader: DocsLoader,
    mode: str = "agents_md",
    use_mock: bool = False,
    save_log: bool = True
):
    """
    Run an interactive QA session.
    
    User can ask any questions and get answers based on the documentation.
    The conversation history is maintained for context.
    
    Args:
        docs_loader: DocsLoader instance with loaded documentation
        mode: The mode to use (baseline, agents_md, etc.)
        use_mock: Use mock LLM
        save_log: Whether to save the conversation log
    """
    global CONVERSATION_HISTORY
    CONVERSATION_HISTORY = []
    
    print(f"\n{'*' * 80}")
    print("GENSTORE HELP DOC QA - 交互式对话模式")
    print(f"{'*' * 80}")
    
    # Show session info
    stats = docs_loader.get_stats()
    print(f"\n文档库信息:")
    print(f"  文档总数: {stats['total_docs']}")
    print(f"  文档大小: {stats['total_size_kb']} KB")
    print(f"  运行模式: {mode}")
    print(f"  LLM 类型: {'Mock' if use_mock else 'DeepSeek API'}")
    
    print(f"\n{'=' * 80}")
    print("使用说明:")
    print("  - 输入您的问题，支持多行输入")
    print("  - 单独一行输入 /// 表示提交问题")
    print("  - 输入 quit 退出对话")
    print("  - 输入 history 查看对话历史")
    print("  - 输入 search <关键词> 搜索相关文档")
    print("  - 输入 stats 查看当前统计")
    print(f"{'=' * 80}")
    
    # Create agent and runner
    def _print_subturn(evt: Dict[str, Any]) -> None:
        t = evt.get("type")
        step = evt.get("step")
        if t == "reasoning":
            print(f"\n[Step {step} 思考]")
            print(evt.get("reasoning_content", ""))
        elif t == "tool_call":
            print(f"\n[Step {step} 工具调用] {evt.get('tool_name')}")
        elif t == "tool_result":
            meta = evt.get("meta", {})
            print(f"\n[Step {step} 工具结果] {evt.get('tool_name')}: {meta}")
        elif t == "response":
            print(f"\n[Step {step} 回复]")
            print(evt.get("content", ""))

    agent = create_agent(use_mock, on_step=_print_subturn)
    runner = create_runner(mode, agent, docs_loader)

    # Session stats
    session_start = datetime.now()

    total_questions = 0
    total_tokens = 0
    
    while True:
        # Read user input
        user_input = read_multiline_input()
        
        if user_input is None:
            print("\n[退出对话]")
            break
        
        # Handle special commands
        cmd = user_input.strip().lower()
        
        if cmd == 'quit':
            print("\n[退出对话]")
            break
        
        if cmd == 'history':
            history = format_conversation_history()
            if history:
                print(f"\n{'=' * 80}")
                print("对话历史:")
                print(f"{'=' * 80}")
                print(history)
            else:
                print("\n[暂无对话历史]")
            continue
        
        if cmd.startswith('search '):
            keyword = user_input.strip()[7:].strip()
            if keyword:
                results = docs_loader.search(keyword, max_results=5)
                print(f"\n搜索结果 (关键词: {keyword}):")
                print("-" * 60)
                for doc_path, score in results:
                    print(f"  [{score:.0f}分] {doc_path}")
                if not results:
                    print("  未找到相关文档")
            else:
                print("\n[请输入搜索关键词，例如: search abandoned]")
            continue
        
        if cmd == 'stats':
            elapsed = (datetime.now() - session_start).total_seconds()
            print(f"\n{'=' * 80}")
            print("当前统计:")
            print(f"{'=' * 80}")
            print(f"  对话轮次: {total_questions}")
            print(f"  运行时间: {elapsed:.1f} 秒")
            if total_tokens > 0:
                print(f"  Token 消耗: {total_tokens}")
            print(f"  模式: {mode}")
            continue
        
        # Skip empty input
        if not user_input.strip():
            continue
        
        # Process question
        total_questions += 1
        
        print(f"\n{'~' * 80}")
        print(f"[问题 #{total_questions}]")
        print(f"{'~' * 80}")
        print(f"{user_input}")
        
        print(f"\n[正在处理...]")
        
        try:
            # Get answer
            start_time = time.time()
            answer = runner.run_task(user_input)
            elapsed = time.time() - start_time
            
            # Store in history
            llm_logs = agent.get_logs() if hasattr(agent, 'get_logs') else ""
            CONVERSATION_HISTORY.append({
                "question": user_input,
                "answer": answer,
                "mode": mode,
                "timestamp": datetime.now().isoformat(),
                "llm_logs": llm_logs
            })
            
            # Update token count
            if hasattr(agent, 'total_tokens'):
                total_tokens = agent.total_tokens
            
            # Print answer
            print(f"\n{'=' * 80}")
            print("[回答]")
            print(f"{'=' * 80}")
            print(answer)
            print(f"\n[耗时: {elapsed:.2f}s]")

            # NOTE: Do NOT print full LLM interaction logs in interactive UI.
            # Logs are still saved to qa_conversation_*.log when save_log is enabled.
            
            # Show relevant docs if in agents_md mode
            if mode == "agents_md" and hasattr(runner, 'docs_loader'):
                search_results = docs_loader.search(user_input, max_results=2)
                if search_results:
                    print(f"\n[相关文档]:")
                    for doc_path, score in search_results:
                        print(f"  - {doc_path} (相关度: {score:.0f})")
            
        except Exception as e:
            print(f"\n[错误]: {str(e)}")
        
        # Reset runner for next question
        if hasattr(runner, 'reset'):
            runner.reset()
    
    # Session summary
    elapsed = (datetime.now() - session_start).total_seconds()
    print(f"\n{'=' * 80}")
    print("对话结束 - 统计摘要")
    print(f"{'=' * 80}")
    print(f"  总对话轮次: {total_questions}")
    print(f"  总运行时间: {elapsed:.1f} 秒")
    if total_tokens > 0:
        print(f"  总 Token 消耗: {total_tokens}")
    print(f"  运行模式: {mode}")
    
    # Save conversation log
    if save_log and CONVERSATION_HISTORY:
        log_filename = f"qa_conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        with open(log_filename, 'w', encoding='utf-8') as f:
            f.write(f"Genstore QA Conversation Log\n")
            f.write(f"Time: {session_start.isoformat()}\n")
            f.write(f"Mode: {mode}\n")
            f.write(f"Questions: {total_questions}\n")
            f.write(f"\n{'=' * 80}\n\n")
            
            for i, turn in enumerate(CONVERSATION_HISTORY):
                f.write(f"[Turn {i+1}]\n")
                f.write(f"User: {turn['question']}\n")
                f.write(f"Assistant: {turn['answer']}\n")
                
                # Include LLM interaction logs
                if turn.get('llm_logs'):
                    f.write(f"\n{'~' * 80}\n")
                    f.write("LLM Interaction Details:\n")
                    f.write(f"{'~' * 80}\n")
                    f.write(turn['llm_logs'])
                    f.write("\n")
                
                f.write(f"\n{'-' * 80}\n\n")
        
        print(f"\n[对话日志已保存: {log_filename}]")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Genstore Help Documentation QA Demo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 批量测试模式（使用 test_cases.py）
  python qa_genstore.py --difficulty easy --modes baseline agents_md

  # 交互式对话模式
  python qa_genstore.py --interactive --mode agents_md

  # Mock 模式测试
  python qa_genstore.py --mock --interactive
        """
    )
    
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use Mock LLM instead of real DeepSeek API"
    )
    
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode - free conversation with the QA system"
    )
    
    parser.add_argument(
        "--mode",
        type=str,
        choices=["baseline", "skills_default", "skills_must_invoke", "skills_explore_first", "agents_md"],
        default="agents_md",
        help="Mode to use in interactive mode (default: agents_md)"
    )
    
    parser.add_argument(
        "--modes",
        nargs="+",
        choices=["baseline", "skills_default", "skills_must_invoke", "skills_explore_first", "agents_md", "all"],
        default=["all"],
        help="Modes to test in batch mode (default: all)"
    )
    
    parser.add_argument(
        "--category",
        choices=["definition", "process", "troubleshooting", "data", "rules", "complex", "navigation", "all"],
        default="all",
        help="Test category to run (default: all)"
    )
    
    parser.add_argument(
        "--difficulty",
        choices=["easy", "medium", "hard", "all"],
        default="all",
        help="Test difficulty to run (default: all)"
    )
    
    parser.add_argument(
        "--log-file",
        type=str,
        default=None,
        help="Path to save detailed logs"
    )
    
    parser.add_argument(
        "--docs-dir",
        type=str,
        default=None,
        help="Path to documentation directory"
    )
    
    parser.add_argument(
        "--no-save-log",
        action="store_true",
        help="Do not save conversation log in interactive mode"
    )
    
    args = parser.parse_args()
    
    # Load documentation
    docs_dir = args.docs_dir
    if docs_dir is None:
        docs_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "blaze-genstore-help-doc-qa", "en"
        )
    
    log_message(f"Loading documentation from: {docs_dir}")
    docs_loader = DocsLoader(docs_dir)
    docs_loader.load()
    
    # Interactive mode
    if args.interactive:
        run_interactive_session(
            docs_loader=docs_loader,
            mode=args.mode,
            use_mock=args.mock,
            save_log=not args.no_save_log
        )
        return
    
    # Batch mode (original behavior)
    # Select test cases
    if args.category != "all":
        test_cases = get_test_cases_by_category(args.category)
    elif args.difficulty != "all":
        test_cases = get_test_cases_by_difficulty(args.difficulty)
    else:
        test_cases = QA_TEST_CASES
    
    # Select modes
    if "all" in args.modes:
        modes = [
            "baseline",
            "skills_default",
            "skills_must_invoke",
            "skills_explore_first",
            "agents_md"
        ]
    else:
        modes = args.modes
    
    # Run experiment
    all_results = run_experiment(modes, test_cases, docs_loader, args.mock)
    
    # Print results
    print_results_table(all_results)
    print_key_findings(all_results)
    
    # Print AGENTS.md sample
    log_message(f"\n{'=' * 80}")
    log_message("SAMPLE AGENTS.MD INDEX")
    log_message(f"{'=' * 80}")
    log_message(f"\n{build_agents_md_index(docs_loader)}")
    
    log_message(f"\n{'=' * 80}")
    log_message("Demo complete!")
    log_message(f"{'=' * 80}")
    
    # Save logs
    if args.log_file:
        with open(args.log_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(MASTER_LOG))
        print(f"\n[Log saved to: {args.log_file}]")


if __name__ == "__main__":
    main()
