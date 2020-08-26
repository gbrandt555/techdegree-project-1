"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("*****Welcome to the number guessing game! Guess the random number to win!*****")
    low_num = 1
    high_num = 10
    answer = random.randint(low_num, high_num) 
    #I found the randint method at https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
    number_of_guesses = 0
    while True:
        try:
            guess = int(input("Guess a number between {} and {}! ".format(low_num, high_num)))
            
            if guess < low_num or guess > high_num:
                raise ValueError("You have entered a number outside of the range")
        except ValueError as err:
            print("You must enter a number between {} and {}!".format(low_num, high_num))
        else:
            if guess == answer:
                print("Congratulations you have guessed the random number!")
                number_of_guesses += 1
                print("You guessed the random number after {} tries!".format(number_of_guesses))
                print("Thank you for playing! Like and subscribe!")
                break
            elif guess < answer:
                print("Higher!^^^")
                number_of_guesses += 1
                continue
            elif guess > answer:
                print("Lower!vvv")
                number_of_guesses += 1
                continue
                
                

    


# Kick off the program by calling the start_game function.
start_game()