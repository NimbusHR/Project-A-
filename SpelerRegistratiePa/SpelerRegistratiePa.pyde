
screen = 0

def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False 
    
def ThreePlayers():
    global amountofplayers
    amountofplayers = 3
    print(amountofplayers)

def FourPlayers():
    global amountofplayers
    amountofplayers = 4
    print(amountofplayers)

def FivePlayers():
    global amountofplayers
    amountofplayers = 5
    print(amountofplayers)
    
def SixPlayers():
    global amountofplayers
    amountofplayers = 6
    print(amountofplayers)
    
def SevenPlayers():
    global amountofplayers
    amountofplayers = 7
    print(amountofplayers)
    
def EightPlayers():
    global amountofplayers
    amountofplayers = 8
    print(amountofplayers)
    
def setup():
    global font, font2, players, playernames, playerReg, screen, s, s1, s2, s3 , s4, s5, s6, s7, s8, amountofplayers, img
    size(800, 500)
    font = createFont('Some Time Later.otf', 36, True)
    font2 = createFont('Some Time Later.otf', 26, True)
    players = 'Aantal spelers'
    playerReg = 'Voer je naam in'
    img = loadImage('BB.jpg')
    img.resize(800, 500)
    s = ''
    s1 = ''
    s2 = ''
    s3 = ''
    s4 = ''
    s5 = ''
    s6 = ''
    s7 = ''
    s8 = ''
    
def draw():
    global font, font2, players, playerReg, playernames, screen, s, s1, s2, s3 , s4, s5, s6, s7, s8, amountofplayers, img
    if screen == 0:
        background(img)
        textFont(font, 36)
        
        fill(255, 0, 0)
        rect(250, 35, 275, 45)
        
        fill(0)
        fill(255 , 255, 0)
        rect(275, 100, 75, 90)
        rect(275, 200, 75, 90)
        rect(275, 300, 75, 90)
        rect(420, 100, 75, 90)
        rect(420, 200, 75, 90)
        rect(420, 300, 75, 90)
        rect(590, 415, 170, 50)
        
        fill(0)
        text(players, 275, 65)
        text('3', 303, 155)
        text('4', 303, 255)
        text('5', 303, 355)
        text('6', 448, 155)
        text('7', 448, 255)
        text('8', 448, 355)
        text('Volgende', 600, 450)

        
    if screen == 1:
        background(img)
        fill(255, 255, 0)
        rect(60, 415, 130, 50)
        rect(590, 415, 170, 50)
        rect(330, 415, 120, 50)
        fill(255, 0, 0)
        rect(265, 45, 275, 45)
        fill(0, 255, 255)
        rect(265, 310, 255, 50)
        rect(250, 115, 300, 120)
        
        fill(0)
        line(250, 115, 550, 115)
        line(250, 145, 550, 145)
        line(250, 175, 550, 175)
        line(250, 205, 550, 205)
        line(250, 235, 550, 235)
        line(250, 115, 250, 235)
        line(250, 115, 250, 235)
        line(400, 115, 400, 235)
        line(550, 115, 550, 235)
        textFont(font)
        text('Terug', 75, 450)
        text('Volgende', 600, 450)
        text(playerReg, 275, 80)
        text('Reset', 340, 450)
        text(s, 275, 350)
        
        textFont(font2)
        text(s1, 280, 140)
        text(s2, 280, 170)
        text(s3, 280, 200)
        text(s4, 280, 230)
        text(s5, 430, 140)
        text(s6, 430, 170)
        text(s7, 430, 200)
        text(s8, 430, 230)
        fill(0)
        
def mousePressed():
    global font, font2, players, screen, s, s1, s2, s3 , s4, s5, s6, s7, s8, amountofplayers
    if screen == 0:
        if isMouseWithinSpace(275, 100, 75, 90):
            ThreePlayers()
        elif isMouseWithinSpace(275, 200, 75, 90):
            FourPlayers()
        elif isMouseWithinSpace(275, 300, 75, 90):
            FivePlayers()
        elif isMouseWithinSpace(420, 100, 75, 90):
            SixPlayers()
        elif isMouseWithinSpace(420, 200, 75, 90):
            SevenPlayers()
        elif isMouseWithinSpace(420, 300, 75, 90):
            EightPlayers()
        elif isMouseWithinSpace(590, 415, 170, 50):
            screen = 1
    if screen == 1:
        if isMouseWithinSpace(60, 415, 130, 50):
            screen = 0
        elif isMouseWithinSpace(330, 415, 120, 50):
            s1 = ''
            s2 = ''
            s3 = ''
            s4 = ''
            s5 = ''
            s6 = ''
            s7 = ''
            s8 = ''
        
def keyPressed():
    global s, s1, s2, s3 , s4, s5, s6, s7, s8, amountofplayers
    if key == ENTER:
        if len(s1) <= 0 and amountofplayers >= 3:
            s1 += s
            s = ''
        elif len(s2) <= 0 and amountofplayers >= 3:
            s2 += s
            s = ''
        elif len(s3) <= 0 and amountofplayers >= 3:
            s3 += s
            s = ''
        elif len (s4) <= 0 and amountofplayers >= 4:
            s4 += s
            s = ''
        elif len (s5) <= 0 and amountofplayers >= 5:
            s5 += s
            s = ''
        elif len (s6) <= 0 and amountofplayers >= 6:
            s6 += s
            s = ''
        elif len (s7) <= 0 and amountofplayers >= 7:
            s7 += s
            s = ''
        elif len (s8) <= 0 and amountofplayers >= 8:
            s8 += s
            s = ''
    elif key == BACKSPACE:
        s = s[:-1]
    elif len(s) <10:
        try:
            s += key
        except:
            pass

    
