import os
import shutil
source = "dir1"
dest = "dir2"
os.makedirs(dest, exist_ok=True)
for file in os.listdir(source):
    if file.endswith(".txt"):
        src = os.path.join(source, file)
        dst = os.path.join(dest, file)
        shutil.copy(src, dst)
        shutil.move(src, dst)