def setup():
    size(500,500)
    smooth()
    background(50)
    strokeWeight(5)
    stroke(250)
    noLoop()
    
cx=250
cy=250
cRadius=200


def draw():
    global cx, cy, cRadius
    for i in range(0,int(2*PI)):
        x1 = cos(i)* cRadius + cx
        y1 = sin(i)* cRadius + cy
        line(x1,y1,x1,y1)
    line(cx,cy,cx,cy)
