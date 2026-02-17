#create class
class MyClass:
  x = 5

print(MyClass)
#create object
p1 = MyClass()
print(p1.x)
#delete object
del p1
#create objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
#create class with placeholder
class Person:
  pass