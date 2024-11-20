print("selamat datang di kalkulator codero")

while True:
    mode = int(input('1. penjumlahan\n2. pengurangan\n3. perkalian\n4. pembagian\n5. stop\nPilih mode: '))
    
    if mode == 5:
        print("terimakasih sudah menggunakan kalkulator saya")
        break
    elif mode < 1 or mode > 5:
        print("Pilihan tidak valid, coba lagi.")
        continue
    
    angka_1 = int(input("masukkan angka pertama: "))
    angka_2 = int(input("masukkan angka kedua: "))
    
    if mode == 1:
        total = angka_1 + angka_2
        print(f"hasil dari {angka_1} + {angka_2} = {total}")

    elif mode == 2:
        total = angka_1 - angka_2
        print(f"hasil dari {angka_1} - {angka_2} = {total}")
        
    elif mode == 3:
        total = angka_1 * angka_2
        print(f"hasil dari {angka_1} * {angka_2} = {total}")

    elif mode == 4:
        total = angka_1 / angka_2
        print(f"hasil dari {angka_1} / {angka_2} = {total}")
