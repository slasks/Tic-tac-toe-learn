#imports
from ssl import HAS_TLSv1_1
from zlib import Z_BLOCK
from cmu_graphics import *

#global varibles
app.round = 0
app.row = 3
app.col = 3
board = makeList(app.row, app.col)
hit = makeList(app.row, app.col)
Turn = []
Playerscore = open("test.txt", "r")
app.pscore = int(Playerscore.read())

#make the board
for x in range(app.row):
    for y in range(app.col):
        a = Rect(50 + 100 * x, 50 + 100 * y,100, 100, fill = "white", border = "green")
        hit[x][y] = a
        b = Label("", a.centerX, a.centerY,size = 70)
        board[x][y] = b

#computer brain
def pickai():
    #clear the board
    Turn.clear()
    #varibles
    a = -1
    b = -1
    v1 = 0
    v2 = 0
    v3 = 0
    h1 = 0
    h2 = 0
    h3 = 0
    v1b = 0
    v2b = 0
    v3b = 0
    h1b = 0
    h2b = 0
    h3b = 0
    d1 = 0
    d2 = 0
    chance = randrange(1, 101)
    #add all position the computer can choice to Turn
    for row in range(app.row):
        for col in range(app.col):
            if board[row][col].value == "":
                Turn.append([row, col])
    #make 25% chance for blunder
    if chance > 25:
        #pick a edge
        for x in Turn:
            if x == [0, 1] or x == [1, 0] or x == [2, 1] or x == [1, 2]:
                print(x)
                a, b = x
                break
        #pick a corner 
        for x in Turn:
            if x == [0, 0] or x == [0, 2] or x == [2, 0] or x == [0, 2] or x == [2, 2]:
                print(x)
                a, b = x
                break
        #pick center
        for x in Turn:
            if x  == [1, 1]:
                a, b = x
                break
        #look if you can block a 3 in a row diagonal not needed bechouse it allways goes in corner first
        for row in range(app.row):
            for col in range(app.col):
                p = board[row][col]
                if p.value == "x":
                    if row == 0:
                        v1 += 1
                    if row == 1:
                        v2 += 1
                    if row == 2:
                        v3 += 1
                    if col == 0:
                        h1 += 1
                    if col == 1:
                        h2 += 1
                    if col == 2:
                        h3 += 1
                if v1 == 2:
                    for i in range(3):
                        if board[0][i].value == "":
                            a, b = [0, i]
                            break
                if v2 == 2:
                    for i in range(3):
                        if board[1][i].value == "":
                            a, b = [1, i]
                            break
                if v3 == 2:
                    for i in range(3):
                        if board[2][i].value == "":
                            a, b = [2, i]
                            break
                if h1 == 2:
                    for i in range(3):
                        if board[i][0].value == "":
                            a, b = [i, 0]
                            break
                if h2 == 2:
                    for i in range(3):
                        if board[i][1].value == "":
                            a, b = [i, 1]
                            break
                if h3 == 2:
                    for i in range(3):
                        if board[i][2].value == "":
                            a, b = [i, 2]
                            break
        #look if you can complete a 3 in a row
        for row in range(app.row):
            for col in range(app.col):
                c = board[row][col]
                if c.value == "O":
                    if row == 0:
                        v1b += 1
                    if row == 1:
                        v2b += 1
                    if row == 2:
                        v3b += 1
                    if col == 0:
                        h1b += 1
                    if col == 1:
                        h2b += 1
                    if col == 2:
                        h3b += 1
                    if (row == 0 and col == 0) or (row == 1 and col == 1) or (row == 2 and col == 2):
                        d1 += 1
                    if (row == 1 and col == 1) or (row == 2 and col == 0) or (row == 0 and col == 0):
                        d2 += 1
                if v1b == 2:
                    for i in range(3):
                        if board[0][i].value == "":
                            a, b = [0, i]
                            break
                if v2b == 2:
                    for i in range(3):
                        if board[1][i].value == "":
                            a, b = [1, i]
                            break
                if v3b == 2:
                    for i in range(3):
                        if board[2][i].value == "":
                            a, b = [2, i]
                            break
                if h1b == 2:
                    for i in range(3):
                        if board[i][0].value == "":
                            a, b = [i, 0]
                            break
                if h2b == 2:
                    for i in range(3):
                        if board[i][1].value == "":
                            a, b = [i, 1]
                            break
                if h3b == 2:
                    for i in range(3):
                        if board[i][2].value == "":
                            a, b = [i, 2]
                            break
                if d1 == 2:
                    if board[0][0].value == "":
                        a, b = [0, 0]
                        break
                    if board[1][1].value == "":
                        a, b = [1,  1]
                        break
                    if board[2][2].value == "":
                        a, b = [2, 2]
                        break
                if d2 == 2:
                    if board[2][0].value == "":
                        a, b = [2, 0]
                        break
                    if board[1][1].value == "":
                        a, b = [1,  1]
                        break
                    if board[0][2].value == "":
                        a, b = [0, 2]
                        break
    #if non of those are an option pick a random pos
    else:       
        a, b = choice(Turn)
    #place O                                          
    if a > -1:
        board[a][b].value = "O"

#draw win or lose rect         
def loeseorwin(lorw):
    if lorw  == "win":
        Rect(50,50,300,300,fill = "green", opacity = 75)
        Label("You Win!!", 200, 200, size = 50)
        app.pscore += 1
        Playerscore = open("test.txt", "w")
        Playerscore.write(str(app.pscore))
        app.stop()
    elif lorw == "draw":
        Rect(50,50,300,300,fill = "yellow", opacity = 75)
        Label("Draw", 200, 200, size = 50)
        app.stop()
    else:
        Rect(50,50,300,300,fill = "red", opacity = 75)
        Label("You lose", 200, 200, size = 50)
        app.stop()

#check if win
def checkwin():
    v1 = 0
    v2 = 0
    v3 = 0
    h1 = 0
    h2 = 0
    h3 = 0
    for row in range(app.row):
        for col in range(app.col):
            if board[row][col].value == "x":
                if row == 0:   
                    v1 += 1
                if row == 1:
                    v2 += 1
                if row == 2:
                    v3 += 1
                if col == 0:
                    h1 += 1
                if col == 1:
                    h2 += 1
                if col ==2:
                    h3 += 1
    
    if v1== 3 or v2 == 3 or v3 == 3:
        loeseorwin("win")
    if h1== 3 or h2 == 3 or h3 == 3:
        loeseorwin("win")
    if board[0][0].value == "x" and board[1][1].value == "x" and board[2][2].value == "x":
        loeseorwin("win")
    if board[0][2].value == "x" and board[1][1].value == "x" and board[2][0].value == "x":
        loeseorwin("win")

#check if lose
def checklose():
    v1a = 0
    v2a = 0
    v3a = 0
    h1a = 0
    h2a = 0
    h3a = 0
    for row in range(app.row):
        for col in range(app.col):
            if board[row][col].value == "O":
                if row == 0:   
                    v1a += 1
                if row == 1:
                    v2a += 1
                if row == 2:
                    v3a += 1
                if col == 0:
                    h1a += 1
                if col == 1:
                    h2a += 1
                if col ==2:
                    h3a += 1
    
    if v1a == 3 or v2a == 3 or v3a == 3:
        loeseorwin("lose")
    if h1a == 3 or h2a  == 3 or h3a == 3:
        loeseorwin("lose")
    if board[0][0].value == "O" and board[1][1].value == "O" and board[2][2].value == "O":
        loeseorwin("lose")
    if board[0][2].value == "O" and board[1][1].value == "O" and board[2][0].value == "O":
        loeseorwin("lose")            
#check draw
def checkdraw():
    if app.round > 8:
        loeseorwin("draw")


def onMousePress(x, y):
    #place X where player press
    for row in range(app.row):
        for col in range(app.col):
            if hit[row][col].hits(x, y):
                if board[row][col].value == "":
                    board[row][col].value = "x"
    
    
    #call functionc
    checkwin()

    #count player move to rounds
    app.round += 1
    
    #make it so computer not can place tiles after game is done
    if app.round < 9:
        pickai()
    
    #call lose function
    checklose()
    
    #count computer move to round
    app.round += 1

def onStep():
    checkdraw()
Label("player score: ", 50, 25, size = 10)
Label(app.pscore ,100, 25, size = 10)
cmu_graphics.run()