numbers = range(1, 101)
result = list(filter(lambda x: x % 7 == 0 and x % 3 != 0, numbers))
print(result)
    