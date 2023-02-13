def sort_words(input_string):
    words = input_string.split("-")
    words.sort()
    return "-".join(words)
input_string = "apple-banana-cherry-date-fig-grape"
print(sort_words(input_string))
