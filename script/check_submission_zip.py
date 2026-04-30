#!/usr/bin/env python3
"""Check that submission.zip contains exactly the required files under section1/ and section2/ at the zip root.

If there's any mismatch the script prints "content or hierarchy mismatch" followed by details and exits with code 1.
"""

from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile
import sys
import argparse

EXPECTED_SECTION1 = [
    "section1/TitleCountSpark.py",
    "section1/TopTitleStatisticsSpark.py",
    "section1/OrphanPagesSpark.py",
    "section1/TopPopularLinksSpark.py",
    "section1/PopularityLeagueSpark.py",
]

EXPECTED_SECTION2 = [
    "section2/PartA.py",
    "section2/PartB.py",
    "section2/PartC.py",
    "section2/PartD.py",
    "section2/PartE.py",
    "section2/PartF.py",
]

# Java-based layout for section2: pom.xml + java sources
EXPECTED_SECTION2_JAVA = [
    "section2/pom.xml",
    "section2/src/main/java/PartA.java",
    "section2/src/main/java/PartB.java",
    "section2/src/main/java/PartC.java",
    "section2/src/main/java/PartD.java",
    "section2/src/main/java/PartE.java",
    "section2/src/main/java/PartF.java",
]

EXPECTED_FILES = set(EXPECTED_SECTION1 + EXPECTED_SECTION2)


def normalize(name: str) -> str:
    # Normalize path separators and strip any leading ./
    n = name.replace("\\", "/")
    if n.startswith("./"):
        n = n[2:]
    return n


def main() -> int:
    parser = argparse.ArgumentParser(description="Check zip file structure for the grader")
    parser.add_argument("-f", "--zip-file", help="Path to zip file to check (default: <repo root>/submission.zip)", default=None)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    if args.zip_file:
        zip_path = Path(args.zip_file).expanduser()
    else:
        zip_path = root / "submission.zip"

    if not zip_path.is_file():
        print(f"submission.zip not found at {zip_path}")
        return 2

    with ZipFile(zip_path) as zf:
        all_names = [normalize(n) for n in zf.namelist() if not n.endswith("/")]

    found = set(all_names)

    # Disallow top-level submission/ parent
    if any(p.startswith("submission/") for p in found):
        print("content or hierarchy mismatch")
        print("Parent directory 'submission/' is not allowed; files must be at the archive root under section1/ and section2/.")
        return 1

    # Top-level components must be only section1 and section2
    top_levels = set(p.split('/')[0] for p in found)
    extra_top = {t for t in top_levels if t not in {"section1", "section2"}}
    if extra_top:
        print("content or hierarchy mismatch")
        print("Additional top-level directories/files are not allowed:")
        for t in sorted(extra_top):
            print(f"  - {t}")
        return 1

    # Validate section1: no subdirectories, expected files must exist
    section1_found = {p for p in found if p.startswith("section1/")}
    section1_files = {p for p in section1_found}
    missing1 = set(EXPECTED_SECTION1) - section1_files
    # detect unexpected subdirectories in section1 (depth > 2)
    bad_subdirs = [p for p in section1_found if len(p.split('/')) > 2]
    if bad_subdirs:
        print("content or hierarchy mismatch")
        print("Unexpected subdirectories under section1/ are not allowed:")
        for p in sorted(bad_subdirs):
            print(f"  - {p}")
        return 1

    # Validate section2: accept either python or java layout
    section2_found = {p for p in found if p.startswith("section2/")}
    py_ok = set(EXPECTED_SECTION2).issubset(section2_found)
    java_ok = set(EXPECTED_SECTION2_JAVA).issubset(section2_found)

    if not py_ok and not java_ok:
        print("content or hierarchy mismatch")
        print("Section2 files missing: expected either Python files or Java layout (pom.xml + src/main/java/...)")
        missing_py = set(EXPECTED_SECTION2) - section2_found
        missing_java = set(EXPECTED_SECTION2_JAVA) - section2_found
        if missing_py:
            print("Missing Python files for section2:")
            for p in sorted(missing_py):
                print(f"  - {p}")
        if missing_java:
            print("Missing Java files for section2:")
            for p in sorted(missing_java):
                print(f"  - {p}")
        return 1

    # Check for unexpected subdirectories under section2 depending on layout
    if py_ok:
        # For python layout, all section2 files should be at depth 2 (section2/<file>)
        bad = [p for p in section2_found if len(p.split('/')) > 2]
        if bad:
            print("content or hierarchy mismatch")
            print("Unexpected subdirectories under section2/ for Python layout are not allowed:")
            for p in sorted(bad):
                print(f"  - {p}")
            return 1
        used_section2 = set(EXPECTED_SECTION2)
    else:
        # Java layout: allow pom.xml and src/main/java/...; disallow other dirs under section2
        # Allow files under section2/src/main/java/... (any depth) but unexpected other second-level names are not allowed
        second_level = {p.split('/')[1] for p in section2_found if len(p.split('/')) > 1}
        allowed_second = {"pom.xml", "src"}
        extras = {s for s in second_level if s not in allowed_second}
        if extras:
            print("content or hierarchy mismatch")
            print("Unexpected directories under section2/ for Java layout:")
            for s in sorted(extras):
                print(f"  - {s}")
            return 1
        used_section2 = set(EXPECTED_SECTION2_JAVA)

    # Now check for missing expected files
    missing = set(EXPECTED_SECTION1) - section1_files
    missing |= used_section2 - section2_found
    if missing:
        print("content or hierarchy mismatch")
        print("Missing files:")
        for p in sorted(missing):
            print(f"  - {p}")
        return 1

    # Additional files under section1/ or section2/ are allowed but should warn
    allowed_union = set(EXPECTED_SECTION1) | set(EXPECTED_SECTION2) | set(EXPECTED_SECTION2_JAVA)
    extras = {p for p in found if p.startswith("section1/") or p.startswith("section2/")}
    unexpected_files = extras - allowed_union
    if unexpected_files:
        print("warning: additional files present:")
        for p in sorted(unexpected_files):
            print(f"  - {p}")

    print("submission.zip structure and contents are correct.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
