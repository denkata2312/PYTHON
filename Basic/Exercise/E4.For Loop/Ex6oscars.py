actor_name = input()
academy_points = float(input())
count_examiners = int(input())

sum_all_points = academy_points

for i in range(1, count_examiners + 1):
    examiner_name = input()
    current_point = float(input())

    sum_all_points += (len(examiner_name) * current_point) / 2

    if sum_all_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {sum_all_points:.1f}!")
        break

if sum_all_points < 1250.5:
    print(f"Sorry, {actor_name} you need {abs(1250.5 - sum_all_points):.1f} more!")