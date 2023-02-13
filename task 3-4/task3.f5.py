squared_numbers = []
for number in range(1, 31):
    if number <= 5 or number >= 26:
        squared_numbers.append(number ** 2)
print("Squared numbers:", squared_numbers)
