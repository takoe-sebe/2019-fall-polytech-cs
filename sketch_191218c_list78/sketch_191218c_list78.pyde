def setup():
    global img0, img1
    background(100)
    smooth()
    noStroke()
    img0=loadImage("dog.jpg")
    img1=loadImage("dog1.jpg")
    size(700,583)
def draw():
    if(frameCount==1):
        image(img1,0,0)
    pointSize = map(mouseX , 0, width , 0, 100)
    pointAlpha = map(mouseY , 0, height , 0, 255)
    x=int(random(img0.width))
    y=int(random(img0.height))
    pix = img0.get(x,y)
    
    
    fill(pix, pointAlpha )
    ellipse (x,y,pointSize , pointSize )
    
    tint(255,2)
    image(img1,0,0)
    
    def keyPressed():
        saveFrame (" myProcessing " + frameCount + ".jpg")
