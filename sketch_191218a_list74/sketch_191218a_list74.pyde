def setup():
    global img0, img1, img2, img3
    background(100)
    smooth()

    img0 = loadImage("img.jpg")
    img1 = loadImage("elka.png")
    img2 = loadImage("sun.png")
    img3 = loadImage("donut.png")
    size(720,500)
def draw():
    background(100)
    image(img0, 0, 0)
    image(img2,mouseX*0.7-150,100)
    image(img1, 0, 0)
    image(img3,width-mouseX*1.5,35)
