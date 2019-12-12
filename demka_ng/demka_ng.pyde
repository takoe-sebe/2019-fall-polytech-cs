smallPoint = 5
largePoint = 100

def setup():
    size(320, 600)
    global elka,ukr,sng
    elka = loadImage("elka.png")
    ukr = loadImage("ukrr.png")
    sng=loadImage("sng.png")
    imageMode(CENTER)
    noStroke()
    background(255)
    image(elka,width/2-5,height/2-48)


def draw():
    for i in range(0,500):
        pointillize = map(0, 0, width, smallPoint, largePoint)
        x = int(random(ukr.width))
        y = int(random(ukr.height))
        pix = ukr.get(x, y)
        fill(pix, 250)
        ellipse(x, y, pointillize, pointillize)
    translate(0,425)
    for i in range(0,500):
        pointillize = map(0, 0, width, smallPoint, largePoint)
        a = int(random(sng.width))
        b = int(random(sng.height))
        pix = sng.get(a, b)
        fill(pix, 250)
        ellipse(a, b, pointillize, pointillize)
