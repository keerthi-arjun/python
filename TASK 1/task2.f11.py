number = 42
counter = 0
while counter < 5:
    guess = int(input("Guess the lucky number: "))
    if guess == number:
        print("Good guess!")
        break
    print("Try again!")
    counter += 1
else:
    print("Sorry but that was not very successful")
print("Game over!")
