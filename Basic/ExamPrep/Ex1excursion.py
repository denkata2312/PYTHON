count_group = int(input())
count_nights = int(input())
cards_for_transport = int(input())
tickets_for_museum = int(input())

nights = count_nights * 20
transport = cards_for_transport * 1.60
museum = tickets_for_museum * 6

price = nights + transport + museum
group = price * count_group
unwanted = group * 1.25

print(f"{unwanted:.2f}")