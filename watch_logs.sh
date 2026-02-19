#!/bin/bash
# watch_logs.sh - Monitor execution log files in a new terminal window
#
# Usage:
#   ./watch_logs.sh <logfile>           # Watch a specific log file
#   ./watch_logs.sh                     # Watch all logs in output/logs/
#   ./watch_logs.sh --latest            # Watch the most recently modified log
#
# Examples:
#   ./watch_logs.sh output/logs/05_merge_20260218.log
#   ./watch_logs.sh --latest

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${SCRIPT_DIR}/output/logs"

# Create log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Function to open a new terminal window with tail -f
watch_log() {
    local logfile="$1"

    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS - use osascript to open new Terminal window
        osascript <<EOF
tell application "Terminal"
    activate
    do script "echo 'Watching: $logfile' && echo '---' && tail -f '$logfile'"
end tell
EOF
    else
        # Linux - try common terminal emulators
        if command -v gnome-terminal &> /dev/null; then
            gnome-terminal -- bash -c "echo 'Watching: $logfile'; echo '---'; tail -f '$logfile'; exec bash"
        elif command -v xterm &> /dev/null; then
            xterm -e "tail -f '$logfile'" &
        else
            echo "No supported terminal emulator found. Use: tail -f '$logfile'"
        fi
    fi
}

# Function to find the latest log file
find_latest_log() {
    find "$LOG_DIR" -name "*.log" -type f -print0 2>/dev/null | \
        xargs -0 ls -t 2>/dev/null | head -1
}

# Main logic
if [[ $# -eq 0 ]]; then
    # No arguments - watch all logs in output/logs/
    echo "Watching all logs in $LOG_DIR..."

    if [[ "$OSTYPE" == "darwin"* ]]; then
        osascript <<EOF
tell application "Terminal"
    activate
    do script "echo 'Watching all logs in $LOG_DIR' && echo '---' && tail -f '$LOG_DIR'/*.log 2>/dev/null || echo 'No log files found yet. Waiting...'"
end tell
EOF
    else
        echo "Use: tail -f $LOG_DIR/*.log"
    fi

elif [[ "$1" == "--latest" ]]; then
    # Find and watch the most recent log
    latest=$(find_latest_log)

    if [[ -z "$latest" ]]; then
        echo "No log files found in $LOG_DIR"
        echo "Creating placeholder and waiting..."
        touch "$LOG_DIR/output.log"
        latest="$LOG_DIR/output.log"
    fi

    echo "Watching latest log: $latest"
    watch_log "$latest"

elif [[ -f "$1" ]]; then
    # Watch specific file
    watch_log "$1"

else
    # Assume it's a filename to create/watch in LOG_DIR
    logfile="$LOG_DIR/$1"
    touch "$logfile"
    echo "Created and watching: $logfile"
    watch_log "$logfile"
fi

echo ""
echo "Log watcher started. To stop, close the Terminal window or press Ctrl+C in it."
