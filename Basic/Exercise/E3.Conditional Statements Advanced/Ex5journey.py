budget = float(input())
season = input()

destination = 0
accommodationType = 0
spendMoney = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodationType = "Camp"
        spendMoney = budget * 0.3
    elif season == "winter":
        accommodationType = "Hotel"
        spendMoney = budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodationType = "Camp"
        spendMoney = budget * 0.4
    elif season == "winter":
        accommodationType = "Hotel"
        spendMoney = budget * 0.8

else:
    destination = "Europe"
    spendMoney = budget * 0.9
    accommodationType = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodationType} - {spendMoney:.2f}")