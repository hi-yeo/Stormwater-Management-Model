"""Project data management."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .objects import Node, Link


@dataclass
class Options:
    steps: int = 10  # number of time steps to simulate


dataclass = dataclass


class Project:
    """Minimal representation of a SWMM project."""

    def __init__(self) -> None:
        self.options = Options()
        self.flow = 0.0
        self.nodes: list[Node] = []
        self.links: list[Link] = []

    def load(self, path: Path) -> None:
        """Load an input file.

        This is a stub parser that only looks for a single option
        'STEPS' specifying how many steps to simulate.
        """
        from .input import read_project

        proj = read_project(path)
        self.options = proj.options
        self.nodes = proj.nodes
        self.links = proj.links
