# first class
class Father:
  def skill_father(self):
    print("can drive")

# second class
class Mother:
  def skill_mother(self):
    print("can cook")

# child class inherits from Father and Mother
class Child(Father, Mother):
  def skill_child(self):
    print("can code")

# create object
c = Child()

# call methods from both parents
c.skill_father()
c.skill_mother()

# call child's own method
c.skill_child()
