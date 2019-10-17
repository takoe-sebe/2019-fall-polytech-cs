def setup():
    size(650,650)
    noLoop()
    
def drawMyScene(myColor):
    fill(myColor)
    rotate(PI/4)
    rect(0,50,150,50)
    rect(50,0,50,150)
    
def draw():
    background(20)
    smooth()
    noStroke()
    
    pushMatrix()
    translate(100,0)
    drawMyScene(180)
    popMatrix()
    
    pushMatrix()
    translate(220,110)
    scale(2)
    drawMyScene(220)
    popMatrix()
    
    pushMatrix()
    translate(520,350)
    scale(1.4)
    drawMyScene(80)
    popMatrix()
