lg_diam =0
lg_rad=0
lg_circ=0
sm_diam=0
cx=0
cy=0
def setup():
    global lg_diam , lg_rad , lg_circ , sm_diam , cx , cy
    background(100)
    smooth()
    size(500,400)
    noStroke()
    lg_diam = width * .55
    lg_rad = lg_diam /2
    lg_circ = PI * lg_diam
    cx = width /2
    cy = height /2
    colorMode (HSB)
def draw():
    fill(0,10)
    rect(0,0,width,height)
    
    nbr_circles = int(map(mouseX , 0, width , 6, 50))
    sm_diam = ( lg_circ / nbr_circles )
    myColor =  int(map(mouseY , 0, height , 150, 255))
    fill(myColor ,180 ,190 ,100)
    for i in range(int(nbr_circles)):
        angle = i * TWO_PI / nbr_circles
        x = cx + cos(angle) * lg_rad 
        y = cy + sin(angle) * lg_rad
        ellipse (x, y, sm_diam , sm_diam )
    filter (BLUR , 3)
