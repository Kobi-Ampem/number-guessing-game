# A number guessing game based on the game.txt

import random

def number_guessing():
    print("Hello, welcome to my number guessing game")
    
    attempts = 0
    max_try = 10
    number = random.randint(1,100)

    while attempts < max_try:
        
        try:
            guess = int(input("What number am I thinking? "))
            attempts += 1
            try_word = "try" if attempts == 1 else "tries"

            if guess == number:
                print(f"Congratulations, you got the guess correct on {attempts} {try_word}.🎉")
                print("The End!")
                break
            elif guess > number:
                print("Guess too high.")
            elif guess < number:
                print("Guess too low")

        except (ValueError, TypeError) as e:
            print(f"{e}, Check your input, must be a number.")

    if attempts >= max_try:
        print("You couldn't get the correct guess.")
        print(f"I was thinking {number}")

    again = input("Would you like to play again? y/n  ")
    again = again.lower()
    if again == "y":
        number_guessing()
    else:
        print("Thanks for playing, goodbye.")

number_guessing()