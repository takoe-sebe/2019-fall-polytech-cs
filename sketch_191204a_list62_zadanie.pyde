xCoordinate = [1,2,3,4,5,6,7,8,9,10]
def setup():
    size(500,500)
    smooth()
    noStroke()
    for i in range(len(xCoordinate)):
        xCoordinate[i] = 35*i + 90

def draw():
    background(50)
    for i in range(len(xCoordinate)):
        fill(200,40)
        ellipse(xCoordinate[i], 250, 15*i, 15*i)
        fill(0)
        ellipse(xCoordinate[i], 250, 3,3)
    for i in range(len(xCoordinate)):
        fill(200,40)
        ellipse(xCoordinate[i], 350, 135-15*i, 135-15*i)
        fill(0)
        ellipse(xCoordinate[i], 350, 3,3)


def keyPressed():
    if (key == 's'):
        saveFrame("Photo")
