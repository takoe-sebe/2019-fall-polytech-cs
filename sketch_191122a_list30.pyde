l1x1=0
l1y1=0
l1x2=500
l1y2=500
flug=1
mr=10
mg=150
mb=100
def setup():
    background(255)
    size(500,500)
    smooth()
def draw():
    global l1x1
    global l1y1
    global l1x2
    global l1y2
    global flug
    global mr
    global mg
    global mb
    background(0)
    stroke (mr , mg , mb , 25)
    line(l1x1 , l1y1 , l1x2 , l1y2)
    for i in range(0,11):
        k=i*50
        stroke (mr , mg , mb , (255/11) *i)
        line(l1x1 + k, l1y1 , l1x2 , l1y2 - k)
        line(l1x1 , l1y1 + k, l1x2 - k, l1y2)
        if(l1x1 == l1x2 or (l1x1 + k) == l1x2 or l1x1 == (l1x2
- k)):
            mr = random (0 ,150)
            mg = random (0 ,150)
            mb = random (0 ,150)
    l1x1 = l1x1 + flug
    l1y1 = l1y1 + flug
    l1x2 = l1x2 - flug
    l1y2 = l1y2 - flug
    if(l1y2 <0 or l1y2 > 500):
        flug=flug*(-1)
