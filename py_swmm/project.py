"""Project data management."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .objects import Node, Link, Subcatch, RainGage


@dataclass
class Options:
    steps: int = 10  # number of time steps to simulate


class Project:
    """Minimal representation of a SWMM project."""

    def __init__(self) -> None:
        self.options = Options()
        self.flow = 0.0
        self.nodes: list[Node] = []
        self.links: list[Link] = []
        self.subcatchments: list[Subcatch] = []
        self.gages: list[RainGage] = []

    def load(self, path: Path) -> None:
        """Load an input file."""
        from .input import read_project

        proj = read_project(path)
        self.options = proj.options
        self.nodes = proj.nodes
        self.links = proj.links
        self.subcatchments = proj.subcatchments
        self.gages = proj.gages
