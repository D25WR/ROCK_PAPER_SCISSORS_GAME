import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def play_round():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    computer_choice = random.choice(choices)
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    result, score = determine_winner(user_choice, computer_choice)
    print(result)

    return score

def main():
    print("Welcome to Rock-Paper-Scissors!")

    play_again = True
    user_score = 0
    computer_score = 0

    while play_again:
        round_score = play_round()
        if round_score == 1:
            user_score += 1
        elif round_score == -1:
            computer_score += 1

        user_input = input("Do you want to play again? (yes/no): ").lower()
        while user_input not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            user_input = input("Do you want to play again? (yes/no): ").lower()

        if user_input == 'no':
            play_again = False

    print("Final Scores:")
    print("User:", user_score)
    print("Computer:", computer_score)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
