from __future__ import annotations

from pathlib import Path
from . import project as project_mod


def read_project(path: Path) -> project_mod.Project:
    """Parse a minimal .inp file and return a Project."""
    proj = project_mod.Project()
    nodes = []
    links = []
    subcatchments = []
    gages = []
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
        elif key == 'SUBCATCH' and len(parts) > 2:
            name = parts[1]
            try:
                area = float(parts[2])
            except ValueError:
                area = 0.0
            subcatchments.append(project_mod.Subcatch(name, area))
        elif key == 'GAGE' and len(parts) > 1:
            gages.append(project_mod.RainGage(parts[1]))
    proj.nodes = nodes
    proj.links = links
    proj.subcatchments = subcatchments
    proj.gages = gages
    return proj
