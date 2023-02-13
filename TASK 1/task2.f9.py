number = 42
answer = "yes"
while answer != "no":
    guess = int(input("Guess the lucky number: "))
    if guess == number:
        print("You guessed it right!")
        break
    answer = input("Do you want to guess again (yes/no)? ").lower()
