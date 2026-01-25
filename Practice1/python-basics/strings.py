a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
yufheiuHfewusgfwugfewgfpuw
wejuyfeiugerhyugfhwewrr
w
rswr
w
r
ew
r
w
rw
r
w
r

"""
print(a)

b = "Hello, World! Again         "
print(b.lower())
print(b.upper())
print(b.capitalize())
print(b[2:7])
print(b[:8])
print(b[4:])
print(b.strip())

age = 233
txt = f"My name is Dracula, I am {age}"
print(txt)

z="abba"
v="rock"
c=z+v
print(c)
c=z+" "+v
print(c)

txt2 = f"The price is {320 * 123} tenge"
print(txt2)

txt3 = "We are the so-called \"Vikings\" from the north at the Calradia."
print(txt3)

txt4 = "\x48\x65\x3c\xbc\x6f"
print(txt4) 
 
print(b.isalnum())
print(b.isalpha())
print(b.isdigit())
print(b.find("a"))
print(b.isupper())
print(b.islower())
print(b.count("a"))