chicken_price = 10.35
fish_price = 12.4
vegan_price = 8.15
delivery_price = 2.5

chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

sum_menus = (chicken_menu * chicken_price) + (fish_menu * fish_price) + (vegan_menu * vegan_price)
dessert = sum_menus/5

total_sum = sum_menus + dessert + delivery_price
print(total_sum)