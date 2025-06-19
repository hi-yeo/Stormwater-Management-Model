from __future__ import annotations

from . import kinwave
from . import project as project_mod
from . import node as node_mod
from . import link as link_mod


def execute(project: project_mod.Project) -> None:
    """Perform one routing step using kinematic wave."""
    for link in project.links:
        kinwave.route(project)
        link.flow = project.flow
        node_mod.reset(link.from_node)
        node_mod.reset(link.to_node)
        link_mod.reset(link)
