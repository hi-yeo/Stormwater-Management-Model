"""Simplified runoff calculations."""

from __future__ import annotations

from . import project as project_mod


def update_subcatchments(project: project_mod.Project) -> None:
    """Dummy runoff calculation.

    Increments project flow slightly to emulate runoff generation.
    """
    project.flow += 0.5
