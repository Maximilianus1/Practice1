#create list with sorted by keys nums from other list using lambda
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
#create list with sorted by keys nums from other list using lambda
words = ["blank", "pie", "coconut", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
