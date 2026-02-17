def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hi", "Emil", "Tobias", "Linus")


def my_function1(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function1(12, 122, 31))
print(my_function1(10, 203, 30, 40))
print(my_function1(5))

def my_function2(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function2(3, 721, 23, 9, 1))

def my_function3(**kid):
  print("His last name is " + kid["lname"])

my_function3(fname = "Tobias", lname = "Refewe")

def my_function4(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function4(name = "Tobias", age = 32, city = "Bergen")

def my_function5(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function5("ev43", age = 12, city = "Astana", hobby = "coding")

def my_function6(title, *args, **kwargs):
  print("Titlo :", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function6("User Info", "Jack", "Tobi", age = 32, city = "Oslo")

def my_function7(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function7(*numbers)
print(result)

def my_function8(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function8(**person)