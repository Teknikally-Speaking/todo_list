# --------------------------------------------
# ✊ Rock, Paper, Scissors Game
# Author: [Your Name]
# Description: A fun terminal game where you play against the computer.
# --------------------------------------------

import random

# List of valid moves
choices = ['rock', 'paper', 'scissors']

# Function to get user's move
def get_user_choice():
    print("\nChoose your move: rock, paper, or scissors")
    user_input = input("Your choice: ").lower()
    while user_input not in choices:
        print("❗ Invalid choice. Please choose rock, paper, or scissors.")
        user_input = input("Try again: ").lower()
    return user_input

# Function to get computer's move
def get_computer_choice():
    return random.choice(choices)

# Function to determine the winner
def determine_winner(player, computer):
    print(f"\n🧍 You chose: {player}")
    print(f"💻 Computer chose: {computer}")

    if player == computer:
        return "🤝 It's a tie!"
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'paper' and computer == 'rock')
    ):
        return "🎉 You win!"
    else:
        return "😞 You lose."

# Main game loop
def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")

    while True:
        player = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(player, computer)
        print(result)

        # Ask if the user wants to play again
        play_again = input("\n🔁 Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("👋 Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    play_game()