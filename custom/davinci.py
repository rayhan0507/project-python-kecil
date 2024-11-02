huruf = 'abcdefghijklmnopqrstuvwxyz1234567890'
key = int(input("masukan key: "))

new_pesan = ''

pesan = input("please enter a message: ")

for kalimat in pesan:
   if kalimat in huruf:
     position = huruf.find(kalimat)
     new_position = (position+key)%26
     new_kalimat = huruf[new_position]
     #print(new_kalimat)
     new_pesan += new_kalimat
   else:
      new_pesan += kalimat
   
print(new_pesan)