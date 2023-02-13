def compare_strings(a, b):
    if len(a) > len(b):
        print(a)
    elif len(b) > len(a):
        print(b)
    else:
        print(a)
        print(b)

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
compare_strings(str1, str2)
