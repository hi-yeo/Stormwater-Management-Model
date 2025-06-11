"""Minimal Python translation of the simplified SWMM solver.

This package provides a limited, kinematic-wave only version of SWMM
implemented in pure Python. It is not a feature complete port but
mirrors the basic structure of the original C solver.
"""

from .swmm5 import swmm_run

__all__ = ["swmm_run"]
