import math

first_time = int(input())
second_time = int(input())
third_time = int(input())

total = first_time + second_time + third_time

minutes = total // 60
seconds = total % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')