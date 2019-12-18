isAnimate=True
currentFrame = 1
def setup():
    global img1, img2, img3, isAnimate
    background(100)
    smooth()
    size(800,800)
    frameRate(12)
    img1=loadImage("elka.png")
    img2=loadImage("donut.png")
    img3=loadImage("sun.png")
def draw():
    global currentFrame, isAnimate
    background(100)
    if(isAnimate):
        def kadr(currentFrame):
            switcher={
                1:'image(img1, mouseX, mouseY)',
                2:'image(img2, mouseX, mouseY)',
                3:'image(img3, mouseX, mouseY)'
            }
            return switcher.get(currentFrame,"kadrr")

        if(currentFrame>3):
            currentFrame=1
        else:
            image(img1, mouseX, mouseY)
def keyPressed():
    isAnimate = False
