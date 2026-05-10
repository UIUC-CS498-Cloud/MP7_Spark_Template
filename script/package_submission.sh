#!/bin/bash

# Author: Edward Ira Snodgrass 

# ─────────────────────────────────────────────
# package_submission.sh
# Packages section1/section2 Python files or
# Java src + pom.xml into a submission.zip
# Usage: ./package_submission.sh [--python|--java]
# Note: This script is only tested on Max and Linux
# ─────────────────────────────────────────────

# --- Argument Handling ---
MODE=""

if [ $# -eq 0 ]; then
    echo "⚠️  Warning: No argument provided. Defaulting to python for section2."
    MODE="python"
elif [ $# -gt 1 ]; then
    echo "❌ Error: Too many arguments. Usage: ./package_submission.sh [--python|--java]"
    exit 1
elif [ "$1" == "--python" ]; then
    echo "Using python for section2."
    MODE="python"
elif [ "$1" == "--java" ]; then
    echo "Using java for section2."
    MODE="java"
else
    echo "❌ Error: Unknown argument '$1'. Use --python or --java."
    exit 1
fi

# --- Setup ---
SUBMISSION_DIR="submission"

# Clean up any previous submission directory or zip
rm -rf "$SUBMISSION_DIR" submission.zip

mkdir -p "$SUBMISSION_DIR/section1"
mkdir -p "$SUBMISSION_DIR/section2"

# Find and copy all .py files from section1 recursively (flat into section1/)
find section1 -name "*.py" | while read f; do
    cp "$f" "$SUBMISSION_DIR/section1/"
done

# ─────────────────────────────────────────────
# PYTHON MODE
# ─────────────────────────────────────────────
if [ "$MODE" == "python" ]; then
    echo "📦 Packaging Python submission..."

    # Find and copy all .py files from section2 recursively (flat into section2/)
    find section2 -name "*.py" | while read f; do
        cp "$f" "$SUBMISSION_DIR/section2/"
    done

    echo "✅ Copied Python files."

# ─────────────────────────────────────────────
# JAVA MODE
# ─────────────────────────────────────────────
elif [ "$MODE" == "java" ]; then
    echo "📦 Packaging Java submission..."

    # Validate required Java files exist
    if [ ! -f "section2/java/pom.xml" ]; then
        echo "❌ Error: section2/java/pom.xml not found."
        rm -rf "$SUBMISSION_DIR"
        exit 1
    fi

    if [ ! -d "section2/java/src" ]; then
        echo "❌ Error: section2/java/src directory not found."
        rm -rf "$SUBMISSION_DIR"
        exit 1
    fi

    cp "section2/java/pom.xml" "$SUBMISSION_DIR/section2/"
    cp -r "section2/java/src" "$SUBMISSION_DIR/section2/src/"

    echo "✅ Copied pom.xml and src/."
fi

# --- Zip ---
(cd "$SUBMISSION_DIR" && zip -r ../submission.zip .)

# --- Cleanup ---
rm -rf "$SUBMISSION_DIR"

echo ""
echo "🎉 Done! Created submission.zip"
echo ""
