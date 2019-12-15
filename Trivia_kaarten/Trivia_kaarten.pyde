def setup():
    global imgBack, trivia, index, trivia_ans, indexans, randomtrivia, imgRoll, imgQuit, imgAnswer, Font
    
    size(1000,700)
    imgBack = loadImage("DoosA4.jpg")
    imgRoll = loadImage("Roll.jpg")
    imgQuit = loadImage("Quit.jpg")
    imgAnswer = loadImage("Answer.jpg")
    
    trivia = ["Spongebob is een van de weinige personages in de serie die...", "Hoeveel sproeten heeft spongebob op elke wang?", "Welke van de vier genoemde dingen zit niet in de krabburger? A.kaas, B.Paddenstoelen, C.Uien, D.Mosterd", 
              "Wat voor telefoon heeft Spongebob?", "Spongebob leeft in een ronde ananas.Wat is er dus raar aan de binnenkant van zijn huis?", "Spongebob is bang voor het donker en wat nog meer?",
               "Wie heeft Spongebob bedacht?", "Wat is de voornaam van Plankton?", "Hoeveel ledematen heeft Octo in totaal?", "Hoe heet de vrouw van Plankton?", 
               "Hoeveel slakken heeft Spongebob in totaal gehad?", "Wat is de volgorde van de huizen in Spongebob's straat, als je aan de linkerkant begint?", "Welk personage in Spongebob draagt geen shirt?", 
               "Waar komt Sandy de eekhoorn origineel vandaan?", "Van welke dingen houdt meneer Krabs het meest?", "Hoe heet het restaurant van Plankton?", "Wat dacht Patrick dat de vaarschool van mevrouw Puff was?", 
               "In de aflevering de Grote Slakken Race. Wat is de naam van de slak die Octo koopt?", "Welk personage in Spongebob is een kreeft?", "Wie is de beste vriend van Spongebob?", 
               "Welke kleur zijn de ogen van Spongebob?", "Hoe ziet de haar van Octo eruit?", "Hoeveel boventanden van Patrick kan je zien als die lacht?",
               "Waar woon Patrick?", "Welk instrument speelt Octo?", "Welke baan heeft Spongebob bij de Krokante Krab? A.frituurkok, B.Chef, C.Ober", 
               "Van wie is Patrick familie van?", "Noem 1 hobby van Patrick:"]
    
    trivia_ans = ["Vingers heeft.", "3", "B.Paddenstoelen", "Een schelp", "Het heeft hoeken.", "Clowns",
                  "Stephen Hillenburg", "Sheldon", "6", "Karen", 
                  "3(Garry, Larry en Jerry)", "Patrick's huis, Octo's huis, Spongebob's huis", "Patrick", 
                  "Texas", "Geld en Parel", "De Maatemmer", "Spaanse les. Patrick Zei: Vaarschool? Ik dacht dat dit Spaans was.",
                  "Shelly", "Larry", "Patrick", 
                  "Blauw", "Hij heeft geen haar!", "1",
                  "Onder een steen", "Clarinet", "A.Frituurkok", 
                  "Gerrit, ze hebben dezelfde grootouders.", "Bellenblazen,Kwallen vangen, Kwijlen, Omgaan met Spongebob, Eten, Slapen"]
    
    index = int(random(len(trivia)))
    indexans = index
    
    randomtrivia = trivia[index]
    
    Font = createFont("KrabbyPatty.ttf", 32)
    
def draw():
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
        text("Back",815,615,100,75)
    else:
        stroke(0)
        strokeWeight(2)
        fill(192,192,192)
        rect(800,600,100,75)
        fill(0)
        text("Back",815,615,100,75)  
    
    #Answer Button
    if button(100,600,100,75) == True:
        stroke(0)
        strokeWeight(2)
        fill(0)
        rect(100,600,125,75)
        fill(255,255,255)
        textSize(26)
        text("Answer",115,615,100,75)
    else:
        stroke(0)
        strokeWeight(2)
        fill(192,192,192)
        rect(100,600,125,75)
        fill(0)
        textSize(26)
        text("Answer",115,615,100,75)

    
    #trivia veld
    fill(192,192,192)
    rect(200,100,600,150)
    
    if len(trivia) == 1:
            refresh()
    
    #trivia font,kleur etc.
    randomtrivia
    fill(0)
    text(randomtrivia,210,105,590,290)
    
    
    
    
def button(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False 

def triviarandom():
    global index, trivia, randomtrivia,indexans
    del trivia[index]
    del trivia_ans[indexans]
    index = int(random(len(trivia)))
    indexans = index
    randomtrivia = trivia[index]
    fill(0)
    text(randomtrivia,200,100,600,300)
    
def refresh():
    global trivia, trivia_ans
    trivia = ["Spongebob is een van de weinige personages in de serie die...", "Hoeveel sproeten heeft spongebob op elke wang?", "Welke van de vier genoemde dingen zit niet in de krabburger? A.kaas, B.Paddenstoelen, C.Uien, D.Mosterd", 
              "Wat voor telefoon heeft Spongebob?", "Spongebob leeft in een ronde ananas.Wat is er dus raar aan de binnenkant van zijn huis?", "Spongebob is bang voor het donker en wat nog meer?",
               "Wie heeft Spongebob bedacht?", "Wat is de voornaam van Plankton?", "Hoeveel ledematen heeft Octo in totaal?", "Hoe heet de vrouw van Plankton?", 
               "Hoeveel slakken heeft Spongebob in totaal gehad?", "Wat is de volgorde van de huizen in Spongebob's straat, als je aan de linkerkant begint?", "Welk personage in Spongebob draagt geen shirt?", 
               "Waar komt Sandy de eekhoorn origineel vandaan?", "Van welke dingen houdt meneer Krabs het meest?", "Hoe heet het restaurant van Plankton?", "Wat dacht Patrick dat de vaarschool van mevrouw Puff was?", 
               "In de aflevering de Grote Slakken Race. Wat is de naam van de slak die Octo koopt?", "Welk personage in Spongebob is een kreeft?", "Wie is de beste vriend van Spongebob?", 
               "Welke kleur zijn de ogen van Spongebob?", "Hoe ziet de haar van Octo eruit?", "Hoeveel boventanden van Patrick kan je zien als die lacht?",
               "Waar woon Patrick?", "Welk instrument speelt Octo?", "Welke baan heeft Spongebob bij de Krokante Krab? A.frituurkok, B.Chef, C.Ober", 
               "Van wie is Patrick familie van?", "Noem 1 hobby van Patrick:"]
    
    trivia_ans = ["Vingers heeft.", "3", "B.Paddenstoelen", "Een schelp", "Het heeft hoeken.", "Clowns",
                  "Stephen Hillenburg", "Sheldon", "6", "Karen", 
                  "3(Garry, Larry en Jerry)", "Patrick's huis, Octo's huis, Spongebob's huis", "Patrick", 
                  "Texas", "Geld en Parel", "De Maatemmer", "Spaanse les. Patrick Zei: Vaarschool? Ik dacht dat dit Spaans was.",
                  "Shelly", "Larry", "Patrick", 
                  "Blauw", "Hij heeft geen haar!", "1",
                  "Onder een steen", "Clarinet", "A.Frituurkok", 
                  "Gerrit, ze hebben dezelfde grootouders.", "Bellenblazen,Kwallen vangen, Kwijlen, Omgaan met Spongebob, Eten, Slapen"]
    
def trivia_answer():
    global randomtrivia,indexans
    fill(255,255,255)
    rect(200,100,600,150)
    indexans = index
    randomtrivia = trivia_ans[indexans]
    fill(0)
    text(randomtrivia,200,100,600,300)

def mouseClicked():
    if button(800,600,100,75) == True:
        exit()
    if button(100,600,100,75) == True:
        trivia_answer()


    
