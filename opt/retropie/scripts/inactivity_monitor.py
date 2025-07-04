#! /usr/bin/env python3
"""
inactivity_monitor.py – exits RetroArch after 15 min of controller silence
"""

import os, time, signal, subprocess, fcntl
from evdev import InputDevice, list_devices, ecodes

IDLE_TIMEOUT = 60*15      # 15 min
POLL_INTERVAL = 1       # seconds

def make_nonblocking(device):
    """Force device.fd into O_NONBLOCK – works on all kernels & evdev versions."""
    flags = fcntl.fcntl(device.fd, fcntl.F_GETFL)
    fcntl.fcntl(device.fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

def all_event_devices():
    """Return every input device that emits keys or axes."""
    devs = []
    for path in list_devices():
        d = InputDevice(path)
        try:
            d.grab()                     # optional – ignore error if you like
        except OSError:
            pass
        make_nonblocking(d)              # our rock-solid helper
        caps = d.capabilities()
        if ecodes.EV_KEY in caps or ecodes.EV_ABS in caps:
            devs.append(d)
    return devs

def main():
    last_activity = time.time()
    devs = all_event_devices()

    while True:
        now = time.time()

        for d in devs:
            try:
                for e in d.read():
                    if e.type in (ecodes.EV_KEY, ecodes.EV_ABS):
                        last_activity = now
            except BlockingIOError:
                pass       # nothing to read – exactly what we expect

        if now - last_activity >= IDLE_TIMEOUT:
            subprocess.run(["sudo", "pkill", "-SIGTERM", "retroarch"])
            break

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
