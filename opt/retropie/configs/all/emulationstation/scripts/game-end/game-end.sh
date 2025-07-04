#! /bin/bash
/opt/retropie/scripts/stop-inactivity_monitor.sh
rclone sync /home/pi/RetroPie/roms gdrive-arcade:/roms -u --log-file=/home/pi/log/roms_game-end.log --log-level INFO
