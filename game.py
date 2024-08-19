import random
import os


def clear_screen():
    os.system('cls')


game_count = 1


def rock_paper_scissors_aysenur_sasmaz():
    global game_count
    clear_screen()
    print("Welcome to the Rock-Paper-Scissors game...\n"
          "We added cat and dog options to the classic rock-paper-scissors game.\n"
          "Dog beats cat and paper.\n"
          "Cat beats rock and scissors.\n"
          "Let's start if you're ready:)")
    x = input("Type 'start' to begin the game, or 'exit' to quit:")
    if x == "exit":
        print("You just arrived, but it's your choice.")
        exit()
    elif x == "start":

        rules = {
            "paper": ["rock", "cat"],
            "rock": ["scissors", "dog"],
            "scissors": ["paper", "dog"],
            "dog": ["cat", "paper"],
            "cat": ["rock", "scissors"]
        }
        game_options = ["rock", "paper", "scissors", "cat", "dog"]

        round_counter = 1
        player_score = 0
        computer_score = 0

        while player_score < 2 and computer_score < 2:
            player = input("Please choose from rock-paper-scissors-cat-dog:").lower()
            computer = random.choice(game_options)
            print(f"Computer's choice: {computer}")

            if player == computer:
                print("It's a tie, play another round!")

            elif player in rules[computer]:
                print("You lost this round :(")
                computer_score += 1

            elif computer in rules[player]:
                print("You're lucky, you won this round!")
                player_score += 1

            else:
                print("You entered an invalid option")
            score_round = f"GAME COUNT: {game_count}--ROUND: {round_counter}"
            score_message = f"PLAYER: {player_score}--COMPUTER: {computer_score}"
            print(score_round)
            print(score_message)
            round_counter += 1
        if player_score == 2:
            print("Congratulations, YOU WON :)")
        elif computer_score == 2:
            print("I WON, I congratulate myself :)")
    else:
        print("You entered an invalid option")
        rock_paper_scissors_aysenur_sasmaz()

    while True:
        y = input("Do you want to play again? Type 'yes' or 'no':").lower()
        options = ["yes", "no"]
        computer_choice = random.choice(options)
        print(f"Computer's choice: {computer_choice}")
        if y == "yes" and computer_choice == "yes":
            game_count += 1
            rock_paper_scissors_aysenur_sasmaz()
            break
        elif y == "no" or computer_choice == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("You entered an invalid option, please try again.")


rock_paper_scissors_aysenur_sasmaz()
