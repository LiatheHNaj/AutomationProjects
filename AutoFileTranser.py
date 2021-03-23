from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json

class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" +filename
            os.rename(src, new_destination)


folder_to_track = '/Users/liathe.najdawi/Desktop/TrackingFolder'
folder_destination = '/Users/liathe.najdawi/Desktop/DestinationFolder'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
        observer.stop()
observer.join()
