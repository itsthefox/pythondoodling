import random
import sys

def game():
    for i in range(3):
        print(".")
    print("Picking number...")
    num = random.randint(1,100)
    print("I have chosen a number between 1, and 100. Guess it.")
    guess = int(input("Your guess: "))
    if num == guess:
        print("You guessed my number, very well then.")
    else:
        print("You're wrong. Oh well.")
        print("The number was " + str(num) + ".")
    again = input("Would you like to play again? y/n: ")
    if again == "y":
        game()
    else:
        sys.exit()

print("Starting the number guessing game...")
for i in range(3):
    print(".")

game()