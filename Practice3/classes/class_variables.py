class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tony", 15)
print(p1.age)

p1.age = 26
print(p1.age)

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

p1 = Person("Linch", 32)

del p1.age

print(p1.name)

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Henry")
p2 = Person("ITan")

Person.lastname = "Refsneswqw"

print(p1.lastname)
print(p2.lastname)

class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tor")

p1.age = 25
p1.city = "Oslow"

print(p1.name)
print(p1.age)
print(p1.city)