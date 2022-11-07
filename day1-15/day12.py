# 2022/02/12 day10

# 
# Guess number
# 
import random
def game_start():
    answer = random.randrange(101)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 ann 100.')
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
    if difficulty == 'easy':
        live = 10
    else:
        live = 5
    print(f'You have {live} attempts remaining to guess the number')   
    guess_number = int(input('Make a guess: '))
    game_over = False
    while not game_over:
        live -= 1
        if live == 0:
            print('you lose')
            print(f'The answer if {answer}')
            game_over = True
        elif guess_number == answer:
            print('you win.')
            game_over = True
        elif guess_number > answer:
            print('Too high.')
        else:
            print('Too low.')
        if not game_over:
            print(f'You have {live} attempts remaining to guess the number')    
            guess_number = int(input('Guess again: '))
    if input('play again? "y" or "n" ') == 'y':
        game_start()
game_start()
