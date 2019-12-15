begin = 0
duration = 60
time = 60

def setup():
    global imgBack, challenges, index, Font
    
    size(1000,700)
    imgBack = loadImage("DoosA4.jpg")
    
    challenges = ["Zeg een zin in een gek accent en laat iemand anders het raden.", "Zing een lied met minstens 1 slok water in je mond.", "Laat een gekke dansmove zien.", "Doe een impressie van Octo.", "Lach zoals Patrick.", "Lach zoals Spongebob.",
               "Geef een inspirerende speech over geld.", "Doe de worm op de grond.", "Vertel een leuke grap waarbij minstens 1 persoon lacht.", "Vouw succesvol zonder je duimen te gebruiken een papier 3x doormidden.", 
               "Probeer voor een minuut je lach in te houden terwijl de rest gekke dingen doet.", "Probeer om 10 seconden op 1 been je balans te houden.", "Eet iets heel zuurs en probeer daarbij je gezicht stil te houden.", 
               "Doe 5 push-ups terwijl je zeurt zoals Octo.", "Doe 10 squats met het enthousiasme van Spongebob.", "Zoek een tongbreker op en lees deze foutloos op.", "Noem 5 bekende plekken uit Spongebob op.", "Doe een dier na en laat iemand het raden.", 
               "Neurie een bekend lied en laat iemand het raden."]
    
    index = int(random(len(challenges)))
    
    begin = millis()
    Font = createFont("KrabbyPatty.ttf", 32)
    
    
def draw():
    global beginTime, time, begin, duration
    background(imgBack)
    textSize(28)
    textFont(Font)
    
    #Quit Button
    if button(800,600,100,75) == True:
        stroke(0)
        strokeWeight(2)
        fill(0)
        rect(800,600,100,75)
        fill(255,255,255)
        text("Back",805,615,100,75)
    else:
        stroke(0)
        strokeWeight(2)
        fill(192,192,192)
        rect(800,600,100,75)
        fill(0)
        text("Back",805,615,100,75)    
    
    #challenge veld
    stroke(0)
    strokeWeight(2)
    fill(192,192,192)
    rect(200,100,600,150)
    
    #challange font,kleur etc.
    randomchallenge = challenges[index]
    fill(0)
    text(randomchallenge,210,105,590,290)
    
    if len(challenges) == 1:
        refresh()
    
    #Timer veld
    if (time > 0):
        time = duration - (millis() - begin)/1000
        fill(192,192,192)
        rect(85,305,130,95)
        textSize(75)
        fill(0)
        text(time, 150, 380)
        textAlign(CENTER)
    if time == 0:
        fill(192,192,192)
        rect(100,335,190,65)
        textSize(40)
        fill(0)
        text("Times Up!", 195, 380)
        
    
def button(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False 

def challenge():
    global index, challenges
    del challenges[index]
    index = int(random(len(challenges)))
    print(index)
    
def refresh():
    global challenges
    challenges = ["Zeg een zin in een gek accent en laat iemand anders het raden.", "Zing een lied met minstens 1 slok water in je mond.", "Laat een gekke dansmove zien.", "Doe een impressie van Octo.", "Lach zoals Patrick.", "Lach zoals Spongebob.",
               "Geef een inspirerende speech over geld.", "Doe de worm op de grond.", "Vertel een leuke grap waarbij minstens 1 persoon lacht.", "Vouw succesvol zonder je duimen te gebruiken een papier 3x doormidden.", 
               "Probeer voor een minuut je lach in te houden terwijl de rest gekke dingen doet.", "Probeer om 10 seconden op 1 been je balans te houden.", "Eet iets heel zuurs en probeer daarbij je gezicht stil te houden.", 
               "Doe 5 push-ups terwijl je zeurt zoals Octo.", "Doe 10 squats met het enthousiasme van Spongebob.", "Zoek een tongbreker op en lees deze foutloos op.", "Noem 5 bekende plekken uit Spongebob op.", "Doe een dier na en laat iemand het raden.", 
               "Neurie een bekend lied en laat iemand het raden."]
    

def mouseClicked():
    global duration
    if button(800,600,100,75) == True:
        exit()

            


        

    
    
