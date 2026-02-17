# create class Person
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# create object
p1 = Person("Emil", 36)

# access attributes
print(p1.name)
print(p1.age)


# create class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# create object
p1 = Person("Tony", 15)

# print age
print(p1.age)

# change age
p1.age = 26
print(p1.age)


# create class
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

# create object
car1 = Car("Toyota", "Corolla")

#get attributes
print(car1.brand)
print(car1.model)


# create Person object
p1 = Person("Linch", 32)

# delete attribute
del p1.age

# print attribute
print(p1.name)


# class with class variable
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

# create objects
p1 = Person("Henry")
p2 = Person("ITan")

# set class variable
Person.lastname = "Refsneswqw"

#get variable od class
print(p1.lastname)
print(p2.lastname)


#create class
class Person:
  def __init__(self, name):
    self.name = name

# create object
p1 = Person("Tor")

# add attributes
p1.age = 25
p1.city = "Oslow"

# print мфvariables
print(p1.name)
print(p1.age)
print(p1.city)
