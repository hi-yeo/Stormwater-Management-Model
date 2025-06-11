"""Rain gage data to mimic gage.c."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RainGage:
    """Simple precipitation source."""

    name: str
    rainfall: float = 0.0
