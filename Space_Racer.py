from pygame_functions import *
import random
import time

def startScreen():

    screenSize(1400, 800)

    #Set up introduction screen

    setBackgroundImage("intro_background.png")

    makeMusic("Start.mp3")
    playMusic(loops=-1)

    Title = makeSprite("Space_Racer_Title.png")
    moveSprite(Title, 320, 30)
    showSprite(Title)

    directionLabel = makeLabel("Use the directional keys to move your spaceship!", 25, 640, 600, "red", "Comic Sans MS")
    showLabel(directionLabel)

    purposeLabel = makeLabel("Avoid obstacles, survive, and earn points!", 25, 680, 640, "red", "Comic Sans MS")
    showLabel(purposeLabel)

    entryLabel = makeLabel("Press SPACEBAR to start or Q to quit.", 25, 700, 680, "red", "Comic Sans MS")
    showLabel(entryLabel)

    intro = True

    while intro:

        if keyPressed("space"):
            intro = False
            break
        if keyPressed("q"):
            quit()

    hideSprite(Title)
    hideLabel(directionLabel)
    hideLabel(purposeLabel)
    hideLabel(entryLabel)


def gameLoop():

    #Setting up screen size, background images, and clock

    setBackgroundImage("Space.png")

    pause(300)

    #Background music

    makeMusic("Theme.wav")
    playMusic(loops=-1)

    #Setting a scoreboard

    scoreTitle = makeLabel("SCORE ", 45, 830, 20, "white", "Comic Sans MS")
    showLabel(scoreTitle)

    scoreBox = makeLabel("0", 45, 1010, 20, "white", "Comic Sans MS")
    showLabel(scoreBox)

    score = 0
    nextScoreBonus = clock()  # Store the current time. This is used to indicate when the next score bonus will happen

    #Creating sprite and alternate image for sprite

    Rocket = makeSprite("Rocket_no_thrust.png")
    addSpriteImage(Rocket, "Rocket_thrust.png")
    addSpriteImage(Rocket, "Rocket_crash.png")
    showSprite(Rocket)
    thrustSound = makeSound("Thruster.wav")
    crashSound = makeSound("Explode.wav")

    #Starting position of spaceship

    xPos = 500
    yPos = 300
    xSpeed = 0
    ySpeed = 0
    moveSprite(Rocket, xPos, yPos)

    #Asteroid functions with random speed and position

    asteroids = [] # Creates a list called asteroids
    for x in range(1):
        thisAsteroid = makeSprite("Asteroid.png")

        thisAsteroid.x = random.randint(600, 1400)
        thisAsteroid.y = random.randint(400, 800)
        moveSprite(thisAsteroid, thisAsteroid.x, thisAsteroid.y)

        thisAsteroid.xspeed = random.randint(-3,3)
        thisAsteroid.yspeed = random.randint(-3,3)
        showSprite(thisAsteroid)

        asteroids.append(thisAsteroid) #This adds thisAsteroid to the list made at the top

    ufo = [] # Creates a list called ufo
    for x in range(1):
        thisUfo = makeSprite("UFO.png")

        thisUfo.x = random.randint(600, 1400)
        thisUfo.y = random.randint(400, 800)
        moveSprite(thisUfo, thisUfo.x, thisUfo.y)

        thisUfo.xspeed = random.randint(-3,3)
        thisUfo.yspeed = random.randint(-3,3)
        showSprite(thisUfo)

        ufo.append(thisUfo) #This adds thisUfo to the list made at the top

    satellite = [] # Creates a list called satellite
    for x in range(1):
        thisSatellite = makeSprite("Satellite.png")

        thisSatellite.x = random.randint(200, 1400)
        thisSatellite.y = random.randint(600, 800)
        moveSprite(thisSatellite, thisSatellite.x, thisSatellite.y)

        thisSatellite.xspeed = random.randint(-3,3)
        thisSatellite.yspeed = random.randint(-3,3)
        showSprite(thisSatellite)

        satellite.append(thisSatellite) #This adds thisSatellite to the list made at the top

    #Defining key press variable and altering position and speed of Rocket

    while True:
        if keyPressed("up"):
            transformSprite(Rocket, 360, 1)
            changeSpriteImage(Rocket, 1)
            playSound(thrustSound)
            ySpeed -= 1 #Negative speed moves up the screen

        elif keyPressed("down"):
            transformSprite(Rocket, 180, 1)
            changeSpriteImage(Rocket, 1)
            playSound(thrustSound)
            ySpeed += 1 #Positive speed moves down the screen

        elif keyPressed("right"):
            transformSprite(Rocket, 90,1)
            changeSpriteImage(Rocket, 1)
            playSound(thrustSound)
            xSpeed += 1

        elif keyPressed("left"):
            transformSprite(Rocket, -90,1)
            changeSpriteImage(Rocket, 1)
            playSound(thrustSound)
            xSpeed -= 1

        else:
            changeSpriteImage(Rocket, 0)
            stopSound(thrustSound)

    #Looping function to appear back on screen if flown out of screen range

        xPos += xSpeed
        if xPos > 1400:
            xPos = -150
        elif xPos < -150:
            xPos = 1400

        yPos += ySpeed
        if yPos > 800:
            yPos = -150
        elif yPos < -150:
            yPos = 800

        moveSprite(Rocket, xPos, yPos)

        #This moves the asteroid by its speed

        for thisAsteroid in asteroids:
            thisAsteroid.x += thisAsteroid.xspeed
        if thisAsteroid.x > 1400:
            thisAsteroid.x = 0
        elif thisAsteroid.x < 0:
            thisAsteroid.x = 1400

        thisAsteroid.y += thisAsteroid.yspeed
        if thisAsteroid.y > 800:
            thisAsteroid.y = 0
        elif thisAsteroid.y < 0:
            thisAsteroid.y = 800

        moveSprite(thisAsteroid, thisAsteroid.x, thisAsteroid.y)


    #This moves the ufo by its speed

        for thisUfo in ufo:
            thisUfo.x += thisUfo.xspeed
        if thisUfo.x > 1400:
            thisUfo.x = 0
        elif thisUfo.x < 0:
            thisUfo.x = 1400

        thisUfo.y += thisUfo.yspeed
        if thisUfo.y > 800:
            thisUfo.y = 0
        elif thisUfo.y < 0:
            thisUfo.y = 800

        moveSprite(thisUfo, thisUfo.x, thisUfo.y)

    #This moves the satellite by its speed

        for thisSatellite in satellite:
            thisSatellite.x += thisSatellite.xspeed
        if thisSatellite.x > 1400:
            thisSatellite.x = 0
        elif thisSatellite.x < 0:
            thisSatellite.x = 1400

        thisSatellite.y += thisSatellite.yspeed
        if thisSatellite.y > 800:
            thisSatellite.y = 0
        elif thisSatellite.y < 0:
            thisSatellite.y = 800

        moveSprite(thisSatellite, thisSatellite.x, thisSatellite.y)

        # update the score label
        if clock() > nextScoreBonus:  # if we have passed the bonus time
            nextScoreBonus += 2000  # set the next bonus time to 2 seconds later
            score += 10  # add to the score
            changeLabel(scoreBox, str(score))  # update the label

        tick(50)

    #End game if rocket collides with other objects

        if touching (Rocket,thisAsteroid):
            changeSpriteImage(Rocket, 2)
            stopSound(thrustSound)
            playSound(crashSound)
            pause(1000)
            break

        if touching (Rocket, thisUfo):
            changeSpriteImage(Rocket, 2)
            stopSound(thrustSound)
            playSound(crashSound)
            pause(1000)
            break

        if touching (Rocket, thisSatellite):
            changeSpriteImage(Rocket, 2)
            stopSound(thrustSound)
            playSound(crashSound)
            pause(1000)
            break

    restartLabel = makeLabel("You Crashed! (Press C to CONTINUE or E to EXIT)", 40, 225, 250, "red", "Comic Sans MS")
    showLabel(restartLabel)

    restart = True

    while restart:

        if keyPressed("c"):
            restart = False
            moveLabel(restartLabel, 8000, 8000)
            moveLabel(scoreBox, 8000, 8000)
            hideAll()
            return gameLoop()
        if keyPressed("e"):
            quit()


startScreen()
gameLoop()


