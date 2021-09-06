l =0
a =0
def setup():
    size(500,250)
def draw():
    background( 191,164,201)
    fill( 77,142,219)
    ellipse (l ,height/2.0,50,60)
    fill(77,142,219)
    ellipse(a, height/3.5, 60,70)
    if l > height:
        l = 0
    else: l = map(second(),0,59,0, height)
    if a > height:
        a = 0
    else: 
        a = map(minute(),0,59,0,height)
        global l
        global a
