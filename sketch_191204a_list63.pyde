xCoordinate = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
def setup():
    size(500,500)
    smooth()
    noStroke()
    myInit()
def myInit():
    println ("New coordinates : ")
    for i in range(len(xCoordinate)):
        xCoordinate [i] = 250 + random ( -100 ,100)
        println ( xCoordinate [i])

def draw():
    background(30)
    for i in range(len(xCoordinate)):
        fill(20)
        ellipse(xCoordinate[i], 250, 5, 5)
        fill(250,40)
        ellipse(xCoordinate[i], 250, 10*i,10*i)
    if (mouseX>250):
       myInit()

def keyPressed():
    if (key == 's'):
        saveFrame("Photo")
