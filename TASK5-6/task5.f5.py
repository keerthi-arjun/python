def get_even_length_strings(filename):
    with open(filename, 'r') as file:
        return [line for line in file if len(line.strip()) % 2 == 0]
if __name__ == "__main__":
    even_length_strings = get_even_length_strings("doc.txt")
    for string in even_length_strings:
        print(string, end="")
