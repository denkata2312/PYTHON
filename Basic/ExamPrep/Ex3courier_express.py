weight = float(input())
type_courier = input()
distance = int(input())

total = 0.03

if type_courier == "standard":
    if weight <= 1:
        total = distance * 0.03
    if 1 < weight <= 10:
        total = distance * 0.05
    elif 11 <= weight <= 40:
        total = distance * 0.10
    elif 41 <= weight <= 90:
        total = distance * 0.15
    elif 91 <= weight <= 150:
        total = distance * 0.20

elif type_courier == "express":
    if weight <= 1:
        total = distance * 0.03 + 0.3 * 0.8 * weight * distance
    elif weight <= 10:
        total = distance * 0.05 + 0.5 * 0.4 * weight * distance
    elif 11 <= weight <= 40:
        total = distance * 0.10 + 0.10 * 0.05 * weight * distance
    elif 41 <= weight <= 90:
        total = distance * 0.15 + 0.15 * 0.02 * weight * distance
    elif 91 <= weight <= 150:
        total = distance * 0.20 + 0.20 * 0.01 * weight * distance

else:
    print("Invalid service type.")
    exit()

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total:.2f} lv.")