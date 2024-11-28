from requests import *


while input("do you want to play?, y = yes: ").lower() == "y":
    web = get("https://official-joke-api.appspot.com/random_joke")
    respond = web.json()
    print(respond.keys())
    if "setup" in respond:
        joke = respond['setup']
        print(joke)
        var = input("tekan apa saja untuk lanjut: ")
        answer = respond['punchline']
        print(answer)