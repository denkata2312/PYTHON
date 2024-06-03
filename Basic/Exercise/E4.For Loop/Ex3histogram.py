n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(1, n + 1):
    current_num = int(input())

    if current_num < 200:
        p1_count += 1
    elif current_num <= 399:
        p2_count += 1
    elif current_num <= 599:
        p3_count += 1
    elif current_num <= 799:
        p4_count += 1
    else:
        p5_count += 1

percent_p1 = (p1_count / n) * 100
percent_p2 = (p2_count / n) * 100
percent_p3 = (p3_count / n) * 100
percent_p4 = (p4_count / n) * 100
percent_p5 = (p5_count / n) * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")