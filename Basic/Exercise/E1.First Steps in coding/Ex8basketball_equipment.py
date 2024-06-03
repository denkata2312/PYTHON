year_tax = int(input())
sneakers_price = year_tax * 0.6
suit_price = sneakers_price * 0.8
ball_price = suit_price / 4
accessories = ball_price / 5

sum = year_tax + sneakers_price + suit_price + ball_price + accessories

print(sum)