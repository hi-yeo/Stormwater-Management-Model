"""Extremely simplified kinematic wave routing."""

from __future__ import annotations

from . import project as project_mod


DEF_FLOW_INCREMENT = 1.0


def route(project: project_mod.Project) -> None:
    """Update project flow using a trivial kinematic approximation."""
    project.flow += DEF_FLOW_INCREMENT
