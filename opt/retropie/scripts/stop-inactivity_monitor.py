#! /bin/bash
if [[ -f /tmp/inactivity_monitor.pid ]]; then
    kill "$(cat /tmp/inactivity_monitor.pid)" 2>/dev/null
    rm /tmp/inactivity_monitor.pid
fi
