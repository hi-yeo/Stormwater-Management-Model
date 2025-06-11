"""Node data and operations matching node.c."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    """Simple node with name and water depth."""

    name: str
    depth: float = 0.0


def reset(node: Node) -> None:
    """Reset node state (placeholder for C version)."""
    node.depth = 0.0
