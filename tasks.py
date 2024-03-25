
from invoke import task
import os


PI = "python"
PIP = "pip"
APP = "./app"


"""
Project task commands: Tasks can be executed using command `invoke <task-name>`
Example: invoke dev  
"""

@task
def start(c, docs=False) -> None:
    c.run(f"{PI} ./main.py")


@task
def test(c, docs=False) -> None:
    c.run(f"{PI} -m unittest discover -s {APP} -p '*_test.py'")


@task
def fmt(c, docs=False) -> None:
    c.run(f"black {APP}")


@task
def lint(c, docs=False) -> None:
    c.run(f"{PI} -m ruff check {APP}")


@task 
def clean(c, docs=False) -> None:
    # recursively remove __pycache__ directories from project
    print("Removing cache files...")
    c.run("find . -type d -name  '__pycache__' -exec rm -r {} +")
    c.run("rm -r .*_cache >& /dev/null")
    c.run("rm -r *.egg-info >& /dev/null")

    build_dir = os.path.join(os.getcwd(), "build")
    if os.path.exists(build_dir):
        c.run(f"rm -r {build_dir}")

