import random
def get_user_choice():
    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

# Start the game
play_game()

#Customization1

import random
def get_user_choice():
    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def play_game():
    print("Welcome to the Rock, Paper, Scissors Game!")
    rounds = int(input("How many rounds would you like to play? "))
    user_score = 0
    computer_score = 0

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result, score = determine_winner(user_choice, computer_choice)
        print(result)
        
        if score == 1:
            user_score += 1
        elif score == -1:
            computer_score += 1
        
        print(f"Current Scores -> You: {user_score}, Computer: {computer_score}\n")
    
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Oh no! The computer won the game!")
    else:
        print("It's a tie game! Well played!")

    print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")

# Start the game
play_game()

