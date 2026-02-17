def myfunc(n):
  return lambda a : a * n

mymultiplier = myfunc(23)

print(mymultiplier(11))

def myfunc1(n):
  return lambda a : a * n

mydoubler = myfunc1(2)
mytripler = myfunc1(3)

print(mydoubler(12))
print(mytripler(13))