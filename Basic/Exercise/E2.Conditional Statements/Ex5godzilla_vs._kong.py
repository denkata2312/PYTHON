budget = float(input())
staff = int(input())
cloths_price_for_one_person = float(input())

decor = budget * 0.1
clothes = staff * cloths_price_for_one_person

decor = budget * 0.1

if staff > 150:
    clothes = clothes * 0.9

sum = decor + clothes

difference = abs(sum - budget)

if sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")