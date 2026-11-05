"""Build the site navigation from every Markdown page in the wiki."""

import re
from pathlib import Path

SKIP_DIRS = {"scripts", "stylesheets"}
DATE_IN_NAME = re.compile(r"_(\d{2})(\d{2})(\d{4})\.md$")


def _first_heading(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def _note_title(path: Path) -> str:
    number = path.stem.split("_")[0]
    match = DATE_IN_NAME.search(path.name)
    if match:
        day, month, year = match.groups()
        return f"{number} · {day}/{month}/{year}"
    return path.stem


def _section_title(folder: Path) -> str:
    readme = folder / "README.md"
    heading = _first_heading(readme) if readme.exists() else None
    return heading or folder.name.replace("_", " ").capitalize()


def _build(folder: Path, docs_dir: Path) -> list:
    items = []
    readme = folder / "README.md"
    if readme.exists():
        items.append({"Visão geral": readme.relative_to(docs_dir).as_posix()})
    for child in sorted(folder.iterdir(), key=lambda p: p.name):
        if child.name.startswith(".") or child.name in SKIP_DIRS or child.name == "README.md":
            continue
        if child.is_dir():
            sub = _build(child, docs_dir)
            if sub:
                items.append({_section_title(child): sub})
        elif child.suffix == ".md":
            items.append({_note_title(child): child.relative_to(docs_dir).as_posix()})
    return items


def on_files(files, config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    home = [{"Visão geral": "README.md"}]
    for page in sorted(docs_dir.glob("*.md"), key=lambda p: p.name):
        if page.name != "README.md":
            home.append({_first_heading(page) or page.stem: page.relative_to(docs_dir).as_posix()})

    sections = [{"Início": home}]
    for folder in sorted(docs_dir.iterdir(), key=lambda p: p.name):
        if not folder.is_dir() or folder.name.startswith(".") or folder.name in SKIP_DIRS:
            continue
        items = _build(folder, docs_dir)
        if items:
            sections.append({_section_title(folder): items})
    config["nav"] = sections
    return files
