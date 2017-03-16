"""Exemple d'audit."""

import time

import eventHandler
from watchdog.observers import Observer

observer = Observer()

observer.schedule(eventHandler.AuditHandler(), path='U:', recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
