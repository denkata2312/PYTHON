pens_price = 5.8
marker_price = 7.2
cleaning_price = 1.2

pack_pens = int(input())
pack_markers = int(input())
cleaning_litters = int(input())
discount = int(input())

price_sum = (pack_pens * pens_price) + (pack_markers * marker_price) + (cleaning_litters * cleaning_price)
discount_price = price_sum - (price_sum * discount/100)

print(discount_price)