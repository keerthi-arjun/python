numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_even_numbers = list(map(lambda x: x**2, even_numbers))
print(squared_even_numbers)
