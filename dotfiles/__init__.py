import sys
import re
import os
import argparse
import shutil


fpath = os.path.abspath(__file__)
METADIR = os.path.dirname(os.path.dirname(fpath))
CWD = os.path.abspath(os.getcwd())

def populate_metafiles():
    """Copy all metafiles to current working directory."""
    cwd = os.path.abspath(os.getcwd())
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
        "workflow.yml"
    ]
    for item in files:
        full = os.path.join(METADIR, item)
        shutil.copy(full, cwd)



def main(args=None):
    """Parse command line arguments."""
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(sys.argv[0], description="populate meta files")
    subparsers = parser.add_subparsers()
    populate = subparsers.add_parser("populate")
    populate.set_defaults(func=populate_metafiles)
    parser.add_argument(
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
    mit = re.comile(r"^[mM][iI][tT]$")
    apache = re.compile(r"^[aA][pP][aA][cC][hH][eE]")
    bsd = re.compile(r"^[Bb][Ss][Dd]\d?$")
    isc = re.compile(r"^[iI][sS][cC]$")
    license_dir = os.path.join(METADIR, "text_licenses")
    if namespace.license:
        name = namespace.license
        if gpl.match(name):
            lic = os.path.join(license_dir, "gpl_3.0.txt")
            shutil.copy(lic, CWD)
        elif lgpl.match(name):
            lic = os.path.join(license_dir, "LGPL3.txt")
            shutil.copy(lic, CWD)
        elif mit.match(name):
            lic = os.path.join(license_dir, "MIT.txt")
            shutil.copy(lic, CWD)
        elif apache.match(name):
            lic = os.path.join(license_dir, "Apache2.txt")
            shutil.copy(lic, CWD)
        elif bsd.match(name):
            lic = os.path.join(license_dir, "BSD3.txt")
            shutil.copy(lic, CWD)
        elif isc.match(name):
            lic = os.path.join(license_dir, "ISC.txt")
            shutil.copy(lic, CWD)


if __name__ == '__main__':
    main()
