#!/Users/lucamarchetti/anaconda3/bin/python3

"""
PACKAGE.Py
by Luca Marchetti

This small python script allows to automatically create a 
python package, with the correct tree structure.

To use:
1. Write `package.py package_name`
2. Add a flag:
    • `-s` for simple projects
    ∙ `-g` for git projects
3. Execute the command
"""

import os
import sys
import shutil
import pathlib


def make_visible(text: str) -> str:
    return f"\033[1m\033[38;5;10m{text}\033[0m"


def make_dirs() -> None:
    os.mkdir(dir_path)
    os.mkdir(dir_path.joinpath("src"))
    os.mkdir(dir_path.joinpath("tests"))


def make_necessary() -> None:
    # make __init__.py
    with open(dir_path.joinpath("src/__init__.py"), "w") as _:
        pass
    with open(dir_path.joinpath("tests/__init__.py"), "w") as _:
        pass

    # make toml
    shutil.copyfile(
        pathlib.Path("/Users/lucamarchetti/Python/useful/package/data/toml.txt"),
        dir_path.joinpath("pyproject.toml"),
    )


def make_optional(flag: str = None) -> None:
    if flag == "-s":
        return

    # make readme
    with open(dir_path.joinpath("README.MD"), "w") as _:
        pass

    # make license
    shutil.copyfile(
        pathlib.Path("/Users/lucamarchetti/Python/useful/package/data/mit.txt"),
        dir_path.joinpath("LICENSE"),
    )

    if flag == "-g":
        # make gitignore
        shutil.copyfile(
            pathlib.Path("/Users/lucamarchetti/Python/useful/package/data/ignore.txt"),
            dir_path.joinpath(".gitignore"),
        )


print(f"You are about to create a package named {make_visible(sys.argv[1])}.")
proceed = input("Are you sure you want to proceed? (Y/n) ")
if proceed:
    print("Process terminated")
    sys.exit()

if pathlib.Path.exists((dir_path := pathlib.Path(f"./{sys.argv[1]}"))):
    print("A package with the same name already exists!")
    sys.exit()

# make directories
try:
    make_dirs()
    make_necessary()
    flag = sys.argv[2] if len(sys.argv) > 2 else None
    make_optional(flag)

    print("Package structure completed!")
except Exception as exc:
    print(exc)
    shutil.rmtree(dir_path)
    sys.exit()
