year_tax = int(input())

sneakers = year_tax * 0.6
clothes = sneakers * 0.8
ball = clothes / 4
accessories = ball / 5

total = year_tax + sneakers + clothes + ball + accessories

print(f"{total:.2f}")