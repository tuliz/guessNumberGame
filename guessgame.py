import random

HARD_DIFFICULTY = 5
EASY_DIFFICULTY = 10

def checkGuess(guess, turns, answer):
    if guess == answer:
        print("thats right, you guessed the number\n")
        return turns

    elif guess < answer:
        print('too low. try again\n')
        return turns - 1
    else:
        print('too high. try again\n')
        return turns - 1

def setDifficulty():
    """let user choose difficulty and set number of turns by the difficulty he chooses."""
    difficulty = input("choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_DIFFICULTY
    else:
        return HARD_DIFFICULTY
    


def game():
    answer = random.randint(1,100)
    print("welcome to the guessing the number game\nim thinking about a number between 1 and 100\n")
    turns = setDifficulty()

    #loop for repeating guess if they are wrong
    guess = 0
    while answer != guess:
        print(f"You have {turns} attempts remaining to guess the number\n")
        guess = int(input('make a guess: '))
        turns = checkGuess(guess, turns, answer)

        #check if there are turns left, if no turns left finish game and exit function.
        if turns == 0:
            print('no turns left. Game Over.')
            return


game()