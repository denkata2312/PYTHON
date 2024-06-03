stay_day = int(input())
accommodation = input()
rating = input()

nights = stay_day - 1
price = 0

if accommodation == "room for one person":
    price = 18 * nights

elif accommodation == "apartment":
    if nights < 10:
        price = nights * 25
    elif nights < 10:
        price = (nights * 25) * 0.7
    elif 10 < nights < 15:
        price = (nights * 25) * 0.65
    elif nights > 15:
        price = (nights * 25) * 0.50

elif accommodation == "president apartment":
    if nights < 10:
        price = (nights * 35) * 0.1
    elif 10 < nights < 15:
        price = (nights * 35) * 0.85
    elif nights > 15:
        price = (nights * 35) * 0.8

if rating == "positive":
    price = price * 1.25
elif rating == "negative":
    price = price * 0.9

print(f"{price:.2f}")