import shutil
import os

shutil.copy("demofile.txt", "demofile_backup.txt")



if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("File not found.")