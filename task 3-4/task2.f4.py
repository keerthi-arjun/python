numbers = [3, 5, 2, 8, 1]
min_num = numbers[0]
max_num = numbers[0]
for number in numbers:
    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number
print("Smallest number:", min_num)
print("Largest number:", max_num)
