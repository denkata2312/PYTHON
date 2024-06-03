price_of_trip = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

amount_puzzle = number_of_puzzles * 2.6
amount_dolls = number_of_dolls * 3
amount_bears = number_of_bears * 4.10
amount_minions = number_of_minions * 8.2
amount_trucks = number_of_trucks * 2

total_amount = (amount_puzzle + amount_dolls + amount_bears + amount_minions + amount_trucks)

total_number = (number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks)

if total_number >= 50:
    total_amount *= 0.75

total_amount = total_amount * 0.9

if total_amount >= price_of_trip:
    print(f"Yes! {total_amount - price_of_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_of_trip - total_amount:.2f} lv needed.")