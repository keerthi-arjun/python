def check_length(num):
    if len(str(num)) != 4:
        return f"The length is too {'short' if len(str(num)) < 4 else 'long'}!!! Please provide only four digits."
    return "The number is of correct length."
try:
    num = int(input("Enter a four-digit number: "))
    print(check_length(num))
except ValueError:
    print("Invalid input. Please enter a valid number.")
