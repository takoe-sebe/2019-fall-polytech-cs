add_library('sound')

amount = 20
num=1.0
scale = 1.5
bands = 64
sum = [0.0] * bands
smooth_factor = 0.2
 
def setup():
    size(800, 600)
    smooth()
    global img, imgtr, imgob
    img = loadImage("nbo.jpg")
    imgtr = loadImage("sun.png")
    imgob=loadImage("rosa.png")
    imageMode(CENTER)
    
    sample = SoundFile(this, "the-wanted-chasing-the-sun.mp3")
    sample.loop()
 
    global fft
    fft = FFT(this, bands)
    fft.input(sample)
    
class nebo():
    def render(self):
        image(img, width / 2, height / 2)
fon=nebo()
class oblako():
    def render(self):
        image(imgob, frameCount, height/2)
cloud=oblako()
class solnce():
    def render(self):
        pushMatrix()
        rotate(frameCount)
        image(imgtr,random(-1,1), random(-1,1))
        popMatrix()
sun=solnce()
class luchi():
    def render(self):
        stroke(255, 0, 0, 100)
        global num
        fill(0, 40)
        rect(-1, -1, width+1, height+1)
        translate(width/2, height/2)
        for i, v in enumerate(sum):
            sum[i] += (fft.spectrum[i] - v) * smooth_factor
            maxX = map(-sum[i] * height * scale, 0, width, 1, 250)
            for i in range(0,360,amount):
                phi=radians(i+num)
                xi=radians(i+amount-num)
                x1 = sin(phi) * maxX
                y1 = cos(phi) * maxX
                x2 = sin(xi) * maxX
                y2 = cos(xi) * maxX
                fill(255, 100, 0 ,100) 
                bezier(x1, y1, x1-x2, y1-y2, x2-x1, y2-y1, x2, y2)
                fill(255, 175,0,100)
                bezier(x1, y1, x1+x2, y1+y2, x2+x1, y2+y1, x2, y2)
                fill(255, 124, 0)
                ellipse(x1, y1, 5, 5)
                ellipse(x2, y2, 5, 5)
            num += 0.5
luch=luchi()
def draw():
    background(0)
    fon.render()
    cloud.render()
    fft.analyze()
    luch.render()
    sun.render()
    


    
