from math import ceil
film_name = input()
duration = int(input())
lunch_break = int(input())

time_for_eat = lunch_break / 8.0
time_for_rest = lunch_break / 4.0

time_for_watch = lunch_break - time_for_eat - time_for_rest

difference = ceil(time_for_watch - duration)
difference_one = ceil(duration - time_for_watch)

if time_for_watch >= duration:
    print(f"You have enough time to watch {film_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {film_name}, you need {difference_one} more minutes. ")