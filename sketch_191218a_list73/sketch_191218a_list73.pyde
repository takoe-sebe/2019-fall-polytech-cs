def setup():
    global img
    background(100)
    smooth()
    size(800,800)
    img = loadImage("img.jpg")
def draw():
    background(100)
    image(img, mouseX, mouseY)
