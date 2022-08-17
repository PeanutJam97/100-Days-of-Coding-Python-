import random



def game():
    """Initiate a number guessing game"""
    lives = 0
    gameover = False

    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

    
    if difficulty == "easy":
        lives += 10
        number = random.randint(1, 101)
    else:
        lives += 5
        number = random.randint(1, 101)

    
        
    while not gameover:

        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))

        if guess == number:
            gameover = True
            print(f"You got it! The answer is {number}")
        elif guess > number:
            lives -= 1
            print("Too high.\nGuess again.")
        else:
            lives -= 1
            print("Too low.\nGuess again.")
        
        if lives == 0:
            gameover = True
            print("You've run out of guesses, you lose.")


game()





