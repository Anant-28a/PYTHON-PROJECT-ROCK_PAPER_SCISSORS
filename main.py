from game import play_match
from game_stats import display_statistics

matches_won = 0
matches_lost = 0

while True:
    name = input("Enter Your Name:")
    print("<><><><><><><><><><><><>><><><><>")
    print("ROCK,PAPER,SCISSORS WITH COMPUTER ")
    print("<><><>><><<>><<>><><<>><<><><>><<>")
    print("\n")
    print("RULES: ROCK BEATS SCISSORS\n \t PAPER BEATS ROCK\n \tSCISSORS BEAT PAPER")

    print("1.ROCK")
    print("2.PAPER")
    print("3.SCISSOR")

    print("\n SELECT MATCH TYPE:")
    print("1. BEST OF 3")
    print("2. BEST OF 5")
    print("3. BEST OF 7")
    match = int(input("ENTER YOUR CHOICE: "))

    if match == 1:
        win_score = 2
    elif match == 2:
        win_score = 3
    elif match == 3:
        win_score = 4
    else:
        print("ENTER 1, 2, OR 3")

    player_score, computer_score, round_no = play_match(win_score)

    print("\n")
    print("================================")

    if player_score == win_score:
        print("🎉 YOU WON THE MATCH!")
        matches_won += 1
    else:
        print("💻 COMPUTER WON THE MATCH!")
        matches_lost += 1

    print(f"FINAL SCORE: {player_score}-{computer_score}")
    print(f"TOTAL ROUNDS:{round_no}")

    display_statistics(matches_won, matches_lost)

    again = input("Do you want to play again? Y/N")
    if again.upper() != "Y":
        print(f"THAN YOU FOR PLAYING \t {name}")
        print("FINAL STATISTICS")
        display_statistics(matches_won, matches_lost)
        break


