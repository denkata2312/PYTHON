teraza_pocket_money_for_day = float(input())
earn_money_per_day = float(input())
expenses = float(input())
price_of_present = float(input())

saved_pocket_money = teraza_pocket_money_for_day * 5
earn_money = earn_money_per_day * 5
total_saved_money = saved_pocket_money + earn_money
total = total_saved_money - expenses

if total > price_of_present:
    print(f"Profit: {total:.2f} BGN, the gift has been purchased.")

else:
    need_more_money = price_of_present - total
    print(f"Insufficient money: {need_more_money:.2f} BGN.")