text = str(input())

vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
sum = 0

for char in text:
    if char.lower() in vowels:
        sum += vowels[char.lower()]

print(sum)