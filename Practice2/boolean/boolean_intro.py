print(113 > 7)
print(113 == 7)
print(113 < 7)
print(True)
print(False)

a = 1200
b = 32

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
print(bool("Hi"))
print(bool(12))

x = "Yes"
y = 51

print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES! It is!")
else:
  print("NO!")
  
x = 1
print(isinstance(x, int))