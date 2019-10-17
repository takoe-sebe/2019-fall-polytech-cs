windowWight=500
windowHeight=550
ellipseSize=100
ellipseWight=200
ellipseHeight=300

def setup():
    size(windowWight,windowHeight)
    smooth()
    background(255)
    fill(50,80)
    stroke(100)
    strokeWeight(3)
    noLoop()
    
def draw():
        ellipse(windowWight/2, windowHeight/2 - ellipseSize/2, ellipseWight, ellipseHeight)
        ellipse(windowWight/2 - ellipseSize/2, windowHeight/2, ellipseWight, ellipseHeight)
        ellipse(windowWight/2 + ellipseSize/2, windowHeight/2, ellipseWight, ellipseHeight)
        ellipse(windowWight/2, windowHeight/2 + ellipseSize/2, ellipseWight, ellipseHeight)


        
