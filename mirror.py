import os
import shutil
import time

fPath = input('Copy files from... > ');
tPath = input('  Copy files to... > ');
print('Bridge started.');

def copy():
    shutil.copytree(fPath, tPath)

# https://stackoverflow.com/questions/182197/
class d():
    def __init__(self, path):
        self._cached_stamp = 0
        self.filename = path;
        self.cb = callback;
        while True:
            self.check()
            time.sleep(5)
            

    def check(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed, so do something...
            print('Files updated, copying...');
            copy();


monkey = Monkey(fPath)
