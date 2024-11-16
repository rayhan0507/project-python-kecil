from random import randint

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    result = randint(min,max)
    result2 = randint(min,max)
    print("rolling the dices")
    print("the value are: ", result)
    print("the value are: ", result2)

    roll_again = input("roll the dice again? ")
    
