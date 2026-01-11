from __future__ import annotations

import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient


def find_repo_root(start: Path) -> Path:
    cur = start.resolve()
    for p in [cur] + list(cur.parents):
        if (p / ".git").exists() or (p / "requirements.txt").exists() or (p / "README.md").exists():
            return p
    return cur  # fallback


def pick_notebook_path(root: Path, name: str) -> Path:
    candidates = [
        root / "notebooks" / name,
        root / name,
    ]
    for c in candidates:
        if c.exists():
            return c
    raise FileNotFoundError(f"Notebook introuvable: {name}. Cherché: {candidates}")


def execute_notebook(nb_path: Path, workdir: Path, timeout: int = 1800) -> None:
    nb_path = nb_path.resolve()

    try:
        display = nb_path.relative_to(workdir)
    except ValueError:
        display = nb_path

    print(f"\n=== Running: {display} ===")

    nb = nbformat.read(nb_path, as_version=4)
    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name="python3",
        resources={"metadata": {"path": str(workdir)}},  # <-- C'est ça qui fixe le CWD côté exécution
    )
    client.execute()

def main() -> int:
    repo_root = find_repo_root(Path(__file__).parent)
    print(f"Repo root: {repo_root}")

    pipeline = ["Main.ipynb", "Merger.ipynb", "Models.ipynb"]

    try:
        for nb_name in pipeline:
            nb_path = pick_notebook_path(repo_root, nb_name)
            execute_notebook(nb_path, workdir=repo_root, timeout=1800)
    except Exception as e:
        print("\n❌ Pipeline failed.")
        print(f"Error: {type(e).__name__}: {e}")
        return 1

    print("\n✅ Pipeline completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
