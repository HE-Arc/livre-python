"""Audit simple utilisé comme exemple pour watchdog."""

import time

from watchdog.observers import Observer

import eventhandler


observer = Observer()

observer.schedule(eventhandler.AuditHandler(), path='U:', recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
