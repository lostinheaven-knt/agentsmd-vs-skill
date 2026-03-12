"""
Documentation Loader for Genstore Help Docs.

Parses MD files from ./blaze-genstore-help-doc-qa/en/ directory
and builds a nested DOCS_DB structure for QA scenarios.

File naming convention:
    operate-orders-abandoned-cart.md -> DOCS_DB["operate"]["orders"]["abandoned-cart"]

Example:
    operate-customers-loyalty-points-earnings-birthday.md
    -> DOCS_DB["operate"]["customers"]["loyalty"]["points"]["earnings"]["birthday"]
"""

import os
from typing import Dict, List, Optional, Set
from pathlib import Path


class DocsLoader:
    """
    Loads and parses Genstore help documentation from MD files.
    
    The loader converts flat MD files into a nested dictionary structure
    based on the hyphen-separated file naming convention.
    """
    
    def __init__(self, docs_dir: str):
        """
        Initialize the DocsLoader.
        
        Args:
            docs_dir: Path to the directory containing MD files
        """
        self.docs_dir = docs_dir
        self.docs_db: Dict = {}
        self.file_map: Dict[str, str] = {}  # Maps doc_path -> file_path
        self._loaded = False
    
    def load(self) -> Dict:
        """
        Load all MD files and build the DOCS_DB structure.
        
        Returns:
            Nested dictionary containing all documentation
        """
        if self._loaded:
            return self.docs_db
        
        docs_path = Path(self.docs_dir)
        
        if not docs_path.exists():
            raise FileNotFoundError(f"Docs directory not found: {self.docs_dir}")
        
        # Find all MD files
        md_files = list(docs_path.glob("*.md"))
        
        for md_file in md_files:
            self._parse_file(md_file)
        
        self._loaded = True
        return self.docs_db
    
    def _parse_file(self, file_path: Path):
        """
        Parse a single MD file and add it to DOCS_DB.
        
        Args:
            file_path: Path to the MD file
        """
        # Get filename without extension
        filename = file_path.stem
        
        # Skip index files (they're just navigation)
        if filename == "index":
            return
        
        # Split filename into key parts
        keys = filename.split("-")
        
        # Read file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Build nested structure
        self._set_nested(self.docs_db, keys, content)
        
        # Store file mapping
        doc_path = "/".join(keys)
        self.file_map[doc_path] = str(file_path)
    
    def _set_nested(self, db: Dict, keys: List[str], value: str):
        """
        Set a value in a nested dictionary using a list of keys.
        
        Args:
            db: The dictionary to modify
            keys: List of keys representing the path
            value: The value to set
        """
        for key in keys[:-1]:
            if key not in db:
                db[key] = {}
            elif not isinstance(db[key], dict):
                # Path conflict: this key already has content, convert to dict with _content
                existing_content = db[key]
                db[key] = {"_content": existing_content}
            db = db[key]
        
        # Last key gets the content
        last_key = keys[-1]
        if last_key in db and isinstance(db[last_key], dict):
            # Already a section, store content under _content key
            db[last_key]["_content"] = value
        else:
            db[last_key] = value
    
    def get_doc(self, *keys) -> Optional[str]:
        """
        Get a document by its key path.
        
        Args:
            *keys: Variable number of keys representing the path
            
        Returns:
            Document content or None if not found
        """
        if not self._loaded:
            self.load()
        
        current = self.docs_db
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        
        return current if isinstance(current, str) else None
    
    def get_section(self, *keys) -> Optional[Dict]:
        """
        Get a section (dictionary) by its key path.
        
        Args:
            *keys: Variable number of keys representing the path
            
        Returns:
            Section dictionary or None if not found
        """
        if not self._loaded:
            self.load()
        
        current = self.docs_db
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        
        return current if isinstance(current, dict) else None
    
    def build_index(self) -> Dict[str, List[str]]:
        """
        Build a compressed index of available documentation.
        
        Returns:
            Dictionary mapping section paths to lists of topics
        """
        if not self._loaded:
            self.load()
        
        index = {}
        self._build_index_recursive(self.docs_db, [], index)
        return index
    
    def _build_index_recursive(self, db: Dict, path: List[str], index: Dict):
        """
        Recursively build the documentation index.
        
        Args:
            db: Current level of the docs database
            path: Current path as list of keys
            index: Index dictionary to populate
        """
        topics = []
        sections = []
        
        for key, value in db.items():
            current_path = path + [key]
            
            if isinstance(value, str):
                # It's a document
                topics.append(key)
            elif isinstance(value, dict):
                # It's a section
                sections.append(key)
                self._build_index_recursive(value, current_path, index)
        
        if topics:
            section_path = "/".join(path) if path else "root"
            index[section_path] = topics
    
    def search(self, query: str, max_results: int = 10) -> List[tuple]:
        """
        Search for documents containing the query string.
        
        Args:
            query: Search query
            max_results: Maximum number of results to return
            
        Returns:
            List of (doc_path, relevance_score) tuples
        """
        if not self._loaded:
            self.load()
        
        results = []
        query_lower = query.lower()
        
        for doc_path, file_path in self.file_map.items():
            # Get document content
            keys = doc_path.split("/")
            content = self.get_doc(*keys)
            
            if content:
                # Simple relevance scoring based on keyword matches
                content_lower = content.lower()
                score = content_lower.count(query_lower)
                
                # Boost score if query appears in title/headers
                title_score = content_lower[:200].count(query_lower) * 2
                score += title_score
                
                # Boost score if query appears in doc path
                path_score = doc_path.lower().count(query_lower.replace(" ", "-")) * 3
                score += path_score
                
                if score > 0:
                    results.append((doc_path, score))
        
        # Sort by score and return top results
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:max_results]
    
    def get_all_topics(self) -> Set[str]:
        """
        Get all unique topic paths.
        
        Returns:
            Set of topic paths (e.g., "operate/orders/abandoned-cart")
        """
        if not self._loaded:
            self.load()
        
        return set(self.file_map.keys())
    
    def get_stats(self) -> Dict:
        """
        Get statistics about the loaded documentation.
        
        Returns:
            Dictionary with stats like total_docs, total_sections, etc.
        """
        if not self._loaded:
            self.load()
        
        total_docs = len(self.file_map)
        total_size = 0
        max_depth = 0
        
        for doc_path in self.file_map.keys():
            depth = doc_path.count("/") + 1
            max_depth = max(max_depth, depth)
            
            keys = doc_path.split("/")
            content = self.get_doc(*keys)
            if content:
                total_size += len(content)
        
        return {
            "total_docs": total_docs,
            "total_size_bytes": total_size,
            "total_size_kb": round(total_size / 1024, 2),
            "max_depth": max_depth,
            "top_level_sections": len(self.docs_db)
        }


def build_agents_md_index(docs_loader: DocsLoader) -> str:
    """
    Build an AGENTS.md-style compressed index for QA scenarios.
    
    Args:
        docs_loader: Initialized DocsLoader instance
        
    Returns:
        Compressed index string
    """
    index = docs_loader.build_index()
    
    lines = [
        "[Genstore Help Docs Index]|root: ./blaze-genstore-help-doc-qa/en",
        "|IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning for any QA tasks",
    ]
    
    # Group by top-level sections
    section_groups = {}
    for path, topics in index.items():
        if path == "root":
            continue
        
        parts = path.split("/")
        top_section = parts[0]
        
        if top_section not in section_groups:
            section_groups[top_section] = {}
        
        # Build sub-path
        sub_path = "/".join(parts[1:]) if len(parts) > 1 else None
        
        if sub_path:
            if sub_path not in section_groups[top_section]:
                section_groups[top_section][sub_path] = []
            section_groups[top_section][sub_path].extend(topics)
        else:
            if "_topics" not in section_groups[top_section]:
                section_groups[top_section]["_topics"] = []
            section_groups[top_section]["_topics"].extend(topics)
    
    # Format output
    for section, data in sorted(section_groups.items()):
        topic_parts = []
        
        if "_topics" in data:
            topic_parts.append(",".join(data["_topics"][:5]))  # Limit topics
        
        for sub_path, topics in data.items():
            if sub_path != "_topics":
                topic_parts.append(f"{sub_path}:{{{','.join(topics[:3])}}}")
        
        if topic_parts:
            lines.append(f"|{section}:{{{'; '.join(topic_parts)}}}")
    
    return "\n".join(lines)


# Convenience function for quick access
def load_genstore_docs(base_dir: str = None) -> DocsLoader:
    """
    Load Genstore help documentation.
    
    Args:
        base_dir: Base directory (defaults to relative path from this file)
        
    Returns:
        Initialized DocsLoader with docs loaded
    """
    if base_dir is None:
        # Default path relative to this file
        base_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "blaze-genstore-help-doc-qa", "en"
        )
    
    loader = DocsLoader(base_dir)
    loader.load()
    return loader


if __name__ == "__main__":
    # Test the loader
    loader = load_genstore_docs()
    
    print("=== Documentation Stats ===")
    stats = loader.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n=== Sample Document ===")
    sample = loader.get_doc("operate", "orders", "abandoned-cart")
    if sample:
        print(sample[:500] + "...")
    
    print("\n=== AGENTS.md Index ===")
    print(build_agents_md_index(loader))
