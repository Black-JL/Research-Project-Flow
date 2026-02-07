#!/bin/bash
# run_all.sh — Master execution script
# Usage: ./run_all.sh "05_merge.do"   (single step)
#        ./run_all.sh --all           (full pipeline)

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$PROJECT_ROOT/output/logs"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"

# --- CONFIGURE THESE ---
STATA_PATH="/usr/local/stata-mp/stata-mp"  # Update to your Stata path
# STATA_PATH="/Applications/Stata/StataSE.app/Contents/MacOS/stata-se"  # macOS alternative
R_PATH="$(which Rscript 2>/dev/null || echo '/usr/local/bin/Rscript')"
# ------------------------

timestamp() {
    date "+%Y-%m-%d_%H%M%S"
}

run_stata() {
    local script="$1"
    local logfile="$LOG_DIR/$(basename "$script" .do)_$(timestamp).log"
    echo "Running Stata: $script"
    echo "Log: $logfile"
    "$STATA_PATH" -b do "$SCRIPTS_DIR/$script" 2>&1 | tee "$logfile"
    local exit_code=${PIPESTATUS[0]}
    echo "Exit code: $exit_code"
    open "$logfile" 2>/dev/null || true
    return $exit_code
}

run_r() {
    local script="$1"
    local logfile="$LOG_DIR/$(basename "$script" .R)_$(timestamp).log"
    echo "Running R: $script"
    echo "Log: $logfile"
    "$R_PATH" "$SCRIPTS_DIR/$script" 2>&1 | tee "$logfile"
    local exit_code=${PIPESTATUS[0]}
    echo "Exit code: $exit_code"
    open "$logfile" 2>/dev/null || true
    return $exit_code
}

run_script() {
    local script="$1"
    case "$script" in
        *.do)  run_stata "$script" ;;
        *.R)   run_r "$script" ;;
        *)     echo "Unknown file type: $script"; exit 1 ;;
    esac
}

if [[ "${1:-}" == "--all" ]]; then
    echo "=== Running full pipeline ==="
    # Add pipeline steps here in order, e.g.:
    # run_script "01_import.do"
    # run_script "05_merge.do"
    # run_script "10_treatment.do"
    # run_script "15_balance.R"
    echo "=== Pipeline complete ==="
elif [[ -n "${1:-}" ]]; then
    run_script "$1"
else
    echo "Usage: $0 <script_name> | --all"
    exit 1
fi
