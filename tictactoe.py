#imports
from operator import index
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
test = open("empty.txt", "r")
empty= list(test.read().split())
Boardstate = []
app.win = False

#app.avalue = 0
#app.bvalue = 0
#for i in empty:
#    x, y = i.replace('[','').replace(']','').split(',')
#    print(y)
##    x = int(x)
 #   y = int(y)
 #  print(x, y)
 #   em.append([x, y])


#print(empty)
#print(em)



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
    points = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    a = -1
    b = -1
        #add all position the computer can choice to Turn
    
    
    for row in range(app.row):
        for col in range(app.col):
            if board[row][col].value == "":
                Turn.append([row, col])
    
    file = open("data.txt", "r")
    line_count = 0
    for coun in enumerate(file):
        line_count += 1
    file.close()
    
    data = open("data.txt", "r")
    
        
    content = data.readlines()
    for i in range(line_count):
        a = content[i]
        x = a.replace('[','').replace(']','').replace(",", "").replace(" ","")
        print(x)
        
        if x[0] == "w":
            for i in range(9):
                if x[4 + i * 3] == "O":
                    points[i] += 1
        
        if x[0] == "l":
            for i in range(9):
                if x[5 + i * 3] == "O":
                    points[i] -= 1
    
            
            
        
    print(points)
     
   
    
    
    for i in range(9):
        
        bignumber = points[0]

        for i in points:
            if i > bignumber:
                bignumber = i
        
        Indexa = points.index(bignumber)
        print(Indexa)
    
        if Indexa == 0 and board[0][0].value == "":
            a = 0
            b = 0
            break
        elif Indexa == 1 and board[1][0].value == "":
            a = 1
            b = 0
            break
        elif Indexa == 2 and board[2][0].value == "":
            a = 2
            b = 0
            break
        elif Indexa == 3 and board[0][1].value == "":
            a = 0
            b = 1
            break
        elif Indexa == 4 and board[1][1].value == "":
            a = 1
            b = 1
            break
        elif Indexa == 5 and board[2][1].value == "":
            a = 2
            b = 1
            break
        elif Indexa == 6 and board[0][2].value == "":
            a = 0
            b = 2
            break
        elif Indexa == 7 and board[1][2].value == "":
            a = 1
            b = 2
            break
        elif Indexa == 8 and board[2][2].value == "":
            a = 2
            b = 2
            break
        else:
            points[Indexa] = -1000000000
            print("aaaaaaaaaaa", points)
        
    
    #place O                                          
    if a > -1:
        board[a][b].value = "O"
    


#draw win or lose rect         
def loeseorwin(lorw):
    if lorw  == "win":
        app.win = True
        Rect(50,50,300,300,fill = "green", opacity = 75)
        Label("You Win!!", 200, 200, size = 50)
         
        test = open("data.txt", "a")
        for row in range(3):
            for col in range(3):
                z = board[row][col].value 
                if z  == "":
                    Boardstate.append("-")
                else:   
                    Boardstate.append(z)
        

        test.write("lose "  + str(Boardstate) + "\n")
        
        app.stop()
    elif lorw == "draw":
        Rect(50,50,300,300,fill = "yellow", opacity = 75)
        Label("Draw", 200, 200, size = 50)
        app.stop()

        test = open("data.txt", "a")
        for row in range(3):
            for col in range(3):
                z = board[row][col].value 
                if z  == "":
                    Boardstate.append("-")
                else:   
                    Boardstate.append(z)
        

        test.write("draw " + str(Boardstate) + "\n")
    else:
        Rect(50,50,300,300,fill = "red", opacity = 75)
        Label("You lose", 200, 200, size = 50)

        test = open("data.txt", "a")
        for row in range(3):
            for col in range(3):
                z = board[row][col].value 
                if z  == "":
                    Boardstate.append("-")
                else:   
                    Boardstate.append(z)
        
        

        test.write("win< " + str(Boardstate) + "\n")
       

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

pickai()
app.round += 1

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

    if app.win == False:
        checklose()
    
    #count computer move to round
    app.round += 1

def onStep():
    checkdraw()
   

cmu_graphics.run()