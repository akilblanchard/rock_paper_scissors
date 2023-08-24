import random

player_wins = 0
computer_wins = 0
draws = 0

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)

    player = input("Type Rock, Paper, Scissors: ").lower()

    if player not in choices:
        continue

    elif player == computer:
            print('computer: ',computer)
            print('player: ',player)
            print('Tie!')
            draws += 1

    elif player == "rock" and computer== "scissors":
        print("You won!")
        print('computer: ',computer)
        print('player: ',player)
        
        player_wins += 1

    elif player == "paper" and computer == "rock":
        print('computer: ',computer)
        print('player: ',player)
        print("You won!")
        player_wins += 1

    elif player == "scissors" and computer == "paper":
        print('computer: ',computer)
        print('player: ',player)
        player("You won!")
        player_wins += 1

    else:
        print('computer: ',computer)
        print('player: ',player)
        print("You lost!")
        computer_wins += 1

    play_again = input('Would you like to play again? (Yes / No): ').lower()

    if play_again == "no":
        break

print(f'You won {player_wins} times.')
print(f'The computer won {computer_wins} times.')
print(f'You guys drew {draws} times')
print("Goodbye!")