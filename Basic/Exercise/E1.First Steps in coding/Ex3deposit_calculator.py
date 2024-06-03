deposit_sum = float(input())
term_deposit = int(input())
percent = float(input())

per_month =((deposit_sum * percent/100)/12)
total_sum = deposit_sum + term_deposit * per_month
print(total_sum)