f = open("demofile.txt")
print(f.read())
f.close()
with open("demofile.txt") as f1:
  print(f1.readline())
  print(f1.readline())