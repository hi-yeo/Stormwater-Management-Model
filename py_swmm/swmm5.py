"""Simplified SWMM runtime interface."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from . import project as project_mod
from . import runoff
from . import routing
from . import report as report_mod


def swmm_run(inp_path: str, report_path: Optional[str] = None) -> None:
    """Run a simplified SWMM simulation.

    Parameters
    ----------
    inp_path : str
        Path to the SWMM input (.inp) file.
    report_path : str, optional
        Where to write a simple text report. If omitted, output is
        printed to stdout.
    """
    inp = Path(inp_path)
    if not inp.exists():
        raise FileNotFoundError(inp)

    project = project_mod.Project()
    project.load(inp)

    # Very small time stepping loop. The real engine supports many
    # options that are omitted here.
    report_lines = []
    for step in range(project.options.steps):
        runoff.update_subcatchments(project)
        routing.execute(project)
        report_lines.append(f"Step {step}: flow={project.flow:.3f}\n")

    output = "".join(report_lines)
    if report_path:
        report_mod.write_report(project, Path(report_path), report_lines)
    else:
        print(output)
