item = [
    "A: 3liter air bersih",
    "B: sabun",
    "C: baju ganti",
    "D: stok makanan 3 hari",
    "E: sarung tangan",
    "F: pisau",
    "G: sendal",
    "H: powerbank",
    "I: senter"
]

print("pada tahun 2024 saya misi pribadi untuk menyelamatkan orang di hutan")
print("jarak hutan dari hutan tempat kamu berada adalah 20km")
print("saya di beri waktu 3 hari untuk menyelamatkan orang tersebut dan diberi kesempatan untuk membawa 4 barang tqambahan")
print("pililah barang2 ini sebanyak 4 yang manakah barang yang alan kamu bawa?")

for objek in item:
    print(objek)

print("untuk memilih 4 barang yang akan kamu bawa, kamu harus ketik 4 huruf berdasarkan index item")
print("barang apa saja yang akan kamu bawa?")
pilihan = input("enter your choice:")

# print(pilihan)
barang = list(pilihan.split())
print(barang)

if 'A' not in barang:
    print("tanpa air kamu akan dehidrasi")
if 'C' not in barang:
    print("bajunya kotor")

if 'D' not in barang:
    print("kamu bakal maag")

if 'F' not in barang:
    print("kamu tidak bisa survive dari mangsa")

if 'A' in barang and 'C' in barang and 'D' in barang and 'F' in barang:
    print("hore kamu mendapatkan barang yang memungkinkan untuk selamat 3 hari")
else:
    print("kamu tidak akan bisa bertahan hidup selama 3 hari")
