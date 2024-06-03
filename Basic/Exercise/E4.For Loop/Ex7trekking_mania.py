count_people = int(input())

people_climber_musala = 0
people_climber_monblan = 0
people_climber_kilimadjaro = 0
people_climber_k2 = 0
people_climber_everest = 0
all_people = 0

for i in range(count_people):
    count_climbers = int(input())
    all_people += count_climbers
    if count_climbers <= 5:
        people_climber_musala += count_climbers
    elif count_climbers <= 12:
        people_climber_monblan += count_climbers
    elif count_climbers <= 25:
        people_climber_kilimadjaro += count_climbers
    elif count_climbers <= 40:
        people_climber_k2 += count_climbers
    else:
        people_climber_everest += count_climbers

people_musala = (people_climber_musala / all_people) * 100
print(f"{people_musala:.2f}%")
people_monblan = (people_climber_monblan / all_people) * 100
print(f"{people_monblan:.2f}%")
people_kilimadjaro = (people_climber_kilimadjaro / all_people) * 100
print(f"{people_kilimadjaro:.2f}%")
people_k2 = (people_climber_k2 / all_people) * 100
print(f"{people_k2:.2f}%")
people_everest = (people_climber_everest / all_people) * 100
print(f"{people_everest:.2f}%")