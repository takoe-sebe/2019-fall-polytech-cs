def setup():
    size(500,500)
    smooth()
    background(255)
    noStroke()
    noLoop()
def draw():
    for i in range(0,10):
        for k in range(1,10,2):
            fill(200-i*20)
            rect(i*40+50,k*40+50,35,35)
            for k in range(0,10,2):
                fill(i*20)
                rect(i*40+50,k*40+50,35,35)
