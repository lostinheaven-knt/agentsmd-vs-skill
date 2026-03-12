from __future__ import annotations

from typing import Any, Dict


def compose_answer_tool_def() -> Dict[str, Any]:
    return {
        "type": "function",
        "function": {
            "name": "compose_answer",
            "description": (
                "Compose the final customer-facing answer based on all information gathered so far. "
                "Call this when you have enough context and should stop searching."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    }
