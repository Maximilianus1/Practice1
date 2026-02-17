# create class that inherits from other but overides what method does
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def printname(self):
    print(self.firstname, self.lastname, self.graduationyear)

x = Student("Maxim", "Olegov", 2028)
x.printname()
