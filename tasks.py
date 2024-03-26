from invoke import task
import os


PI = "python"
PIP = "pip"
ROOT = os.getcwd()
APP = os.path.join(ROOT, "app")
MAIN = os.path.join(ROOT, "main.py")
BUILD_DIR = os.path.join(ROOT, "build")


"""
Project task commands: Tasks can be executed using command `invoke <task-name>`
Example: invoke dev  
"""

@task
def start(c, docs=False) -> None:
    c.run(f"{PI} {MAIN}")


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
def build(c, docs=False) -> None:
    c.run(f"pyinstaller --onefile --specpath={BUILD_DIR} {MAIN}")
    

@task 
def clean(c, docs=False) -> None:
    # recursively remove __pycache__ directories from project
    print("Removing cache files...")
    c.run("find . -type d -name  '__pycache__' -exec rm -r {} +")

    dist_dir = os.path.join(os.getcwd(), "dist")        
    if os.path.exists(dist_dir):
        c.run(f"rm -rf {dist_dir}")

    if os.path.exists(BUILD_DIR):
        c.run(f"rm -r {BUILD_DIR}")

