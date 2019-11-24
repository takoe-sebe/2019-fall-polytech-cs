def setup():
    size(500,500)
    smooth()
    noLoop()
    noStroke()
    ellipseMode(CENTER)
    
    
def draw():
    background(255)
    border=50
    nw=width-2*border
    nh=height-2*border
    number=5
    nWstep=nw/number
    nHstep=nh/number
    for i in range(0,number):
        for j in range(0,number):
             x = border + j* nWstep + nWstep /2;
             y = border + i* nHstep + nHstep /2;
             size = 85 - (j+i)*10;
             mColor = size *4;
             fill(mColor , 78, 800);
             ellipse (x, y, size , size);
             fill (250);
             ellipse (x, y, 3, 3);
        
