# create function with argument
def my_function(fname):
  print(fname + " Refsnes")

# call function with different arguments
my_function("Oleg")
my_function("Misha")
my_function("Linus")

# create function with arguments
def my1_function(fname, lname):
  print(fname + " " + lname)

# call function with two arguments
my1_function("Oleg", "Dobronravov")

# call function with defined argument
def my_function2(country = "Norway"):
  print("I am from", country)

# call function
my_function2("Sweden")
my_function2("India")
my_function2()
my_function2("Brazil")