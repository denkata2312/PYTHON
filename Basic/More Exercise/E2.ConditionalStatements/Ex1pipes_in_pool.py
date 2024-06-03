v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

water = p1 * h + p2 * h

if water <= v:
    print("The pool is {:.2f}% full. Pipe 1: {:.2f}%. Pipe 2: {:.2f}%.".format(
        (water / v) * 100,
        (p1 * h / water) * 100,
        (p2 * h / water) * 100))
else:
    print("For {:.2f} hours the pool overflows with {:.2f} liters.".format(h, water - v))