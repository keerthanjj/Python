import random

choices = ['rock', 'paper', 'scissors']

player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

while player_choice not in choices:
    print("Invalid choice. Please enter rock, paper, or scissors.")
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == 'rock' and computer_choice == 'scissors') or \
     (player_choice == 'paper' and computer_choice == 'rock') or \
     (player_choice == 'scissors' and computer_choice == 'paper'):
    print(f"You win! {player_choice} beats {computer_choice}.")
else:
    print(f"Computer wins! {computer_choice} beats {player_choice}.")

