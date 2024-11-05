skor = 0
nama = input("masukan 2 nama: ")

for huruf in nama:
    if huruf in 'aiueo':
        skor += 5
    if huruf in 'friend':
        skor += 10

print('nilai skor persahabatan: ', skor)

if skor >= 50:
    print("best friend")
if skor < 50:
    print("friend")
if skor <= 30:
    print("not friend") 