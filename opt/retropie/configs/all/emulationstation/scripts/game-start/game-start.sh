#! /bin/bash
rclone sync gdrive-arcade:/roms /home/pi/RetroPie/roms --log-file=/home/pi/log/roms_game-start.log --log-level INFO
/opt/retropie/scripts/start-inactivity_monitor.sh
