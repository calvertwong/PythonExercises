# Generate a random integer in the range [1,10]
# Ask the user to guess the number until it is correct
import random
play = "yes"
while play == "yes":
    lower_bound = 1
    upper_bound = 10
    secret_number = random.randint(lower_bound, upper_bound)

    while True:
        guess = int(input("Please enter your guess: "))
        if guess == secret_number:
            print("Congratulations!")
            break
        else:
            if guess < secret_number:
                print("Your guess was too low")
            else:
                print("Your guess was too high")
    play = input("Please enter 'yes' to keep playing: ")