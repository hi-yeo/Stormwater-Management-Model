"""Subcatchment representation, mirroring subcatch.c."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Subcatch:
    """Basic subcatchment with area and runoff."""

    name: str
    area: float = 0.0
    runoff: float = 0.0


def generate_runoff(subcatch: Subcatch) -> float:
    """Very small runoff placeholder calculation."""
    subcatch.runoff += 0.1 * subcatch.area
    return subcatch.runoff
