from pathlib import Path


def find_root():
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / ".project_root").exists():
            return parent
    raise RuntimeError("Root not found")
