def setup():
    global img0, img1
    background(100)
    smooth()
    img0=loadImage("dog.jpg")
    img1=loadImage("dog2.jpg")
    size(700,583)
def draw():
    myTintBO = map(mouseX , 0, width , 0, 255)
    myTintVP = map(mouseX , 0, width , 255, 0)
    tint (255 , myTintVP )
    image(img0 , 0, 0)
    tint (255 , myTintBO )
    image(img1 , 0, 0)
