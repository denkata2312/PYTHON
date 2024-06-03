import math
one_racket = float(input())
number_rackets = int(input())
number_of_pair_of_sneakers = int(input())

one_pair_of_sneakers = one_racket /6

total_shoes_price = number_of_pair_of_sneakers * one_pair_of_sneakers
total_racket_price = one_racket * number_rackets

equipment_price = 0.2 * (total_racket_price + total_shoes_price)
total_price = total_racket_price + equipment_price + total_shoes_price

djokovic_payment = total_price / 8
sponsors_price = total_price - djokovic_payment

print(f"Price to be paid by Djokovic {math.floor(djokovic_payment)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_price)}")