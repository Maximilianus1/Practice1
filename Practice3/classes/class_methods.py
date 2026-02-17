# create class with method
class Person:
  # constructor
  def __init__(self, name):
    self.name = name

  # greeting method
  def greet(self):
    print("Hello, my name is " + self.name)

# create object and call methods
p1 = Person("Jhon")
p1.greet()


# create class with methods
class Calculator:
  # add two numbers
  def add(self, a, b):
    return a + b

  # multiply two numbers
  def multiply(self, a, b):
    return a * b

# create object and call methods
calc = Calculator()
print(calc.add(31, 32))
print(calc.multiply(45, 43))


# create class with method to get
class Person:
  # constructor with name and age
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # return info
  def get_info(self):
    return f"{self.name} is {self.age} years"

# create object and call get method
p1 = Person("Tobi", 28)
print(p1.get_info())


class Person:
  # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # increase age
  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Lork", 22)
p1.celebrate_birthday()
p1.celebrate_birthday()


class Person:
  # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # string representation
  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)


class Playlist:
  # constructor
  def __init__(self, name):
    self.name = name
    self.songs = []

  # add song
  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  # remove song
  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  # show songs
  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.add_song("RAP GOD")
my_playlist.add_song("I was made for lovin' you, baby!")
my_playlist.show_songs()


class Person:
  # constructor
  def __init__(self, name):
    self.name = name

  # greet method
  def greet(self):
    print("Hello!")

p1 = Person("Josh")

# delete method
del Person.greet

# try to call method under will cause an error
# p1.greet()
