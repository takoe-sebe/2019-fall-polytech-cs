i=0
k=1
flug=1
def setup():
    size(500,500)
    smooth()
    strokeWeight(1)
    background(0)
def upDate():
    global i,k,flug
    i=i+k
    if(i==255):
        k=-1
    if(i==0):
        k=1
def draw():
    global i,k,flug
    stroke(i,20)
    #myRandom=random(-20,20)
    myY1=mouseY-random(0,500)
    myY2=mouseY+random(0,500)
    line(0,myY1,500,myY2)
    upDate()
