"""Audit de fichier musique utilisé comme exemple pour watchdog."""

import time

import eventHandler
from watchdog.observers import Observer

observer = Observer()

handler = eventHandler.AuditHandlerMusic(patterns=["*.mp3","*.wav","*.flac"])

observer.schedule(handler, path='U:', recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
