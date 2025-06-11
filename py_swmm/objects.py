from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    name: str
    depth: float = 0.0


@dataclass
class Link:
    name: str
    from_node: Node
    to_node: Node
    flow: float = 0.0
