even_list = []
odd_list = []

for i in range(5):
    num = int(input("Enter a number between 1 and 50: "))
    while num < 1 or num > 50:
        num = int(input("Invalid input. Enter a number between 1 and 50: "))
        
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
        
print("The sum of even numbers is:", sum(even_list))
print("The maximum even number is:", max(even_list))

print("The sum of odd numbers is:", sum(odd_list))
print("The maximum odd number is:", max(odd_list))
