#imports
from ssl import HAS_TLSv1_1
from zlib import Z_BLOCK
from cmu_graphics import *

hits = []
possible = []
app.score = 0
for i in range(50):
    hits.append(Rect(0 + 8 * i, 0, 8, 400, fill = rgb(i * 1, i * 1, i * 1)))


for i in range(2):
    for x in range(50):
        possible.append(hits[x])

print(possible)

def pick():
    
    p = choice(possible)
    
    if p.fill == rgb(0, 0, 0):
        app.score += 1
        possible.append(p)
    else:
        app.score -= 1
        possible.remove(p)
    

def onStep():
    pick()
    print(app.score)


cmu_graphics.run()