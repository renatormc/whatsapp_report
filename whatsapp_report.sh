#!/bin/bash
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
wd="$(pwd)"
cd $SCRIPT_DIR
uv run main.py -w "$wd" "$@"
