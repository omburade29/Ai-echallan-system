"""Build the React UI (if needed) and serve FE + BE on one HTTP link.

Open: http://127.0.0.1:8000/
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FRONTEND = ROOT / "frontend"
BACKEND = ROOT / "backend"
DIST_INDEX = FRONTEND / "dist" / "index.html"
VENV_PYTHON = BACKEND / ".venv" / "Scripts" / "python.exe"


def ensure_frontend_build() -> None:
    if DIST_INDEX.is_file():
        print(f"Using existing frontend build: {DIST_INDEX.parent}")
        return
    print("Building frontend (npm run build)...")
    subprocess.check_call(["npm", "run", "build"], cwd=FRONTEND, shell=True)


def main() -> None:
    ensure_frontend_build()
    python = str(VENV_PYTHON if VENV_PYTHON.is_file() else sys.executable)
    os.chdir(BACKEND)
    print("Website: http://127.0.0.1:8000/")
    os.execv(
        python,
        [
            python,
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8000",
        ],
    )


if __name__ == "__main__":
    main()
