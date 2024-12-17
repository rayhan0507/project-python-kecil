import random

def mapp(n, k):
    arr = [[0 for row in range(n)] for column in range(n)]
    for num in range(k):
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        arr[y][x] = "X"
        
        # center-right
        if (x >= 0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1
        
        # center-left
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1

        # top-left
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1
        
        # top-right
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1

        # top-center
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1
            
        # bottom-right
        if (x >= 0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1

        # bottom-left
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1

        # bottom-center
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1

    return arr

def player_map(n):
    arr = [["-" for row in range(n)] for column in range(n)]
    return arr

def display_map(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")

def checkwon(map):
    for row in map:
        for cell in row:
            if cell == "-":
                return False
    return True

def continue_game(score):
    print("your score: ",  score)
    iscontinue = input("do you want to try again? y/n: ")
    if iscontinue == "n":
        return False
    
    return True

def game():
    game_status = True
    while game_status:
        difficulty = input("select your difficulty (b,i,h): ")
        if difficulty.lower() == 'b':
            n = 5
            k = 1
            
        elif difficulty.lower() == 'i':
            n = 6
            k = 8
        
        elif difficulty.lower() == 'h':
            n = 8
            k = 20

        else:
            print('invalid level')

        minesweeper_map = mapp(n, k)
        game_map = player_map(n)
        score = 0
        while True:
            if checkwon(game_map) == False:
                print("enter your cell to open: ")
                x = input("x(1 ke 5): ")
                y = input("y(1 ke 5): ")
                x = int(x) - 1
                y = int(y) - 1
                if (minesweeper_map[y][x] == "X"):
                    print("Game Over")
                    display_map(minesweeper_map)
                    game_status = continue_game(score)
                    break
                else:
                    game_map[y][x] = minesweeper_map[y][x]
                    display_map(game_map)
                    score += 1

            else:
                display_map(game_map)
                print("You have won")
                game_status = continue_game(score)
                break

if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        print("\n end of game bye bye")