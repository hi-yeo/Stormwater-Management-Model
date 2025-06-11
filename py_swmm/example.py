"""Example usage of the minimal Python SWMM."""

from pathlib import Path
from . import swmm5


if __name__ == "__main__":
    inp = Path(__file__).with_name("example.inp")
    if not inp.exists():
        inp.write_text("STEPS 5\nNODE J1\nNODE J2\nLINK L1 J1 J2\n")
    swmm5.swmm_run(str(inp))
