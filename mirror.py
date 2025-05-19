import os
import shutil
import time

fPath = input('Copy files from... > ');
tPath = input('  Copy files to... > ');
print('Bridge started.');

def copy():
    try:
        shutil.copytree(fPath, tPath, dirs_exist_ok=True)
        print("Copied files.")
    except Exception as e:
        errstr = str(e)
        print(f"Failed to copy: {errstr}")

# https://stackoverflow.com/questions/182197/
class d():
    def __init__(self, path):
        self._cached_stamp = 0
        self.filename = path;
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


monkey = d(fPath)
