number = int(input())
bonus = 0

if number <= 100:
    bonus = 5
elif number > 1000:
    bonus = bonus + number * 0.1
else:
    bonus = bonus + number * 0.2

if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2

print(bonus)
print(bonus + number)