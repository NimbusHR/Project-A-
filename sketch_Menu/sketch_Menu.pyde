#This is how I imported the sound. I installed an extra library name minim.
add_library('minim')

minim = Minim(this)




#In the setup are all the important factors that I'm using in this program. This you will find in globals.
def setup():
    global img, font, minim, player
    
    #This is the size of the screen. It's the same size as the background image.
    size(1024, 768)
    
    #This is the code for the background. You put this code here so you can be able to use it in the draw function.
    img = loadImage("Bikinibottom.jpg")
    background(img)
    font = createFont("Arial", 46)
    
     #This is the code for the sound.
    minim = Minim(this)
    player = minim.loadFile("spongebobmuziek2.mp3")
    player.play()

#In draw we use globals again so the program knows what's important.
#In draw we put everything that we want to display on the screen.    
def draw():
    global img, font, minim, player
    background(img)
    
    #This is so the text Menu can appear on the screen.
    fill(0)
    textSize(46)
    text("Menu", 450, 100)
    

    #This is so the text score board can appear on the screen in a rectangle.
    #The coordinates for the rectangle.(x, y, width, height).
    fill(255)
    rect(300, 120, 400, 50)
    fill(0)
    textSize(30)
    text("Score board", 399, 170)
        
    #This is so the text seizoenen can appear on the screen in a rectangle.
    #The coordinates for the rectangle.(x, y, width, height).
    fill(255)
    rect(299, 220, 400, 50)
    fill(0)
    textSize(30)
    text("Seizoenen", 420, 270)

        
    
     #This is so the text trivia vragen can appear on the screen in a rectangle.
    #The coordinates for the rectangle.(x, y, width, height).
    fill(255)
    rect(299, 320, 400, 50)
    fill(0)
    textSize(30)
    text("Trivia vragen", 420, 370)
   
             
    #This is so the text challenges can appear on the screen in a rectangle.
    #The coordinates for the rectangle.(x, y, width, height).
    fill(255)
    rect(299, 420, 400, 50)
    fill(0)
    textSize(30)
    text("Challenges", 420, 470)
