def setup():
    size(500,500)
    smooth()
    background(150)
    strokeWeight(1)
def draw():
    fill(434,654,545,random(26,100))
    myY2 = mouseY + random ( -10 ,10) *1
    myX2 = mouseX + random ( -10 ,10) *1
    ellipse(mouseX , mouseY , myX2 , myY2)
    
