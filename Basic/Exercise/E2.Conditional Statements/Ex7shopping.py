budget = float(input())
count_video_card = int(input())
count_CPU = int(input())
count_RAM = int(input())

sum_video_card = count_video_card * 250
sum_cCPU = count_CPU * (sum_video_card * 0.35)
sum_RAM = count_RAM * (sum_video_card * 0.1)
total_sum = sum_video_card + sum_cCPU + sum_RAM

if count_video_card > count_CPU:
    total_sum = total_sum - (total_sum * 0.15)

money_left = budget - total_sum
money_needed = total_sum - budget

if budget >= total_sum:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_needed:.2f} leva more!")