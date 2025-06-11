"""Minimal Python translation of the simplified SWMM solver."""

from __future__ import annotations

from .swmm5 import swmm_run
from .objects import Node, Link, Subcatch, RainGage

__all__ = ["swmm_run", "Node", "Link", "Subcatch", "RainGage"]
