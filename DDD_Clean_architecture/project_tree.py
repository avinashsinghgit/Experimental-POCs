from rich.tree import Tree
from rich import print
from pathlib import Path

# Define patterns or folder names to exclude
EXCLUDE_DIRS = {"__pycache__", "tests", ".git", ".venv"}
EXCLUDE_FILES_EXT = {".pyc", ".pyo", ".log", ".toml", ".lock"}
EXCLUDE_FILE_NAMES = {"pytest.ini", ".DS_Store", "project_tree.py"}

def build_tree(directory: Path, tree: Tree):
    """Recursively build the tree structure with exclusions."""
    for path in sorted(directory.iterdir()):
        name = path.name

        # Skip hidden files/folders and unwanted ones
        if name.startswith(".") and name not in {".env"}:
            continue
        if path.is_dir() and name in EXCLUDE_DIRS:
            continue
        if path.is_file() and (path.suffix in EXCLUDE_FILES_EXT or name in EXCLUDE_FILE_NAMES):
            continue

        # Build subtrees recursively
        if path.is_dir():
            branch = tree.add(f"[bold blue]{name}/[/]")
            build_tree(path, branch)
        else:
            tree.add(f"[green]{name}[/]")

def print_project_tree(start_path="."):
    """Prints the directory tree starting from start_path."""
    root_dir = Path(start_path)
    tree = Tree(f":open_file_folder: [bold magenta]{root_dir.resolve().name}[/]")
    build_tree(root_dir, tree)
    print(tree)


if __name__ == "__main__":
    print_project_tree("/")
