count_tournament = int(input())
starting_points = int(input())
count_win = 0
sum_all_tournament_points = 0

for i in range(count_tournament):
    current_stage = input()

    if current_stage == "W":
        count_win += 1
        sum_all_tournament_points += 2000
    elif current_stage == "F":
        sum_all_tournament_points += 1200
    elif current_stage == "SF":
        sum_all_tournament_points += 720

final_points = starting_points + sum_all_tournament_points
average_points = sum_all_tournament_points // count_tournament
percent_win = (count_win / count_tournament) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_win:.2f}%")