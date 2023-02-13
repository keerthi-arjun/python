def is_even(num):
    return num % 2 == 0
even_numbers = list(filter(is_even, range(1, 21)))
print(even_numbers)
