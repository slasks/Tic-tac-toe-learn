from cmu_graphics import *

app.h = 700
app.height = 1000
app.width = 1000


data = open("data.txt", "r")
        
content = data.readlines()

for i in range(1000):
    z = content[i]

    
    if z[0] == "w":
        app.h -= 1
    if z[0] == "l":
        app.h += 1

    Circle(0 + i, app.h, 1)

    

cmu_graphics.run()