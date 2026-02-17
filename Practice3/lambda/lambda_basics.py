# function that returns lambda func
def myfunc(n):
  return lambda a : a * n

# create function
mymultiplier = myfunc(23)
# call lambda function
print(mymultiplier(11))


# function that returns lambda func
def myfunc1(n):
  return lambda a : a * n
# create doubler and tripler
mydoubler = myfunc1(2)
mytripler = myfunc1(3)

# call lambda functions
print(mydoubler(12))
print(mytripler(13))
