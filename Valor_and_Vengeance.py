from pygame_functions import *


def startScreen():

    screenSize(1024, 698)

    setBackgroundImage("Images/Intro_Background.jpg")

    makeMusic("Sounds/Main_Menu_Theme.wav")
    playMusic(loops=-1)

    title = makeSprite("Images/Title.png")
    moveSprite(title, 110, 220)
    showSprite(title)

    subtext1 = makeSprite("Images/Subtext1.png")
    moveSprite(subtext1, 260, 330)
    showSprite(subtext1)

    subtext2 = makeSprite("Images/Subtext2.png")
    moveSprite(subtext2, 220, 350)
    showSprite(subtext2)

    subtext3 = makeSprite("Images/Subtext3.png")
    moveSprite(subtext3, 200, 370)
    showSprite(subtext3)

    subtext4 = makeSprite("Images/Subtext4.png")
    moveSprite(subtext4, 280, 560)
    showSprite(subtext4)

    newGame = makeSprite("Images/New_Game.png")
    moveSprite(newGame, 325, 400)
    showSprite(newGame)

    sword1 = makeSprite("Images/Sword_Icon_New_Game.png")
    moveSprite(sword1, 260, 450)
    showSprite(sword1)
    sword2 = makeSprite("Images/Sword_Icon_New_Game1.png")
    moveSprite(sword2, 570, 450)
    showSprite(sword2)

    intro = True

    while intro:

        if spriteClicked(newGame):
            intro = False
            break
        if keyPressed("q"):
            quit()

    hideSprite(title)
    hideSprite(subtext1)
    hideSprite(subtext2)
    hideSprite(subtext3)
    hideSprite(subtext4)
    hideSprite(newGame)
    hideSprite(sword1)
    hideSprite(sword2)
    stopMusic()


def gameLoop():

    def leveling():
        lvl = 1
        xp = 0
        lvlNext = 25

        pStr = 0
        pEnd = 0
        pDex = 0

        while xp >= lvlNext:
            lvl += 1
            xp = xp - lvlNext
            lvlNext = round(lvlNext * 1.5)
        print("Level: ", lvl)
        print("Exp: ", xp)
        print("Next: ", lvlNext)

    width = 30

    setBackgroundImage(["Images/Kingdom_Background.jpg"])

    makeMusic("Sounds/Village_Theme.wav")
    playMusic(loops=-1)

    flag = makeSprite("Images/flag.png")
    moveSprite(flag, 790, 400)
    showSprite(flag)

    flag2 = makeSprite("Images/flag2.png")
    flag3 = makeSprite("Images/flag3.png")
    guard = makeSprite("Images/Guard.png")
    guard2 = makeSprite("Images/Guard2.png")
    commander = makeSprite("Images/Guard_Commander.png")
    talk = makeSprite("Images/Talk_Box.png")
    iman = makeLabel("Commander Iman: Welcome knight...", 14, 400, 600, "red")
    iman1 = makeLabel("(Press C to continue)", 14, 440, 620, "red")
    iman2 = makeLabel("Orc raiders have taken Queen Zafira!", 14, 405, 600, "red")
    iman3 = makeLabel("Please rescue her in the forest!", 14, 420, 600, "red")
    queen_danger = makeSprite("Images/Queen Zafira_Danger.png")
    wall = makeSprite("Images/Wall_Forest.png")
    wall2 = makeSprite("Images/Wall_Forest2.png")
    gate = makeSprite("Images/Gate.png")
    loot = makeSprite("Images/Treasure_Box_Locked.png")
    saved = makeSprite("Images/Exclaimation.jpg")
    talk2 = makeSprite("Images/Talk_Box.png")
    zafira = makeLabel("Queen Zafira: Thank you, Hero!", 14, 415, 600, "red")
    zafira1 = makeLabel("I must make my return to the castle.", 14, 410, 600, "red")
    zafira2 = makeLabel("Please return when you are able.", 14, 415, 600, "red")
    zafira3 = makeLabel("We must restore peace to the kingdom!", 14, 400, 600, "red")
    zafira0 = makeLabel("(Press C to continue)", 14, 440, 620, "red")
    battle = makeSprite("Images/Player_Character_Battle_Stance.png")
    orcbattle = makeSprite("Images/Orc_Battle_Stance.png")
    talk3 = makeSprite("Images/Talk_Box.png")
    orc1 = makeLabel("Your Queen is mine. Prepare to die!", 14, 410, 600, "red")
    orc0 = makeLabel("(Press C to continue)", 14, 440, 620, "red")
    offense = makeSprite("Images/Attack_Icon.png")
    attack = makeSprite("Images/Player_Character_Attack_Right1.png")
    orcattack = makeSprite("Images/Orc_Attack_Right1.png")

    player = []  # Creates a list called player
    for x in range(1):
        thisPlayer = makeSprite("Player_Character_Walk_Down1.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Down2.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Down3.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Down4.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Down5.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Down6.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Down7.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Down8.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Down9.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Up1.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Up2.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Up3.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Up4.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Up5.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Up6.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Up7.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Up8.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Up9.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Right1.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Right2.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Right3.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Right4.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Right5.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Right6.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Right7.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Right8.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Right9.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Left1.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Left2.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Left3.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Left4.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Left5.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Left6.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Left7.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Left8.png")
        addSpriteImage(thisPlayer, "Images/Player_Character_Walk_Left9.png")

        thisPlayer.x = 400
        thisPlayer.y = 450

        moveSprite(thisPlayer, thisPlayer.x, thisPlayer.y)
        showSprite(thisPlayer)

        player.append(thisPlayer)

        orc = [] # Creates a list called orc
        for x in range(1):
            thisOrc = makeSprite("Images/Orc_Walk_Left1.png")
            addSpriteImage(thisOrc, "Images/Orc_Walk_Left2.png")
            addSpriteImage(thisOrc, "Images/Orc_Walk_Left3.png")
            addSpriteImage(thisOrc, "Images/Orc_Walk_Left4.png")
            addSpriteImage(thisOrc, "Images/Orc_Walk_Left5.png")
            addSpriteImage(thisOrc, "Images/Orc_Walk_Left6.png")
            addSpriteImage(thisOrc, "Images/Orc_Walk_Left7.png")
            addSpriteImage(thisOrc, "Images/Orc_Walk_Left8.png")
            addSpriteImage(thisOrc, "Images/Orc_Walk_Left9.png")

            thisOrc.x = 755
            thisOrc.y = 900

            thisOrc.xspeed = 0
            thisOrc.yspeed = 0

            moveSprite(thisOrc, thisOrc.x, thisOrc.y)

            orc.append(thisOrc)

        queen = []  # Creates a list called queen
        for x in range(1):
            thisQueen = makeSprite("Images/Queen_Walk_Right1.png")
            addSpriteImage(thisQueen, "Images/Queen_Walk_Right2.png")
            addSpriteImage(thisQueen, "Images/Queen_Walk_Right3.png")

            thisQueen.x = 950
            thisQueen.y = 600

            thisQueen.xspeed = -1
            thisQueen.yspeed = 0

            moveSprite(thisQueen, thisQueen.x, thisQueen.y)

            queen.append(thisQueen)

            arrow = []  # Creates a list called arrow
            for x in range(1):
                thisArrow = makeSprite("Images/Arrow1.png")
                addSpriteImage(thisArrow, "Images/Arrow2.png")
                addSpriteImage(thisArrow, "Images/Arrow3.png")
                addSpriteImage(thisArrow, "Images/Arrow4.png")
                addSpriteImage(thisArrow, "Images/Arrow5.png")
                addSpriteImage(thisArrow, "Images/Arrow6.png")
                addSpriteImage(thisArrow, "Images/Arrow7.png")
                addSpriteImage(thisArrow, "Images/Arrow8.png")
                addSpriteImage(thisArrow, "Images/Arrow9.png")

                thisArrow.x = 680
                thisArrow.y = 385

                moveSprite(thisArrow, thisArrow.x, thisArrow.y)

                arrow.append(thisArrow)

        # Key press functions for player and frame movement

        nextFrame = clock()
        frame = 0

        while True:

            if clock() > nextFrame:  # We only animate our character every 80ms.
                frame = (frame + 1) % 8  # There are 9 frames of animation in each direction
                nextFrame += 80  # so the modulus 8 allows it to loop

            if nextFrame:
                changeSpriteImage(thisArrow, 0 * 8 + frame)

            if keyPressed("right"):
                for thisPlayer in player:
                    moveSprite(thisPlayer, thisPlayer.x, thisPlayer.y)
                    changeSpriteImage(thisPlayer, 2 * 9 + frame)
                    thisPlayer.x += 2
                    if thisPlayer.x > 800 - width:
                        thisPlayer.x = 800 - width
                    elif thisPlayer.x < 0:
                        thisPlayer.x = 800 - width

            if keyPressed("left"):
                for thisPlayer in player:
                    moveSprite(thisPlayer, thisPlayer.x, thisPlayer.y)
                    changeSpriteImage(thisPlayer, 3 * 9 + frame)
                    thisPlayer.x -= 2
                    if thisPlayer.x > 800:
                        thisPlayer.x = 0 + width
                    elif thisPlayer.x < 0:
                        thisPlayer.x = 0

            if keyPressed("up"):
                for thisPlayer in player:
                    moveSprite(thisPlayer, thisPlayer.x, thisPlayer.y)
                    changeSpriteImage(thisPlayer, 1 * 9 + frame)
                    thisPlayer.y -= 2
                    if thisPlayer.y < 300:
                        thisPlayer.y = 330 - width

            if keyPressed("down"):
                for thisPlayer in player:
                    moveSprite(thisPlayer, thisPlayer.x, thisPlayer.y)
                    changeSpriteImage(thisPlayer, 0 * 9 + frame)
                    thisPlayer.y += 2
                    if thisPlayer.y > 630:
                        thisPlayer.y = 610 + width

            # This moves the orc by its speed

            for thisOrc in orc:
                thisOrc.x += thisOrc.xspeed
            if thisOrc.x > 0:
                thisOrc.x = 730 + width
            elif thisOrc.x < 0:
                thisOrc.x = 730 + width

            thisOrc.y += thisOrc.yspeed
            if thisOrc.y > 0:
                thisOrc.y = 580 + width
            elif thisOrc.y < 0:
                thisOrc.y = 580 + width

            moveSprite(thisOrc, thisOrc.x, thisOrc.y)

            # This moves the queen by her speed

            for thisQueen in queen:
                thisQueen.x += thisQueen.xspeed
            if thisQueen.x > 0:
                thisQueen.x = 790
            elif thisQueen.x < 0:
                thisQueen.x = 790

            thisQueen.y += thisQueen.yspeed
            if thisQueen.y > 0:
                thisQueen.y = 608
            elif thisQueen.y < 0:
                thisQueen.y = 608

            moveSprite(thisQueen, thisQueen.x, thisQueen.y)

            # Collision and switching scenes

            if touching(thisPlayer, flag):
                stopMusic()
                pause(500)
                hideSprite(flag)
                setBackgroundImage("Images/Castle_Throne.png")
                makeMusic("Sounds/Castle_Theme.mp3")
                playMusic(loops=-1)
                moveSprite(thisPlayer, 130, 490)
                thisPlayer.x = 130
                thisPlayer.y = 490
                moveSprite(flag2, 80, 490)
                showSprite(flag2)
                moveSprite(guard, 690, 540)
                showSprite(guard)
                moveSprite(guard2, 670, 450)
                showSprite(guard2)
                moveSprite(commander, 640, 490)
                showSprite(commander)
            if touching(thisPlayer, commander):
                moveSprite(talk, 360, 540)
                showSprite(talk)
                showLabel(iman)
                showLabel(iman1)
                thisPlayer.x = 616
                if keyPressed("c"):
                    moveLabel(iman, -5000, -5000)
                    moveLabel(iman1, -6000, 4000)
                    showLabel(iman2)
                    pause(2000)
                    moveLabel(iman2, 60000, 60000)
                    showLabel(iman3)

            if not touching(thisPlayer, commander):
                hideSprite(talk)
                hideLabel(iman)
                hideLabel(iman1)
                hideLabel(iman2)
                hideLabel(iman3)

            if touching(thisPlayer, flag2):
                stopMusic()
                pause(500)
                makeMusic("Sounds/Village_Theme.wav")
                playMusic(loops=-1)
                moveSprite(commander, 9000, 9000)
                hideSprite(flag2)
                moveSprite(flag2, 10000, 10000)
                hideSprite(guard)
                hideSprite(guard2)
                hideSprite(commander)
                setBackgroundImage(["Images/Kingdom_Background.jpg"])
                moveSprite(flag, 790, 400)
                showSprite(flag)
                moveSprite(flag3, 250, 270)
                showSprite(flag3)
                moveSprite(thisPlayer, 680, 410)
                thisPlayer.x = 680
                thisPlayer.y = 410

            if touching(thisPlayer, flag3):
                stopMusic()
                makeMusic("Sounds/Forest_Theme.mp3")
                playMusic(loops=-1)
                pause(500)
                hideSprite(flag)
                moveSprite(flag, -5000, -5000)
                hideSprite(flag3)
                moveSprite(flag3, 4800, 4800)
                setBackgroundImage(["Images/Forest.png"])
                moveSprite(thisPlayer, 0, 500)
                thisPlayer.x = 0
                thisPlayer.y = 500
                moveSprite(queen_danger, 950, 600)
                showSprite(queen_danger)
                showSprite(thisOrc)
                moveSprite(wall, 805, 665)
                showSprite(wall)
                moveSprite(wall2, 805, 405)
                showSprite(wall2)
                moveSprite(gate, 735, 605)
                showSprite(gate)

            if touching(thisPlayer, thisOrc):
                thisPlayer.x = 745
                moveSprite(talk3, 360, 540)
                showSprite(talk3)
                showLabel(orc0)
                showLabel(orc1)
                if keyPressed("c"):
                    stopMusic()
                    moveLabel(orc0, 2845, 2845)
                    moveLabel(orc1, 2845, 2845)
                    hideSprite(wall)
                    hideSprite(wall2)
                    hideSprite(gate)
                    hideSprite(queen_danger)
                    setBackgroundImage("Images/Battle_Background.png")
                    makeMusic("Sounds/Battle_Theme.wav")
                    playMusic(loops=-1)
                    hideSprite(thisPlayer)
                    moveSprite(battle, 250, 425)
                    showSprite(battle)
                    hideSprite(thisOrc)
                    moveSprite(orcbattle, 685, 425)
                    showSprite(orcbattle)
                    moveSprite(offense, 445, 570)
                    showSprite(offense)
                if spriteClicked(offense):
                    showSprite(thisArrow)
                if spriteClicked(orcbattle):
                    hideSprite(thisArrow)
                    hideSprite(battle)
                    moveSprite(attack, 250, 425)
                    showSprite(attack)
                    pause(300)
                    hideSprite(attack)
                    showSprite(battle)
                    pause(2000)
                    hideSprite(orcbattle)
                    moveSprite(orcattack, 685, 425)
                    showSprite(orcattack)
                    pause(300)
                    hideSprite(orcattack)
                    showSprite(orcbattle)




                 #   tick(2000)
                  #  killSprite(thisOrc)
                   # moveSprite(gate, 1024, 1024)
                    #hideSprite(gate)
                    #pause(1000)
                    #moveSprite(saved, 955, 520)
                    #showSprite(saved)
                    #stopMusic()
                    #queen_saved = makeSound("Queen_Saved.wav")
                    #playSound(queen_saved, loops=0)
                    #pause(500)
                    #hideSprite(saved)
                    #pause(500)
                    #rush = makeSprite("gust_of_wind.png")
                    #moveSprite(rush, 910, 580)
                    #hideSprite(queen_danger)
                    #showSprite(rush)
                    #dash = makeSound("hiding_sound.wav")
                    #playSound(dash, loops=0)
                    #pause(100)
                    #hideSprite(rush)
                    #showSprite(thisQueen)

            if touching(thisPlayer, thisQueen):
                moveSprite(talk2, 360, 540)
                showSprite(talk2)
                showLabel(zafira)
                showLabel(zafira0)
                if keyPressed("c"):
                    moveLabel(zafira0, 8256, 8256)
                    moveLabel(zafira, -5000, -5000)
                    showLabel(zafira1)
                    pause(2000)
                    moveLabel(zafira1, 60000, 60000)
                    showLabel(zafira2)
                    pause(2000)
                    moveLabel(zafira2, 90000, 90000)
                    showLabel(zafira3)

            if not touching(thisPlayer, thisQueen):
                hideSprite(talk2)
                hideLabel(zafira)
                hideLabel(zafira1)
                hideLabel(zafira2)
                hideLabel(zafira3)
                hideLabel(zafira0)




startScreen()
gameLoop()
endWait()
