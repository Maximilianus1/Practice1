def my_function(*kids):
  return "The oldest child is " + kids[1]

print(my_function("Misha", "Sasha", "Linus"))


def my_function1(numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function1([31, 73, 22, 912, 21]))