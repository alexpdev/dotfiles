"""Shortcut functions."""

import argparse
import os
import re
import shutil
import sys

parent = os.path.dirname(os.path.abspath(__file__))
METADIR = os.path.join(parent, "metafiles")
CWD = os.path.abspath(os.getcwd())
LICENSEDIR = os.path.join(parent, "text_licenses")


def populate_metafiles():
    """Copy all metafiles to current working directory."""
    files = [
        ".prospector.yml",
        ".markdownlint.json",
        ".prettierrc",
        ".editorconfig",
        ".gitignore",
        ".gitattributes",
        ".pylintrc",
        ".setup.cfg",
        ".vscodeignore",
        "CHANGELOG.md",
        "Makefile",
        "Manifest.in",
        "pyproject.toml",
        "README.md",
        "settings.json",
        "workflow.yml",
    ]
    for item in files:
        full = os.path.join(METADIR, item)
        shutil.copy(full, CWD)


def main():
    """Parse command line arguments."""
    args = sys.argv[1:]
    parser = argparse.ArgumentParser(
        sys.argv[0], description="populate meta files"
    )
    subparsers = parser.add_subparsers()
    populate = subparsers.add_parser("populate")
    populate.set_defaults(func=populate_metafiles)
    populate.add_argument(
        "-l",
        "--license",
        help="select license",
        metavar="<license>",
        dest="license",
        action="store",
    )
    namespace = parser.parse_args(args)
    namespace.func()
    gpl = re.compile(r"^[gG][pP][lL]$")
    lgpl = re.compile(r"^[lL][gG][pP][lL]$")
    mit = re.compile(r"^[mM][iI][tT]$")
    apache = re.compile(r"^[aA][pP][aA][cC][hH][eE]")
    bsd = re.compile(r"^[Bb][Ss][Dd]\d?$")
    isc = re.compile(r"^[iI][sS][cC]$")
    if namespace.license:
        name = namespace.license
        if gpl.match(name):
            lic = os.path.join(LICENSEDIR, "gpl_3.0.txt")
            shutil.copy(lic, CWD)
        elif lgpl.match(name):
            lic = os.path.join(LICENSEDIR, "LGPL3.txt")
            shutil.copy(lic, CWD)
        elif mit.match(name):
            lic = os.path.join(LICENSEDIR, "MIT.txt")
            shutil.copy(lic, CWD)
        elif apache.match(name):
            lic = os.path.join(LICENSEDIR, "Apache2.txt")
            shutil.copy(lic, CWD)
        elif bsd.match(name):
            lic = os.path.join(LICENSEDIR, "BSD3.txt")
            shutil.copy(lic, CWD)
        elif isc.match(name):
            lic = os.path.join(LICENSEDIR, "ISC.txt")
            shutil.copy(lic, CWD)
