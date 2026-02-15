from pathlib import Path


def find_root():
    """
    Used as a tool to find the root directory of the project, used for utility functions
    """
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / ".project_root").exists():
            return parent
    raise RuntimeError("Root not found")
