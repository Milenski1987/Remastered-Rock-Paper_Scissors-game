import random

games_count = 0
computer_won_count = 0
user_won_count = 0
draws_count = 0
stop_game = False

while True:
    computer_choice = ""
    computer_turn = random.randint(1, 3)
    if computer_turn == 1:
        computer_choice = "rock"
    elif computer_turn == 2:
        computer_choice = "scissors"
    elif computer_turn == 3:
        computer_choice = "paper"

    user_choice = ""
    user_turn = input("Please choose [r]ock, [s]cissors or [p]aper: ")
    if user_turn.lower() == "r":
        user_choice = "rock"
    elif user_turn.lower() == "s":
        user_choice = "scissors"
    elif user_turn.lower() == "p":
        user_choice = "paper"
    else:
        print("Invalid input. Please choose 'r' for rock, 's' for scissors, 'p' for paper!")
        continue

    if user_choice == computer_choice:
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        print(f"Result: Draw")
        draws_count += 1
    elif (user_choice == "rock" and computer_choice == "scissors") \
            or (user_choice == "scissors" and computer_choice == "paper") \
            or (user_choice == "paper" and computer_choice == "rock"):
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        print(f"Result: User wins")
        user_won_count += 1
    else:
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        print(f"Result: Computer wins")
        computer_won_count += 1

    games_count += 1

    while True:
        restart = input("Do you want another try? (Yes or No): ")
        if restart.lower() == "yes":
            break
        elif restart.lower() == "no":
            stop_game = True
            break
        else:
            print("Invalid input. Try again...")

    if stop_game:
        print("Game over!")
        print(f"{games_count} games played,"
              f"\nComputer won: {computer_won_count} times,"
              f"\nUser won: {user_won_count} times,"
              f"\nDraw: {draws_count} times.")
        break