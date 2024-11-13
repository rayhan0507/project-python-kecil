import random

character = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.,/';][]!?"

length = int(input("password length? "))
jumlah = int(input("jumlah plihan password? "))

for p in range(jumlah):
    password = ''
    for c in range(length):
        password += random.choice(character)
    print(password)