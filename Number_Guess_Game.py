import random

logo = r"""
,  , ,  , , ,  __   ,,       _,  ,  ,  _, _, _, ___,,  ,  _,  
|\ | |  ||\/| '|) /,|)     / _  |  | /,(,(,' |  |\ | / _  
|'\|'\|| | _|_)'\_'| \    '\_|'\|'\_  ) _) _|,|'\|'\_|` 
'  `    `'  `'       `'  `     _|     `   `'  '  '    '  `  _|                             '                            '                                                                                                                            
"""

def guess_number(number, attempt, guess_computer):
    if guess_computer == number:
        print(f"You got it! The answer was{guess_computer}")
    elif guess_computer > number:
        print("Too low.")
        print("Guess again.")
        print(f"You have {attempt} attempts remaining to guess the number.")
    elif guess_computer < number:
        print("Too high.")
        print("Guess again.")
        print(f"You have {attempt} attempts remaining to guess the number.")


def guess_again(attempt,guess_comp):
    while attempt != 0:
        guess_player = int(input('Make a Guess: '))
        attempt -= 1
        guess_number(guess_player, attempt,guess_comp)
        if guess_comp == guess_player:
            attempt = 0


def guessing_game():
    guess_computer = random.randint(1, 100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    guess_again(attempts, guess_computer)

guessing_game()