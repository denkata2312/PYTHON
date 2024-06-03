age = int(input())
price_washing_machine = float(input())
price_for_toy = int(input())

sum_money = 0
count_toys = 0
money_even_age = 10

for current_age in range(1, age + 1):
    if current_age % 2 == 0:
        sum_money += money_even_age
        money_even_age += 10
        sum_money -= 1
    else:
        count_toys += 1

sum_money += count_toys * price_for_toy

diff = abs(sum_money - price_washing_machine)

if sum_money >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")