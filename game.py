from computer import computer_choice

def play_match(win_score):
    player_score = 0
    computer_score = 0
    round_no = 0

    while player_score < win_score and computer_score < win_score:
        round_no += 1
        print("*************************")
        print(f" ROUND {round_no} \n ************************")
        
        choices = ["ROCK", "PAPER", "SCISSOR"]
        user = int(input("ENTER YOUR CHOICE '1', '2' or '3':"))

        if user == 1:
            player = "ROCK"
        elif user == 2:
            player = "PAPER"
        elif user == 3:
            player = "SCISSOR"
        else:
            print("INAVLID INPUT! Please Enter 1,2or 3 ")
            continue

        computer = computer_choice(choices)

        print(f"Computer choice: {computer}, Your choice:{player}")
        if player == computer:
            print("It is a draw , try again")
        elif player == "ROCK" and computer == "SCISSOR":
            print("YOU WIN")
            player_score += 1
        elif player == "ROCK" and computer == "PAPER":
            print("You lose")
            computer_score += 1
        elif player == "PAPER" and computer == "SCISSOR":
            print("You lose")
            computer_score += 1
        elif player == "PAPER" and computer == "ROCK":
            print("You win")
            player_score += 1
        elif player == "SCISSOR" and computer == "PAPER":
            print("You win")
            player_score += 1
        elif player == "SCISSOR" and computer == "ROCK":
            print("You lose")
            computer_score += 1
        else:
            print("invalid input, please give proper inputs ")

    return player_score, computer_score, round_no