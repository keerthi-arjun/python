from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7]
flattened_numbers = str(reduce(lambda x, y: x * 10 + y, numbers))
print(flattened_numbers)
