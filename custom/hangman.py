import time
import random

print("\nwelcome to hangman game by rehan\n")
nama = input("Enter your name: ")
print('hello', nama, "best your luck")
time.sleep(2)  
print("the game will start\nlet's play hanggame")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guess
    global length
    global play_game

    word_to_guess = ['senin', 'selasa', 'matahari', 'python', 'siang', 'jakarta', 'bola', 'bulan', 'orang', 'saya']
    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guess = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("do you want to play again? y=yes, n=no\n")
    while play_game not in ['y', 'n', 'Y', 'N']:
       play_game = input("do you want to play again? y=yes, n=no\n")
    if play_game == "y":
       main()
    elif play_game == "n": 
       print('thanks for playing')
       exit()

def hangman():
    global count
    global display
    global word
    global already_guess
    global play_game

    limit = 5
    guess = input("this is the hangman word" + display + "enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("invalid input, try a letter.\n")
        hangman()

    elif guess in word:
        already_guess.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guess:
        print("try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   ______ \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count) + "guess remaining\n")
        
        elif count == 2:
            time.sleep(1)
            print("   ______ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count) + "guess remaining\n")
        
        elif count == 3:
            time.sleep(1)
            print("   ______ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count) + "guesses remaining\n")
        
        elif count == 4:
            time.sleep(1)
            print("   ______ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count) + "last guess remaining\n")
        
        elif count == 5:
            time.sleep(1)
            print("   ______ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. Your are hanged!!!\n")
            print("The word was:", already_guess, word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()
hangman()