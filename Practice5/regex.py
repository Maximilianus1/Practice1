import re
#1
s = input()
a = re.fullmatch("ab*", s)
print(f"{a.group()}")
#2
s = input()
a = re.fullmatch("ab{2,3}", s)
if(a):
    print(a.group())
else:
    print(a)
#3
s = input()
a = re.findall(r"[a-z]+_", s)
print(a)
#4
s = input()
a = re.findall(r"[A-Z][a-z]+", s)
print(a)
#5
s = input()
a = re.fullmatch(r"a.*b", s)
if(a):
    print(a.group())
else:
    print(a)
#6
s = input()
a = re.sub(r"[ ,.]", ":", s)
print(a)
#7
s = input()
a = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s)
print(a)
#8
s = input()
a = re.split(r"(?=[A-Z])", s)
print(a)
# 9
s = input()
a = re.sub(r"(\w)([A-Z])", r"\1 \2", s)
print(a)
#10
s = input()
a = re.sub(r"(\w)([A-Z])", r"\1_\2", s).lower()
print(a)