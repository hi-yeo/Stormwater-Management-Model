"""Example usage of the minimal Python SWMM."""

from pathlib import Path
from . import swmm5


if __name__ == "__main__":
    inp = Path(__file__).with_name("example.inp")
    if not inp.exists():
        inp.write_text(
            "\n".join([
                "STEPS 5",
                "NODE J1",
                "NODE J2",
                "LINK L1 J1 J2",
                "SUBCATCH S1 1.0",
                "GAGE G1",
            ])
        )
    swmm5.swmm_run(str(inp))
