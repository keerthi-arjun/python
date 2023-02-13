string = "hello my name is abcde"

words = string.split()

for word in words:
    if len(word) % 2 == 0:
        print(f"The word '{word}' has an even length.")
