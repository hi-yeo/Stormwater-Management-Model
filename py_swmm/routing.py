from __future__ import annotations

from . import kinwave
from . import project as project_mod


def execute(project: project_mod.Project) -> None:
    """Perform one routing step using kinematic wave."""
    for link in project.links:
        kinwave.route(project)
        link.flow = project.flow
