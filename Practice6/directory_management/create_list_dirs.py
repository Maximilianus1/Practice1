import os

os.makedirs("dira/sub1/sub2", exist_ok=True)
print("Dirs created.")

for item in os.listdir("dira"):
    print(item)