
screen = 0


def setup():
    global screen, img, f, lente, zomer, herfst, winter, lentegeselecteerd, zomergeselecteerd, herfstgeselecteerd, wintergeselecteerd
    #achtergrond
    size(1000, 700)
    img = loadImage("wp2967401.jpg")
    img.resize(1000, 700)
    background(img)
    f = createFont("Some Time Later.otf", 16, True)
    lente = loadImage("Lente2.jpg")
    lente.resize(1000, 700)
    zomer = loadImage("Zomer.jpg")
    zomer.resize(1000, 700)
    herfst = loadImage("Herfst.jpg")
    herfst.resize(1000, 700)
    winter = loadImage("Winter.jpg")
    winter.resize(1000, 700)


def draw():
    global screen, img, f, lente, zomer, herfst, winter, lentegeselecteerd, zomergeselecteerd, herfstgeselecteerd, wintergeselecteerd
    background(img)

    
    if(screen == 0):
        textFont(f,36)
        fill(0xff)
        text("Kies een seizoen", 360, 60)
        
        
        
        
        if (mouseX > 100 and mouseX < 300 and mouseY > 100 and mouseY < 300):
            stroke(255, 0, 0)
            strokeWeight(15)
            
        else: 
            stroke(0)
            strokeWeight(2)
        
        fill(0xff)
        rect(120, 100, 200, 200)
        textFont(f,36)
        fill(0)
        text("Lente", 155, 200)
        
        
        if (mouseX > 580 and mouseX < 800) and mouseY > 100 and mouseY < 300:
            stroke(255, 0, 0)
            strokeWeight(15)
        else: 
            stroke(0)
            strokeWeight(2)
    
        fill(0xff)
        rect(620, 100, 200, 200)
        textFont(f,36)
        fill(0)
        text("Zomer", 655, 200)
        
        if (mouseX > 100 and mouseX < 300 and mouseY > 390 and mouseY < 600):
            stroke(255, 0, 0)
            strokeWeight(15)
        else: 
            stroke(0)
            strokeWeight(2)
        
        fill(0xff)
        rect(120, 400, 200, 200)
        textFont(f,36)
        fill(0)
        text("Herfst", 155, 500)
        
        if (mouseX > 580 and mouseX < 800 and mouseY > 390 and mouseY < 600):
            stroke(255, 0, 0)
            strokeWeight(15)
        else: 
            stroke(0)
            strokeWeight(2)
        
        fill(0xff)
        rect(620, 400, 200, 200)
        textFont(f,36)
        fill(0)
        text("Winter", 655, 500)
        
    if screen == 1:
        
        Lente()
            
        
    if(screen == 2):
        Zomer()
        
    if(screen == 3):
        Herfst()
   
    if(screen == 4):
        Winter()
        
    if(screen == 5):
        lentegeselecteerd()
        
    if(screen == 6):
        zomergeselecteerd()
        
    if(screen == 7):
        herfstgeselecteerd()
        
    if(screen == 8):
        wintergeselecteerd()

def Lente():
    background(lente)
    
    #knop 'ga terug'
    if mouseX > 400 and mouseX < 600 and mouseY > 600 and mouseY < 650:
        stroke(255, 0, 0)
        strokeWeight(9)
            
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(420, 600, 200, 50)
    textFont(f,30)
    fill(0)
    text("Ga terug", 455, 630)
    
    stroke(0)
    strokeWeight(2)
    fill(0xff)
    rect(420, 300, 200, 200)
    textFont(f,60)
    fill(0)
    text("Lente", 445, 400)

def Zomer():
    background(zomer)
    #knop 'ga terug'
    if mouseX > 400 and mouseX < 600 and mouseY > 600 and mouseY < 650:
        stroke(255, 0, 0)
        strokeWeight(9)
            
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(420, 600, 200, 50)
    textFont(f,30)
    fill(0)
    text("Ga terug", 455, 630)
    
    stroke(0)
    strokeWeight(2)
    fill(0xff)
    rect(420, 300, 200, 200)
    textFont(f,60)
    fill(0)
    text("Zomer", 445, 400)
    
def Herfst():
    background(herfst)
    #knop 'ga terug'
    if mouseX > 400 and mouseX < 600 and mouseY > 600 and mouseY < 650:
        stroke(255, 0, 0)
        strokeWeight(9)
            
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(420, 600, 200, 50)
    textFont(f,30)
    fill(0)
    text("Ga terug", 455, 630)
    
    stroke(0)
    strokeWeight(2)
    fill(0xff)
    rect(420, 300, 200, 200)
    textFont(f,60)
    fill(0)
    text("Herfst", 445, 400)
    
def Winter():
    background(winter)
    #knop 'ga terug'
    if mouseX > 400 and mouseX < 600 and mouseY > 600 and mouseY < 650:
        stroke(255, 0, 0)
        strokeWeight(9)
            
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(420, 600, 200, 50)
    textFont(f,35)
    fill(0)
    text("Ga terug", 455, 630)
    
    stroke(0)
    strokeWeight(2)
    fill(0xff)
    rect(420, 300, 200, 200)
    textFont(f,60)
    fill(0)
    text("Winter", 445, 400)
    
def lentegeselecteerd():
    
    textFont(f,36)
    fill(0xff)
    text("Het is nu Lente!", 360, 60)
        
        
        
    if (mouseX > 100 and mouseX < 300 and mouseY > 100 and mouseY < 300):
        stroke(255, 0, 0)
        strokeWeight(15)
            
    else: 
        stroke(0, 255, 0)
        strokeWeight(15)
        
    fill(0xff)
    rect(120, 100, 200, 200)
    textFont(f,36)
    fill(0)
    text("Lente", 155, 200)
        

    if (mouseX > 580 and mouseX < 800) and mouseY > 100 and mouseY < 300:
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0)
        strokeWeight(2)
    
    fill(0xff)
    rect(620, 100, 200, 200)
    textFont(f,36)
    fill(0)
    text("Zomer", 655, 200)
        
    if (mouseX > 100 and mouseX < 300 and mouseY > 390 and mouseY < 600):
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(120, 400, 200, 200)
    textFont(f,36)
    fill(0)
    text("Herfst", 155, 500)
        
    if (mouseX > 580 and mouseX < 800 and mouseY > 390 and mouseY < 600):
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(620, 400, 200, 200)
    textFont(f,36)
    fill(0)
    text("Winter", 655, 500)
    
def zomergeselecteerd():
    
    textFont(f,36)
    fill(0xff)
    text("Het is nu Zomer!", 360, 60)
        
        
        
    if (mouseX > 100 and mouseX < 300 and mouseY > 100 and mouseY < 300):
        stroke(255, 0, 0)
        strokeWeight(15)
            
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(120, 100, 200, 200)
    textFont(f,36)
    fill(0)
    text("Lente", 155, 200)
        

    if (mouseX > 580 and mouseX < 800) and mouseY > 100 and mouseY < 300:
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0, 255, 0)
        strokeWeight(15)
    
    fill(0xff)
    rect(620, 100, 200, 200)
    textFont(f,36)
    fill(0)
    text("Zomer", 655, 200)
        
    if (mouseX > 100 and mouseX < 300 and mouseY > 390 and mouseY < 600):
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(120, 400, 200, 200)
    textFont(f,36)
    fill(0)
    text("Herfst", 155, 500)
        
    if (mouseX > 580 and mouseX < 800 and mouseY > 390 and mouseY < 600):
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(620, 400, 200, 200)
    textFont(f,36)
    fill(0)
    text("Winter", 655, 500)
    
def herfstgeselecteerd():
    
    textFont(f,36)
    fill(0xff)
    text("Het is nu Herfst!", 360, 60)
        
        
        
    if (mouseX > 100 and mouseX < 300 and mouseY > 100 and mouseY < 300):
        stroke(255, 0, 0)
        strokeWeight(15)
            
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(120, 100, 200, 200)
    textFont(f,36)
    fill(0)
    text("Lente", 155, 200)
        

    if (mouseX > 580 and mouseX < 800) and mouseY > 100 and mouseY < 300:
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0)
        strokeWeight(2)
    
    fill(0xff)
    rect(620, 100, 200, 200)
    textFont(f,36)
    fill(0)
    text("Zomer", 655, 200)
        
    if (mouseX > 100 and mouseX < 300 and mouseY > 390 and mouseY < 600):
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0, 255, 0)
        strokeWeight(15)
        
    fill(0xff)
    rect(120, 400, 200, 200)
    textFont(f,36)
    fill(0)
    text("Herfst", 155, 500)
        
    if (mouseX > 580 and mouseX < 800 and mouseY > 390 and mouseY < 600):
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(620, 400, 200, 200)
    textFont(f,36)
    fill(0)
    text("Winter", 655, 500)
    
    
def wintergeselecteerd():
    
    textFont(f,36)
    fill(0xff)
    text("Het is nu Winter!", 360, 60)
        
        
        
    if (mouseX > 100 and mouseX < 300 and mouseY > 100 and mouseY < 300):
        stroke(255, 0, 0)
        strokeWeight(15)
            
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(120, 100, 200, 200)
    textFont(f,36)
    fill(0)
    text("Lente", 155, 200)
        

    if (mouseX > 580 and mouseX < 800) and mouseY > 100 and mouseY < 300:
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0)
        strokeWeight(2)
    
    fill(0xff)
    rect(620, 100, 200, 200)
    textFont(f,36)
    fill(0)
    text("Zomer", 655, 200)
        
    if (mouseX > 100 and mouseX < 300 and mouseY > 390 and mouseY < 600):
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0)
        strokeWeight(2)
        
    fill(0xff)
    rect(120, 400, 200, 200)
    textFont(f,36)
    fill(0)
    text("Herfst", 155, 500)
        
    if (mouseX > 580 and mouseX < 800 and mouseY > 390 and mouseY < 600):
        stroke(255, 0, 0)
        strokeWeight(15)
    else: 
        stroke(0, 255, 0)
        strokeWeight(15)
        
    fill(0xff)
    rect(620, 400, 200, 200)
    textFont(f,36)
    fill(0)
    text("Winter", 655, 500)
    
    
    
    
    

  
 
def mousePressed():
    global screen, img, lente, lentegeselecteerd
    
    #lente
    if (screen == 0 or screen == 5 or screen == 6 or screen == 7 or screen == 8) and (mouseX > 100 and mouseX < 300 and mouseY > 100 and mouseY < 300):
        screen = 1
    #knopterug
    if (screen == 1) and mouseX > 400 and mouseX < 600 and mouseY > 600 and mouseY < 650:
        screen = 5
        
    if (screen == 2) and mouseX > 400 and mouseX < 600 and mouseY > 600 and mouseY < 650:
        screen = 6
        
    if (screen == 3) and mouseX > 400 and mouseX < 600 and mouseY > 600 and mouseY < 650:
        screen = 7
        
    if (screen == 4) and mouseX > 400 and mouseX < 600 and mouseY > 600 and mouseY < 650:
        screen = 8

    #zomer
    if (screen == 0 or screen == 5 or screen == 6 or screen == 7 or screen == 8) and (mouseX > 580 and mouseX < 800) and mouseY > 100 and mouseY < 300:
        screen = 2
    #herfst    
    if (screen == 0 or screen == 5 or screen == 6 or screen == 7 or screen == 8) and (mouseX > 100 and mouseX < 300 and mouseY > 390 and mouseY < 600):
        screen = 3
    #winter    
    if (screen == 0 or screen == 5 or screen == 6 or screen == 7 or screen == 8) and (mouseX > 580 and mouseX < 800 and mouseY > 390 and mouseY < 600):
        screen = 4

    #if (screen == 1 or screen == 2 or screen == 3 or screen == 4) and mouseX > 400 and mouseX < 600 and mouseY > 600 and mouseY < 650:
        #screen = 0
        
    
    
