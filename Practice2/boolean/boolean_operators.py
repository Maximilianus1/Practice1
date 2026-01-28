x = 4

print(x > 0 and x < 10)

x1 = 2

print(x1 < 3 or x1 > 12)

x2 = 7

print(not(x2 > 4 and x2 < 9))

fruits = ["apple", "banana", "pear"]

print("banana" in fruits)

fruits_n_berries = ["strawberry", "pomelo", "cherry"]

print("pineapple" not in fruits_n_berries)

xf = ["lemon", "banana"]
yf = ["lemon", "banana"]
zf = xf

print(xf is zf)
print(xf is yf)
print(xf == yf)
print(xf is not yf)

x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x3 == y3)
print(x3 is y3)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)