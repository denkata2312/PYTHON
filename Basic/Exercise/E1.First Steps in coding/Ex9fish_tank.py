length = int(input())
width = int(input())
height = int(input())
percent_filled_space = float(input())

sum_space = (length * width * height) * 0.001
needed_water = sum_space * (1 - percent_filled_space / 100)
print(needed_water)