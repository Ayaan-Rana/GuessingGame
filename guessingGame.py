chances= 0
while chances < 5:
    guess = int(input("Choose a number between 1-9: "))
    if (guess>5):
        print("Your guess was too high. Guess a lower number.")
    elif (guess<5):
        print("Your guess was too low. Guess a higher number.")
    else:
        print("Congradulations! You picked the right number!!")

