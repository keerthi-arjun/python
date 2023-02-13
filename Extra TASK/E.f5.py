def reverse_vowel(string):
    vowels = "aeiouAEIOU"
    string = string[::-1]
    for i, char in enumerate(string):
        if char in vowels:
            print(char, "at index", i)

string = input("Enter a string: ")
reverse_vowel(string)
