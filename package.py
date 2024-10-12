#!/Users/lucamarchetti/anaconda3/bin/python3

"""
PACKAGE.Py
by Luca Marchetti

This small python script allows to automatically create a 
python package, with the correct tree structure.
"""

import os
import sys
import shutil
import pathlib


class Text:
    @staticmethod
    def make_visible(text: str) -> str:
        return f"\033[1m\033[38;5;10m{text}\033[0m"

    @staticmethod
    def make_error(text: str) -> str:
        return f"\033[1m\033[38;5;160m{text}\033[0m"


class Tree:
    @staticmethod
    def make_dirs() -> None:
        os.mkdir(dir_path)
        os.mkdir(dir_path.joinpath("src"))
        os.mkdir(dir_path.joinpath("tests"))

    @staticmethod
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

    @staticmethod
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
                pathlib.Path(
                    "/Users/lucamarchetti/Python/useful/package/data/ignore.txt"
                ),
                dir_path.joinpath(".gitignore"),
            )


# no project name
if len(sys.argv) < 2:
    print("[package.py]: " + Text.make_error("ERROR") + " - Package name not inserted")
    print(f"[package.py]: Use 'package.py -h' for help.")
    sys.exit()

# help
if sys.argv[1] == "-h":
    print("usage: package.py [package name] [option] \n")
    print(
        "package is a small python script that makes it possible to setup a python package \n"
    )
    print("options:")
    print("-s   Simple project: only necessary files")
    print("-g   Git project: complete project with .gitignore")
    sys.exit()

# start
print(f"You are about to create a package named {Text.make_visible(sys.argv[1])}.")
proceed = input("Are you sure you want to proceed? (Y/n) ")
if proceed:
    print("Process terminated")
    sys.exit()

if pathlib.Path.exists((dir_path := pathlib.Path(f"./{sys.argv[1]}"))):
    print("A package with the same name already exists!")
    sys.exit()

# make directories
try:
    Tree.make_dirs()
    Tree.make_necessary()
    flag = sys.argv[2] if len(sys.argv) > 2 else None
    Tree.make_optional(flag)

    print("Package structure completed!")
except Exception as exc:
    print(exc)
    shutil.rmtree(dir_path)
    sys.exit()
