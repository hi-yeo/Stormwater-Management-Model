"""Simplified SWMM runtime interface."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from . import project as project_mod
from . import runoff
from . import routing
from . import report as report_mod
from . import stats as stats_mod
from . import massbal as massbal_mod


def swmm_run(inp_path: str, report_path: Optional[str] = None) -> None:
    """Run a simplified SWMM simulation."""
    inp = Path(inp_path)
    if not inp.exists():
        raise FileNotFoundError(inp)

    project = project_mod.Project()
    project.load(inp)
    stats = stats_mod.Stats()

    report_lines = []
    for step in range(project.options.steps):
        runoff.update_subcatchments(project)
        routing.execute(project)
        massbal_mod.update()
        stats_mod.update(stats)
        report_lines.append(
            f"Step {step}: flow={project.flow:.3f}, steps={stats.steps_completed}\n"
        )

    if report_path:
        report_mod.write_report(project, Path(report_path), report_lines)
    else:
        print("".join(report_lines))
