print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for division")
print("Enter 4 for multiplication")
print("Enter 5 for average")

choice = int(input("Enter your choice: "))

if choice in [1, 2, 3, 4]:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))


if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 / num2
elif choice == 4:
    result = num1 * num2
elif choice == 5:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    result = (num1 + num2 + num3 + num4) / 4
else:
    print("Invalid choice")

if result < 0:
    print("NEGATIVE",result)
else:
    print("The result is:", result)



