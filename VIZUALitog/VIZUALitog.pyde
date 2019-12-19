add_library('sound')

amount = 20
num=1.0
scale = 1.9
bands = 64
sum = [0.0] * bands
smooth_factor = 0.2
 
def setup():
    fullScreen()
    size(800, 600)
    smooth()
    global img, imgtr, imgob, vniz, vverh
    img = loadImage("nbo.jpg")
    imgtr = loadImage("sun.png")
    imgob=loadImage("ros.png")
    vniz = loadImage("niz.png")
    vverh = loadImage("verh.png")
    imageMode(CENTER)
    
    sample = SoundFile(this, "the-wanted-chasing-the-sun.mp3")
    sample.loop()
 
    global fft
    fft = FFT(this, bands)
    fft.input(sample)
    
class zadnii_fon():
    def render(self):
        image(img, width / 2, height / 2)
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
                fill(255, random(0,100), 0 ,100) 
                bezier(x1, y1, x1-x2, y1-y2, x2-x1, y2-y1, x2, y2)
                fill(255, random(175,255),0,100)
                bezier(x1, y1, x1+x2, y1+y2, x2+x1, y2+y1, x2, y2)
                fill(255, 124, 0)
                ellipse(x1, y1, 5, 5)
                ellipse(x2, y2, 5, 5)
            num += 0.5
        pushMatrix()
        rotate(frameCount)
        image(imgtr,random(-1,1), random(-1,1))
        popMatrix()
fon=zadnii_fon()

class oblako():
    def render(self):
        image(imgob, frameCount*2-700, height/2)
cloud=oblako()

class vniz():
    def render(self):
        image(vniz,-frameCount*2.7+1300,-200)
niz=vniz()

class vverh():
    def render(self):
        image(vverh,-frameCount*2.7+1300,-290)
verh=vverh()

def draw():
    background(0)
    fon.render()
    fft.analyze()
    if frameCount > 200:
        if frameCount%5==0:
            niz.render()
        else:
            verh.render()
    cloud.render()
    println(frameCount)

    
