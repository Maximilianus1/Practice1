#create list with modified nums from other list using lambda in map
numbers = [1, 2, 3, 4, 5]
powered = list(map(lambda x: x ** 2, numbers))
print(powered)
