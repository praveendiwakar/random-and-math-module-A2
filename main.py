import random
while True:
    user_input = input("enter your choice (rock, paper, scissors)")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"you have chosen {user_input} and computer chose {computer_action}")

    if user_input == computer_action:
        print("you and comp have entered the same thing, its a tie")

    elif user_input == "rock":
        if computer_action == "paper":
            print("paper beats rock, computer wins")
        else: print("you win")

    elif user_input == "paper":
            if computer_action == "scissors":
                print("scissor beats paper, computer wins")
            else: print("you win")

    elif user_input == "scissor":
            if computer_action == "rock":
                print("rock beats scissors, computer wins")
            else: print("you win")

    play_again = input("play again? (yes/no)")
    if play_again != "yes":
         break
    
    