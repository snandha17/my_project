"""Import the modules for the Number guess game"""
import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

guessing_number = random.randint(1,100) # generate number

"""Declare the global variable"""
attempts = -1
if difficulty_level == 'easy':
    attempts = 10
elif difficulty_level == 'hard':
    attempts= 5
else:
    print("Enter the correct word to play")

while attempts >= 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    attempts -= 1
    user_guess = int(input("Make a guess: "))
    if attempts == 0:
        print("You lose the game")
        break
    elif user_guess < guessing_number:
        print("To low..")
        print( "Guess again.")
    elif user_guess > guessing_number:
        print("To High..")
        print("Guess again.")
    else:
        print(f"You got it, the answer is {guessing_number}")
        break


