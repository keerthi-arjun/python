string = input("Enter a string: ")
uppercase_characters = [char for char in string if char.isupper()]
print("Uppercase characters in the string:", "".join(uppercase_characters))
