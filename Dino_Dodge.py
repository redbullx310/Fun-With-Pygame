from pygame_functions import *
import random

# This function will spawn an egg at a random x location between 100 and 1000, then return the reference of the newly created egg
def spawnEgg():
    egg = makeSprite("Images/flyer_egg.png")
    egg.x = random.randint(100, 1000)
    egg.y = 340
    moveSprite(egg, egg.x, egg.y)
    showSprite(egg)
    return egg  # return the variable egg to the caller

def startScreen():

    screenSize(1024, 465)

    #Set up introduction screen

    setBackgroundImage("Images/dino_dodge_intro_background.jpg")

    makeMusic("Sounds/dino_dodge_intro.mp3")
    playMusic(loops=-1)

    Title = makeSprite("Images/dino_dodge_title.png")
    moveSprite(Title, 350, 150)
    showSprite(Title)

    character = makeSprite("Images/dino1.png")
    moveSprite(character, 320, 150)
    showSprite(character)

    goal = makeSprite("Images/flyer_egg.png")
    moveSprite(goal, 570, 180)
    showSprite(goal)

    directionLabel = makeLabel("Use directional RIGHT and LEFT keys to move and SPACE to hide!", 25, 200, 350, "yellow")
    showLabel(directionLabel)

    purposeLabel = makeLabel("Outsmart the raptors and collect as many eggs as you can!", 25, 245, 380, "yellow")
    showLabel(purposeLabel)

    entryLabel = makeLabel("Press P to play or Q to quit.", 25, 370, 410, "yellow")
    showLabel(entryLabel)

    intro = True

    while intro:

        if keyPressed("p"):
            intro = False
            break
        if keyPressed("q"):
            quit()

    hideSprite(Title)
    hideLabel(directionLabel)
    hideLabel(purposeLabel)
    hideLabel(entryLabel)
    hideSprite(character)
    hideSprite(goal)


def game_Loop():
    setBackgroundImage("Images/Prehistoric_background.png")

    makeMusic("Sounds/Dino_dodge_theme.mp3")
    playMusic(loops=-1)

    # Setting a scoreboard

    score = 0

    scoreTitle = makeLabel("EGGS COLLECTED ", 25, 0, 12, "yellow", "Comic Sans MS")
    showLabel(scoreTitle)

    scoreBox = makeLabel(str(int(score)), 25, 230, 12, "yellow", "Comic Sans MS")
    showLabel(scoreBox)

    gust = makeSound("Sounds/hiding_sound.wav")

    wind = makeSprite("Images/gust_of_wind.png")

    die = makeSprite("Images/die.png")

    caught = makeSound("Sounds/caught.wav")

    collect = makeSound("Sounds/collect.wav")

    width = 5

    bushes = makeSprite("Images/hiding_bush.png")
    moveSprite(bushes, 0, 290)
    showSprite(bushes)

    bushes1 = makeSprite("Images/hiding_bush.png")
    moveSprite(bushes1, 300, 290)
    showSprite(bushes1)

    bushes2 = makeSprite("Images/hiding_bush.png")
    moveSprite(bushes2, 550, 290)
    showSprite(bushes2)

    # Dino movement with speed and position

    dino = []  # Creates a list called dino
    for x in range(1):
        thisDino = makeSprite("Images/dino1.png")
        addSpriteImage(thisDino, "Images/dino2.png")  # Add extra images. They are stored in the Sprite object
        addSpriteImage(thisDino, "Images/dino3.png")  # but not displayed yet
        addSpriteImage(thisDino, "Images/dino4.png")
        addSpriteImage(thisDino, "Images/dino5.png")
        addSpriteImage(thisDino, "Images/dino6.png")
        addSpriteImage(thisDino, "Images/dino7.png")
        addSpriteImage(thisDino, "Images/dino8.png")
        addSpriteImage(thisDino, "Images/dino9.png")
        addSpriteImage(thisDino, "Images/dino9.png")
        addSpriteImage(thisDino, "Images/dino10.png")

        thisDino.x = random.randint(0, 0)
        thisDino.y = random.randint(305, 305)
        moveSprite(thisDino, thisDino.x, thisDino.y)

        thisDino.xspeed = 7
        thisDino.xspeed1 = -5
        thisDino.yspeed = random.randint(0, 0)
        showSprite(thisDino)

        dino.append(thisDino)

    # Raptor movement with speed and position

    raptor = []  # Creates a list called raptor
    for x in range(1):
        thisRaptor = makeSprite("Images/raptor1.png")
        addSpriteImage(thisRaptor, "Images/raptor2.png")
        addSpriteImage(thisRaptor, "Images/raptor3.png")
        addSpriteImage(thisRaptor, "Images/raptor4.png")
        addSpriteImage(thisRaptor, "Images/raptor5.png")
        addSpriteImage(thisRaptor, "Images/raptor6.png")

        thisRaptor.x = random.randint(200, 200)
        thisRaptor.y = random.randint(410, 410)
        moveSprite(thisRaptor, thisRaptor.x, thisRaptor.y)

        thisRaptor.xspeed = 7
        thisRaptor.yspeed = random.randint(0, 0)
        showSprite(thisRaptor)

        raptor.append(thisRaptor)  # This adds thisRaptor to the list made at the top

    # Second raptor movement with speed and position

    raptor2 = []
    for x in range(1):
        thisRaptor2 = makeSprite("Images/raptor7.png")
        addSpriteImage(thisRaptor2, "Images/raptor8.png")
        addSpriteImage(thisRaptor2, "Images/raptor9.png")
        addSpriteImage(thisRaptor2, "Images/raptor10.png")
        addSpriteImage(thisRaptor2, "Images/raptor11.png")
        addSpriteImage(thisRaptor2, "Images/raptor12.png")

        thisRaptor2.x = random.randint(500, 500)
        thisRaptor2.y = random.randint(310, 310)
        moveSprite(thisRaptor2, thisRaptor2.x, thisRaptor2.y)

        thisRaptor2.xspeed = -7
        thisRaptor2.yspeed = random.randint(0, 0)
        showSprite(thisRaptor2)

        raptor2.append(thisRaptor2)

    # Create a list of eggs, spawn the starting egg and add it to the list of eggs
    eggs = []
    thisEgg = spawnEgg()  # creates a variable 'thisEgg', and sets it equal to the egg variable created and returned from the spawnEgg function
    eggs.append(thisEgg)

    # Countdown to game start

    countdown3 = makeSprite("Images/countdown3.png")
    moveSprite(countdown3, 460, 150)
    showSprite(countdown3)
    pause(1000)
    hideSprite(countdown3)

    countdown2 = makeSprite("Images/countdown2.png")
    moveSprite(countdown2, 460, 150)
    showSprite(countdown2)
    pause(1000)
    hideSprite(countdown2)

    countdown1 = makeSprite("Images/countdown1.png")
    moveSprite(countdown1, 460, 150)
    showSprite(countdown1)
    pause(1000)
    hideSprite(countdown1)

    countdown0 = makeSprite("Images/countdown0.png")
    moveSprite(countdown0, 380, 150)
    showSprite(countdown0)
    pause(1000)
    hideSprite(countdown0)

    #Key press functions for dino and frame movement

    nextFrame = clock()
    frame = 0
    mass = 6
    velocity = 6
    jumping = False
    while True:

        if clock() > nextFrame:  # We only animate our character every 80ms.
            frame = (frame + 1) % 4  # There are 4 frames of animation in each direction
            nextFrame += 80  # so the modulus 8 allows it to loop


        if nextFrame:
            changeSpriteImage(thisRaptor, 0 * 5 + frame)
            changeSpriteImage(thisRaptor2, 0 * 5 + frame)

        #This moves dino by its speed with x position boundaries

        if keyPressed("right"):
            for thisDino in dino:
                thisDino.x += thisDino.xspeed
            if thisDino.x > 950:
                thisDino.x = 950 - width
            elif thisDino.x < 0:
                thisDino.x = 0

            thisDino.y += thisDino.yspeed
            if thisDino.y > 355:
                thisDino.y = 0
            elif thisDino.y < 0:
                thisDino.y = 355

            moveSprite(thisDino, thisDino.x, thisDino.y)
            changeSpriteImage(thisDino, 0 * 4 + frame)
            scrollBackground(-2, 0)

        if keyPressed("left"):
            for thisDino in dino:
                thisDino.x += thisDino.xspeed1
            if thisDino.x > 950:
                thisDino.x = 0 + width
            elif thisDino.x < 0:
                thisDino.x = 0

            thisDino.y += thisDino.yspeed
            if thisDino.y > 355:
                thisDino.y = 0
            elif thisDino.y < 0:
                thisDino.y = 355

            transformSprite(thisDino, 355, 1)
            moveSprite(thisDino, thisDino.x, thisDino.y)
            changeSpriteImage(thisDino, 1 * 4 + frame)
            scrollBackground(2, 0)

        # Press the up arrow key to initiate a jump
        if keyPressed("up") and thisDino.y == 305:
            jumping = True

        # this will run once the user pressed the up arrow key and the jumping variable is set to True
        if jumping:
            force = mass * velocity                       # a basic physics formula for calculating force
            thisDino.y = thisDino.y - force               # apply the force to the dino (subtracts the calculated force from its current y position, moving it up)
            moveSprite(thisDino, thisDino.x, thisDino.y)  # move the dino up
            velocity = velocity - 1                       # subtract 1 from the velocity, so the next force calculation will be smaller. This will eventually reach a
                                                          # negative number range, which begins the descention of the dino (bringing him back down)
            if thisDino.y >= 305:                         # If the ground is reached after jumping, reset everything
                thisDino.y = 305                          # Make sure dino is back to the right y position
                moveSprite(thisDino, thisDino.x, thisDino.y)
                velocity = 6                              # reset the velocity
                jumping = False                           # set jumping to False

        if keyPressed("SPACE") and thisDino.x < 232:
            changeSpriteImage(thisDino, 9)
            moveSprite(thisDino, thisDino.x, 408)
            moveSprite(wind, thisDino.x, thisDino.y)
            showSprite(wind)
            pause(30)
            playSound(gust, loops=0)
            hideSprite(wind)

        if keyPressed("SPACE") and thisDino.x > 232:
            changeSpriteImage(thisDino, 10)
            moveSprite(thisDino, thisDino.x, 408)
            moveSprite(wind, thisDino.x, thisDino.y)
            showSprite(wind)
            pause(30)
            playSound(gust, loops=0)
            hideSprite(wind)

        # This moves the raptor by its speed

        for thisRaptor in raptor:
            thisRaptor.x += thisRaptor.xspeed
        if thisRaptor.x > 1024:
            thisRaptor.x = 0
        elif thisRaptor.x < 0:
            thisRaptor.x = 1024

        thisRaptor.y += thisRaptor.yspeed
        if thisRaptor.y > 410:
            thisRaptor.y = 0
        elif thisRaptor.y < 0:
            thisRaptor.y = 410

        moveSprite(thisRaptor, thisRaptor.x, thisRaptor.y)

        # This moves the raptor2 by its speed

        for thisRaptor2 in raptor2:
            thisRaptor2.x += thisRaptor2.xspeed
        if thisRaptor2.x > 1024:
            thisRaptor2.x = 0
        elif thisRaptor2.x < 0:
            thisRaptor2.x = 1024

        thisRaptor2.y += thisRaptor2.yspeed
        if thisRaptor2.y > 410:
            thisRaptor2.y = 0
        elif thisRaptor2.y < 0:
            thisRaptor2.y = 410

        moveSprite(thisRaptor2, thisRaptor2.x, thisRaptor2.y)

        # Collision detection

        if touching(thisEgg, thisDino):
            moveSprite(thisEgg, random.randint(0, 1000), random.randint(340, 340))
            playSound(collect)
            score += 1
            changeLabel(scoreBox, str(score))  # update the label

        if touching(thisDino, thisRaptor):
            moveSprite(die, thisDino.x, thisDino.y)
            hideSprite(thisDino)
            showSprite(die)
            playSound(caught)
            stopMusic()
            pause(1000)
            break

        if touching(thisDino, thisRaptor2):
            moveSprite(die, thisDino.x, thisDino.y)
            hideSprite(thisDino)
            showSprite(die)
            playSound(caught)
            stopMusic()
            pause(1000)
            break

    # Restart or quit if caught

    restartLabel = makeLabel("You were caught! (Press C to CONTINUE or Q to QUIT)", 25, 300, 12, "red")
    showLabel(restartLabel)

    restart = True

    while restart:

        if keyPressed("c"):
            moveLabel(restartLabel, 8000, 8000)
            moveLabel(scoreBox, 8000, 8000)
            hideAll()
            return game_Loop()
        if keyPressed("q"):
            quit()


startScreen()
game_Loop()
endWait()
