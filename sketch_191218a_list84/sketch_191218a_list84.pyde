rotateCounter = 0
def setup():
    global font
    size(600,600)
    smooth()
    background(0)
    font = loadFont ("Bauhaus93-48.vlw")
    textFont (font , 48)
        
def draw():
    global rotateCounter
    translate(width/2,height/2)
    pushMatrix()
    rotate(rotateCounter)
    fill(255)
    text("Black", mouseX - width /2, mouseY - height /2)
    popMatrix()
    
    pushMatrix()
    rotate(-rotateCounter*1.5)
    fill(0)
    text("White", width/2-mouseX, height/2-mouseY)
    popMatrix()
    
    rotateCounter +=0.05
