def my_function(fname):
  print(fname + " Refsnes")

my_function("Oleg")
my_function("Misha")
my_function("Linus")

def my1_function(fname, lname):
  print(fname + " " + lname)

my1_function("Oleg", "Dobronravov")

def my_function2(country = "Norway"):
  print("I am from", country)

my_function2("Sweden")
my_function2("India")
my_function2()
my_function2("Brazil")