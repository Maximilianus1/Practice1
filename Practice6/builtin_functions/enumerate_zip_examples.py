a = ["Aba", "Boba", "Aboba"]
b = [85, 90, 78]

for i, name in enumerate(a):
    print(i, name)

for x, s in zip(a,b):
    print(f"{x}: {s}")