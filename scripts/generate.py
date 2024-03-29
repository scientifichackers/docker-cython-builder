#!/usr/bin/env python
import subprocess
from pathlib import Path
from string import Template

base_dir: Path = Path(__file__).parent.parent.resolve() / "docker"

header = """\
#
# Generated by "scripts/generate.py". 
# Don't edit directly.
#\n
"""
dockerfile = "Dockerfile"
template = Template(header + (base_dir / dockerfile).read_text())

avail = [
    i.strip()
    for i in subprocess.check_output(
        ["pyenv", "install", "-l"], encoding="utf-8"
    ).split()
]

for ver in ["3.5", "3.6", "3.7"]:
    try:
        exact = [i for i in avail if i.startswith(ver)][-1]
    except IndexError:
        raise RuntimeError(f"Python version {ver} not available!")

    ver_dir = base_dir / ver
    ver_dir.mkdir(exist_ok=True)

    df_path = ver_dir / dockerfile
    df_path.write_text(template.safe_substitute(py_version=exact))

    print(df_path)
