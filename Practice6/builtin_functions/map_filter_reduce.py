from functools import reduce

nums = [1, 2, 3, 4, 5]

a = map(lambda x: x**2, nums)
print(a)
print(type(a))
print(list(a))

b = filter(lambda x: x % 2 == 0, nums)
print(b)
print(type(b))
print(list(b))
c = reduce(lambda x, y:x+y,nums)
print(c)
print(type(c))