import random
from string import ascii_letters, digits, punctuation

all_characters = ascii_letters + digits + punctuation

password_length = 20

password = ''.join(random.sample(all_characters, password_length))

print(password)