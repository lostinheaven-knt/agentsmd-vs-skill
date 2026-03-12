from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


_DSML_INVOKE_RE = re.compile(
    r"<\|DSML\|invoke\s+name=\"(?P<name>[^\"]+)\">(?P<body>[\s\S]*?)</\|DSML\|invoke\>",
    re.MULTILINE,
)

_DSML_PARAM_RE = re.compile(
    r"<\|DSML\|parameter\s+name=\"(?P<name>[^\"]+)\"[^>]*>(?P<value>[\s\S]*?)</\|DSML\|parameter\>",
    re.MULTILINE,
)


@dataclass
class DsmlInvoke:
    name: str
    args: Dict[str, Any]


def parse_dsml_invokes(text: str) -> List[DsmlInvoke]:
    if not text:
        return []

    invokes: List[DsmlInvoke] = []
    for m in _DSML_INVOKE_RE.finditer(text):
        name = m.group("name").strip()
        body = m.group("body")
        args: Dict[str, Any] = {}
        for pm in _DSML_PARAM_RE.finditer(body):
            k = pm.group("name").strip()
            v = pm.group("value").strip()
            # try parse json primitives
            try:
                args[k] = json.loads(v)
            except Exception:
                args[k] = v
        invokes.append(DsmlInvoke(name=name, args=args))
    return invokes


def is_dsml_function_calls(text: str) -> bool:
    return bool(text and "<｜DSML｜function_calls>" in text)
