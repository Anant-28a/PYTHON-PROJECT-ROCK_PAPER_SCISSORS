def calculate_win_percentage(matches_won, total_matches):
    if total_matches == 0:
        return 0.0
    return round((matches_won / total_matches) * 100, 2)

def display_statistics(matches_won, matches_lost):
    total_matches = matches_won + matches_lost
    win_percentage = calculate_win_percentage(matches_won, total_matches)

    print("\n========== STATISTICS ==========")
    print("Matches Played:", total_matches)
    print("Matches Won:", matches_won)
    print("Matches Lost:", matches_lost)
    print("Win Percentage:", win_percentage, "%")
    print("================================")