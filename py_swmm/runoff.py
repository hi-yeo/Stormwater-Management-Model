"""Simplified runoff calculations."""

from __future__ import annotations

from . import project as project_mod
from . import subcatch as subcatch_mod


def update_subcatchments(project: project_mod.Project) -> None:
    """Update runoff for all subcatchments."""
    for sc in project.subcatchments:
        project.flow += subcatch_mod.generate_runoff(sc)
