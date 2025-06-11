"""Project data management."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Options:
    steps: int = 10  # number of time steps to simulate


dataclass = dataclass


class Project:
    """Minimal representation of a SWMM project."""

    def __init__(self) -> None:
        self.options = Options()
        self.flow = 0.0

    def load(self, path: Path) -> None:
        """Load an input file.

        This is a stub parser that only looks for a single option
        'STEPS' specifying how many steps to simulate.
        """
        for line in path.read_text().splitlines():
            line = line.strip()
            if line.startswith("STEPS"):
                try:
                    self.options.steps = int(line.split()[1])
                except (IndexError, ValueError):
                    pass
