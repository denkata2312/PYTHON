vegetables = float(input())
fruits = float(input())
vegetables_kilograms = int(input())
fruits_kilograms = int(input())

price_vegetables = vegetables * vegetables_kilograms
price_fruits = fruits * fruits_kilograms

total = (price_vegetables + price_fruits) / 1.94

print("{:.2f}".format(total))