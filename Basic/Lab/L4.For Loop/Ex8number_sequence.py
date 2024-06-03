n = int(input())

max_num = float('-inf')
min_num = float('inf')

for i in range(1, n + 1):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num
    if current_num < min_num:
        min_num = current_num

print(max_num)
print(min_num)