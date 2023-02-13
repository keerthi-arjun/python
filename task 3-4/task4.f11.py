def count_letters(input_str):
    upper_count = 0
    lower_count = 0
    for char in input_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("Number of uppercase letters:", upper_count)
    print("Number of lowercase letters:", lower_count)
input_str = input("Enter a string: ")
count_letters(input_str)
