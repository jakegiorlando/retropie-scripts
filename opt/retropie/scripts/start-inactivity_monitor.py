#! /bin/bash
/opt/retropie/scripts/inactivity_monitor.py &
echo $! > /tmp/inactivity_monitor.pid        # remember PID
