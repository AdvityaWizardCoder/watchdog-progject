import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:/Users/ADVITYA/Downloads"

class File_event_handler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"hey , {event.src_path} has been created")
    def on_modified(self, event):
        print(f"hey , {event.src_path} has been modified")
    def on_deleted(self, event):
        print(f"hey , {event.src_path} has been deleted")
    def on_moved(self, event):
        print(f"someone moved {event.src_path} to {event.dest_path}")

event_handler = File_event_handler
observer = Observer()
observer.schedule(event_handler , from_dir , recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
        print("running")
except KeyboardInterrupt:
    print("stopped")

    observer.stop()