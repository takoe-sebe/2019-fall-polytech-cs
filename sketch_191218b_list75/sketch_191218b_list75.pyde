isAnimate=True
currentFrame = 1
def setup():
    global img1, img2, img3
    background(100)
    smooth()
    size(800,800)
    frameRate(5)
    img1=loadImage("dog1.jpg")
    img2=loadImage("dog2.jpg")
    img3=loadImage("dog3.jpg")
def draw():
    global currentFrame, isAnimate
    background(100)
    if isAnimate:
        if currentFrame==1:
            image(img1, mouseX, mouseY)
        elif currentFrame==2:
            image(img2, mouseX, mouseY)
        elif currentFrame==3:
            image(img3, mouseX, mouseY)
        currentFrame+=1
        if currentFrame >3:
            currentFrame = 1
    else:
        image(img1, mouseX, mouseY)
def keyPressed():
    global isAnimate
    isAnimate = not isAnimate
