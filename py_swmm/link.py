"""Link data and operations matching link.c."""

from __future__ import annotations

from dataclasses import dataclass

from .node import Node


@dataclass
class Link:
    """Simple link connecting two nodes."""

    name: str
    from_node: Node
    to_node: Node
    flow: float = 0.0


def reset(link: Link) -> None:
    """Reset link state (placeholder for C version)."""
    link.flow = 0.0
