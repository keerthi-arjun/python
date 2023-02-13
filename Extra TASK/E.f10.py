def even_numbers(numbers):
  evens = []
  for number in numbers:
    if number % 2 == 0:
      evens.append(number)
  return tuple(evens)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_tuple = even_numbers(numbers)
print("Even numbers:", even_tuple)
