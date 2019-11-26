def setup():
    size(500,500)
    smooth()
    background(50)
    strokeWeight(5)
    stroke(250)
    
cx=250
cy=250
cRadius=200
counter=1
mcolor=1


def draw():
    global cx, cy, cRadius, counter, mcolor
    x1 = sin( counter )* cRadius + cx
    y1 = cos( counter )* cRadius + cy
    mcolor = mcolor + 1
    stroke ( mcolor )
    line(cx , cy , x1 , y1)
    counter = counter + 2*PI /255
    
    if( counter > 2*PI):
        counter=0
        mcolor=0
        background(50)
    
