import twilio_functions as tw
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import check_in

#############################################################
###database triggers this code when status is changed to "out"
#############################################################
#if tw.check_user_status("out"): tw.checked_out()
#############################################################
#############################################################

# Additional goals: every X days the device uploads the entry/exit logs to cave/park management

def observed_change():
    print("OK")


if __name__ == "__main__":
    path = "./database.csv" #relative path
    observer = Observer()
    observer.schedule(observed_change, path, recursive=True)
    print("1")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

print("2")
