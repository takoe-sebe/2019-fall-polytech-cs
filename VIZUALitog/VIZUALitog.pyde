add_library('sound')

r_width = 0
amount = 20
num=1
scale = 1.5
bands = 64
sum = [0.0] * bands
smooth_factor = 0.2
 
def setup():
    size(800, 600)
    global img, imgtr, imgob
    img = loadImage("nbo.jpg")
    imgtr = loadImage("sun.png")
    imgob=loadImage("rosa.png")
    imageMode(CENTER)
    
    global r_width
    r_width = width / float(bands)
    sample = SoundFile(this, "the-wanted-chasing-the-sun.mp3")
    sample.loop()
 
    global fft
    fft = FFT(this, bands)
    fft.input(sample)
    
 
def draw():
    background(0)
    image(img, width / 2, height / 2)
    image(imgob, frameCount, height/2)
    fill(255, 243, 0 ,100)
    noStroke()
    
    fft.analyze()
    
    stroke(255, 0, 0, 100)
    global num, amount
    fill(0, 40)
    rect(-1, -1, width+1, height+1)
    translate(width/2, height/2)
    for i, v in enumerate(sum):
        sum[i] += (fft.spectrum[i] - v) * smooth_factor
        maxX = map(-sum[i] * height * scale, 0, width, 1, 250)
        for i in range(0,360,amount):
            x = sin(radians(i+num)) * maxX
            y = cos(radians(i+num)) * maxX
            x2 = sin(radians(i+amount-num)) * maxX
            y2 = cos(radians(i+amount-num)) * maxX
            fill(255, 100, 0 ,100) 
            bezier(x, y, x-x2, y-y2, x2-x, y2-y, x2, y2)
            fill(255, 175,0,100)
            bezier(x, y, x+x2, y+y2, x2+x, y2+y, x2, y2)
            fill(255, 124, 0)
            ellipse(x, y, 5, 5)
            ellipse(x2, y2, 5, 5)
        num += 0.5;
    pushMatrix()
    translate(0,0)
    rotate(frameCount/2)
    image(imgtr, 0, 0)
    popMatrix()



    
