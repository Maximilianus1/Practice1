# function with *args (like a list)
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
# call function
my_function("Hi", "Emil", "Tobias", "Linus")
# function to sum numbers
def my_function1(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
# call function
print(my_function1(12, 122, 31))
print(my_function1(10, 203, 30, 40))
print(my_function1(5))

# function to find max number
def my_function2(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num
# call function
print(my_function2(3, 721, 23, 9, 1))
# function with **kwargs
def my_function3(**kid):
  print("His last name is " + kid["lname"])

# call function
my_function3(fname = "Tobias", lname = "Refewe")
# function with **kwargs (dictionary)
def my_function4(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

# call function
my_function4(name = "Tobias", age = 32, city = "Bergen")
# function with normal argument and **kwargs
def my_function5(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

# call function
my_function5("ev43", age = 12, city = "Astana", hobby = "coding")
# function with normal arg, *args and **kwargs
def my_function6(title, *args, **kwargs):
  print("Titlo :", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

# call function
my_function6("User Info", "Jack", "Tobi", age = 32, city = "Oslo")


# unpack list with *
def my_function7(a, b, c):
  return a + b + c
numbers = [1, 2, 3]

# unpack list into arguments
result = my_function7(*numbers)
print(result)
# unpack dictionary with **
def my_function8(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}

# unpack dictionary into arguments
my_function8(**person)
