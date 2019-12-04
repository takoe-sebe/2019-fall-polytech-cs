cx = 0
cy = 0
fsize = 0
counter = 0
class FunnyRect():

    def setCenter(self, x,y):
        self.cx = x
        self.cy = y

    def setSize(self, size):
        self.size = size

    def render(self):
        rect(self.cx, self.cy, self.size, self.size)

funnyRect0b = FunnyRect()
funnyRect0b1 = FunnyRect()

def setup():
    size(600,600)
    smooth()
    noStroke()
   # rectMode(CENTER)
    funnyRect0b.setSize(50)
    funnyRect0b1.setSize(20)

def draw():
    global counter
    background(255)
    fill(50)
    obX = mouseX + sin( counter )*150
    obY = mouseY + cos( counter )*150
    funnyRect0b.setCenter(mouseX, mouseY)
    funnyRect0b.render()
    funnyRect0b1.setCenter(obX, obY)
    funnyRect0b1.render()
    counter+=0.05
