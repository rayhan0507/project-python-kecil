tanya1 = str(input("apakah kamu suka bermain game: "))
kemalasan = 0
if tanya1 == "iya":
    kemalasan += 20
elif tanya1 == "kadang-kadang":
    kemalasan += 10

else:
    kemalasan -= 10
   
tanya2 = input('Apakah kamu suka nonton Anime/K-drama: ')

if tanya2 == "iya":
    kemalasan += 20

elif tanya2 == "kadang-kadang":
    kemalasan += 10
else:
    kemalasan += 0


tanya3 = input('Apakah kamu suka bermain sosmed: ')

if tanya3 == "iya":
    kemalasan += 20

elif tanya3 == "kadang-kadang":
    kemalasan += 10

else:
    kemalasan += 0

if kemalasan >= 60:
    print("kamu sangat pemalas")
elif kemalasan >= 30:
    print('kamu normal')
else:
    print('kamu anak yang rajin')