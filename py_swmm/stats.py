"""Statistics tracker corresponding to stats.c."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Stats:
    steps_completed: int = 0


def update(stats: Stats) -> None:
    stats.steps_completed += 1
