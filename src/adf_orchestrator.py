"""ADF-like pipeline: ordered activities with logging."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ACTIVITIES = [
    ("Copy to bronze", [sys.executable, "-m", "src.run_lab"]),
    ("Publish silver/gold", [sys.executable, "-c", "print('publish step stub')"]),
]

def main():
    print("ADF-style orchestrator (local educational)")
    for name, cmd in ACTIVITIES:
        print(f"Activity: {name}")
        subprocess.run(cmd, cwd=ROOT, check=False)
    print("Pipeline finished")

if __name__ == "__main__":
    main()
