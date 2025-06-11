from __future__ import annotations

from pathlib import Path
from . import project as project_mod


def read_project(path: Path) -> project_mod.Project:
    """Parse a minimal .inp file and return a Project."""
    proj = project_mod.Project()
    nodes = []
    links = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith(';'):
            continue
        parts = line.split()
        key = parts[0].upper()
        if key == 'STEPS':
            try:
                proj.options.steps = int(parts[1])
            except (IndexError, ValueError):
                pass
        elif key == 'NODE' and len(parts) > 1:
            nodes.append(project_mod.Node(parts[1]))
        elif key == 'LINK' and len(parts) > 3:
            from_node = project_mod.Node(parts[2])
            to_node = project_mod.Node(parts[3])
            links.append(project_mod.Link(parts[1], from_node, to_node))
    proj.nodes = nodes
    proj.links = links
    return proj
