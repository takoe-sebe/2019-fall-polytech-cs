windowWight=650
windowHeight=650
ellipseSize=200

def setup():
    size(windowWight,windowHeight)
    smooth()
    background(255)
    fill(50,80)
    stroke(100)
    strokeWeight(3)
    noLoop()
    
def draw():
        ellipse(windowWight/2, windowHeight/2 - ellipseSize/2, ellipseSize, ellipseSize)
        ellipse(windowWight/2 - ellipseSize/2, windowHeight/2, ellipseSize, ellipseSize)
        ellipse(windowWight/2 + ellipseSize/2, windowHeight/2, ellipseSize, ellipseSize)
        ellipse(windowWight/2, windowHeight/2 + ellipseSize/2, ellipseSize, ellipseSize)


        
