'''
Paper, rock, scissors game to be played in terminal.
It takes the player choice, randomized the computer's choice, then apply the rules:
1) Rock crushes scissors
2) Paper covers rock
3) Scissors cuts paper

If them choose the same, it's a draw.
'''

# import random library
import random

# creates a list of the options of the game
options = ['Rock', 'Paper', 'Scissors']

# Take user input choice as a integer variable with a try-except loop for
# three times or untill the player types a valid number
i = 3
while True:
    try:
        player_choice = int(input('''
        *****************************************
        Welcome to the Paper-Rock-Scissors' game.
        *****************************************
        Make your choice wisely:
        1) Rock
        2) Paper
        3) Scissors
        4) Exit
        '''))
        if player_choice >=1 and player_choice <= 4:
            break
        else:
            i -= 1
            print(f'Invalid number. You need to type a number between 1 and 4.\nYou have more {i} attempts.')
            if i==0:
                print('Shutting down...')
                exit(1)
    except Exception as e:
        i -= 1
        print(f'Invalid number. You need to type a number between 1 and 4.\nYou have more {i} attempts.')
        if i==0:
            print('Shutting down...')
            exit(1)
# close the game if user choose 4
if player_choice == 4:
    print('The game is closed.')
    exit(1)

# changes the input user to option in the list
player_choice = options[player_choice-1]

# randomize the computer choice using the random library
computer_choice = random.choice(options)

# creates a string variable to print the result to the player

display_text = '''
You choose: {0}
The computer choose: {1}
The result: {2}
'''

# implement if-elif-else statements with the rules of the game
if player_choice == 'Rock':
    if computer_choice == 'Rock':
        print(display_text.format(player_choice, computer_choice, 'It\'s a drawn. Try again.'))
    elif computer_choice == 'Paper':
        print(display_text.format(player_choice, computer_choice, 'You lose.\nPaper covers rock.\nBest luck next time.'))
    else:
        print(display_text.format(player_choice, computer_choice, 'You Win.\nRock crushes scissors.\nYou did well.'))
elif player_choice == 'Paper':
    if computer_choice == 'Rock':
        print(display_text.format(player_choice, computer_choice, 'You Win.\nPaper covers rock.\nYou did well.'))
    elif computer_choice == 'Paper':
        print(display_text.format(player_choice, computer_choice, 'It\'s a drawn. Try again.'))
    else:
        print(display_text.format(player_choice, computer_choice, 'You lose.\nScissors cuts paper.\nBest luck next time.'))
else:
    if computer_choice == 'Rock':
        print(display_text.format(player_choice, computer_choice, 'You lose.\nRock crushes scissors.\nBest luck next time.'))
    elif computer_choice == 'Paper':
        print(display_text.format(player_choice, computer_choice, 'You Win.\nScissors cuts paper.\nYou did well.'))
    else:
        print(display_text.format(player_choice, computer_choice, 'It\'s a drawn. Try again.'))