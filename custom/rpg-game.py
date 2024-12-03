def Showinteraction(): 
  print('''
RPG GAME 
========
      

GET TO THE GARDEN WITH A KEY AND POSION
AVOID THE MONSTER
      
COMMANDS:
go [direction]
get [item]
''')

def Status():
    print("--------------------------------------------------------")
    print("you are in the " + CurrentRoom)
    print("inventory: " + str(inventory))
    if "item" in rooms[CurrentRoom]:
      print("you see an " + rooms[CurrentRoom]["item"])
    
    print("--------------------------------------------------------")

inventory = []
CurrentRoom = 'hall'


rooms = {
    'hall': {
        "south": "kitchen",
        "east": "dining room",
        "item": "key"
    },
    'kitchen': {
        "north": "hall",
        "item": "monster"
    },
    'dining room': {
        "west": "hall",
        "south": "garden",
        "item": "posion"
    },
    'garden': {
        'north': "dining room"

    }

}

Showinteraction()

while True:
   Status()
   move = ''
   while move == '':
      move = input('>')
      move = move.lower().split()