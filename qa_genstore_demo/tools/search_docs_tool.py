from __future__ import annotations

import json
from typing import Any, Dict, List, Optional


def search_docs_tool_def() -> Dict[str, Any]:
    """OpenAI tool definition for searching docs."""

    return {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": "Search Genstore help documentation and return the most relevant full documents.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of documents to return",
                        "default": 3,
                        "minimum": 1,
                        "maximum": 10,
                    },
                },
                "required": ["query"],
            },
        },
    }


def run_search_docs(docs_loader, query: str, max_results: int = 3) -> Dict[str, Any]:
    """Execute search_docs tool. Returns JSON-serializable payload."""

    results: List[Dict[str, Any]] = []
    search_results = docs_loader.search(query, max_results=max_results)
    for doc_path, score in search_results:
        keys = doc_path.split("/")
        content = docs_loader.get_doc(*keys)
        if content:
            results.append(
                {
                    "doc_path": doc_path,
                    "score": score,
                    "content": content,
                }
            )

    return {
        "status": "success",
        "query": query,
        "count": len(results),
        "results": results,
    }
