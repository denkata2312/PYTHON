minutes_of_controla = int(input())
seconds_of_controloa = int(input())
lenght = float(input())
seconds_for_100 = int(input())

time_of_controla = minutes_of_controla * 60 + seconds_of_controloa
decrease_time = lenght / 120
total_decrease_time = decrease_time * 2.5
martin_time = (lenght / 100) * seconds_for_100 - total_decrease_time
difference = abs(time_of_controla - martin_time)

if martin_time <= time_of_controla:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {martin_time:.3f}.")
elif martin_time > time_of_controla:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")