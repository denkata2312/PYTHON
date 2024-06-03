fruit = input()
day_of_week = input()
quantity = float(input())

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week =="Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        product_price = 2.50
    elif fruit == "apple":
        product_price = 1.20
    elif fruit == "orange":
        product_price = 0.85
    elif fruit == "grapefruit":
        product_price = 1.45
    elif fruit == "kiwi":
        product_price = 2.70
    elif fruit == "pineapple":
        product_price = 5.50
    elif fruit == "grapes":
        product_price = 3.85
    else:
        print("error")
        exit()

elif day_of_week == "Sunday" or day_of_week == "Saturday":
    if fruit == "banana":
        product_price = 2.70
    elif fruit == "apple":
        product_price = 1.25
    elif fruit == "orange":
        product_price = 0.90
    elif fruit == "grapefruit":
        product_price = 1.60
    elif fruit == "kiwi":
        product_price = 3.00
    elif fruit == "pineapple":
        product_price = 5.60
    elif fruit == "grapes":
        product_price = 4.20
    else:
        print("error")
        exit()

else:
    print("error")
    exit()

price = product_price * quantity
print(f"{price:.2f}")