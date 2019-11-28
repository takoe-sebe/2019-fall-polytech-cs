add_library('sound')

r_width = 0

scale = 1.3
bands = 64
sum = [0.0] * bands
smooth_factor = 0.2
 
def setup():
    size(800, 600)
    global img, imgtr
    img = loadImage("nebo.jpg")
    imgtr = loadImage("sun.png")
    
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
    
    fill(255, 243, 0 ,100)
    noStroke()

    fft.analyze()
 
    for i, v in enumerate(sum):
        sum[i] += (fft.spectrum[i] - v) * smooth_factor
        ellipse(width/2, height/2, -sum[i] * height * scale,  -sum[i] * height * scale)
        fill(255, 100,0,100)
        ellipse(width/2, height/2, -sum[i] * height * scale,  -sum[i] * height * scale)

    image(imgtr, width / 2, height / 2)
