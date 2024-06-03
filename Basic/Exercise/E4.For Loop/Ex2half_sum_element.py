number = int(input())

max_number = float('-inf')
sum_val = 0

for i in range(1, number + 1):
    current_num = int(input())
    sum_val += current_num

    if current_num > max_number:
        max_number = current_num

sum_without_max_number = sum_val - max_number

if sum_without_max_number == max_number:
    print("Yes")
    print(f"Sum = {sum_without_max_number}")
else:
    diff = abs(sum_without_max_number - max_number)
    print("No")
    print(f"Diff = {diff}")