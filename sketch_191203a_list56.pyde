centerX = 500/2
centerY = 500/2
leng = 350
angle = PI/4
weight = 1
counter = 0
radius=50
class myline():

    def render(self, centerX, centerY, angle):
        x1 = centerX - cos(angle)*leng/2
        y1 = centerY + sin(angle)*leng/2
        x2 = centerX + cos(angle)*leng/2
        y2 = centerY - sin(angle)*leng/2

        stroke(50,100)
        strokeWeight(weight)
        line(x1,y1,x2,y2)
        strokeWeight(5)
        stroke(50)
        line(x2, y2, x2, y2)
        line(x1, y1, x1, y1)

mline = myline()

def setup():
    size(500,500)
    smooth()
    background(255)


def draw():
    global counter,radius
    counter += 0.05

    if counter > 2*PI:
        counter = 0
        radius=radius+50

    mline.render(width/2 + sin(counter)*radius, height/2 + cos(counter)*radius, counter*2)
