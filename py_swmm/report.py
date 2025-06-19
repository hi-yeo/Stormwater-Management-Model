from __future__ import annotations

from pathlib import Path
from . import project as project_mod


def write_report(project: project_mod.Project, path: Path, lines: list[str] | None = None) -> None:
    if lines is None:
        lines = [f"Step {i}: flow={project.flow:.3f}\n" for i in range(project.options.steps)]
    path.write_text("".join(lines))
