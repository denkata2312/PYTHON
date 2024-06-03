type_flowers = input()
number_flowers = int(input())
budget = int(input())

ROSE_PRICE = 5
DAHLIAS_PRICE_ = 3.80
TULIP_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.5

if type_flowers == "Roses":
    total_price = number_flowers * ROSE_PRICE
    if number_flowers > 80:
        total_price = total_price * 0.9

elif type_flowers == "Dahlias":
    total_price = number_flowers * DAHLIAS_PRICE_
    if number_flowers > 90:
        total_price = total_price * 0.85

elif type_flowers == "Tulips":
    total_price = number_flowers * TULIP_PRICE
    if number_flowers < 80:
        total_price = total_price * 0.85

elif type_flowers == "Narcissus":
    total_price = number_flowers * NARCISSUS_PRICE
    if number_flowers < 120:
        total_price = total_price * 1.15

elif type_flowers == "Gladiolus":
    total_price = number_flowers * GLADIOLUS_PRICE
    if number_flowers < 80:
        total_price = total_price * 1.20

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")