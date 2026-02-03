a = 4
b = 2
if a > b: print("a is greater than b")

a1 = 1
b1 = 31
print("A") if a1 > b1 else print("B")

a2 = 15
b2 = 12
bigger = a2 if a2 > b2 else b2
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

x = 12
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
