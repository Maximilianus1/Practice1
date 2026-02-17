# create class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# create object
p1 = Person("Oleg", 21)

# print attributes
print(p1.name)
print(p1.age)


#create class with placeholder
class Person:
  pass

#create object
p1 = Person()

# add attributes
p1.name = "Toguluk"
p1.age = 25

# print attributes
print(p1.name)
print(p1.age)


#cret class with defined age
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

# create objects
p1 = Person("Emil")
p2 = Person("Titus", 22)

# print values
print(p1.name, p1.age)
print(p2.name, p2.age)


# create Person class with multiple attributes
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

# create object
p1 = Person("Linch", 32, "Oslo", "Norway")

# print
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
