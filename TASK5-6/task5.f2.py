import sys
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"The file '{filename}' could not be found.")
        return False
    return True
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the name of the file as an argument.")
    else:
        filename = sys.argv[1]
        while not open_file(filename):
            filename = input("Enter the name of the file again: ")
