nylon_price = 1.5
paint_price = 14.5
water_price = 5
bag_price = 0.4

number_nylon = int(input())
paint_litters = int(input())
water_quantity = int(input())
hours_of_work = int(input())

sum_of_materials = ((number_nylon+2) * nylon_price) + ((paint_litters * 1.1) * paint_price) + (water_quantity * water_price) + bag_price

work_amount = (sum_of_materials * 0.3) * hours_of_work
total_sum = sum_of_materials + work_amount

print(total_sum)