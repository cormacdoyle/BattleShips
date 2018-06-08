import pygame
import random
import time

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1050, 550))  # set display to a size of 1000x500 pixels

pygame.display.set_caption("Battleships")  # name this screen "Battleships"

#myfont.render('Your score: ', False, (0, 255, 0))  # add in score keeping variable
#textsurface2 = myfont.render('Enemy score: ', False, (0, 255, 0))
#textsurface3 = myfont.render('A      B      C      D      E      F      G      H      I      J', False, black)
shotlistx = []
shotlisty = []

# colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
shiptestcolour = (0, 50, 255)
shipfinalcolour = (0, 200, 255)

myfont = pygame.font.SysFont('arial bold', 30)


def message_to_screen(msg, colour, coorx, coory):
    screen_text = myfont.render(msg, True, colour)
    win.blit(screen_text, [coorx, coory])

def level_one():
    keys = pygame.key.get_pressed()

    enemyship_listx = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    enemyship_listy = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

    randomnum1 = (random.randint(0, 8))
    randomnum2 = (random.randint(0, 8))
    randomnum3 = (random.randint(0, 8))
    randomnum4 = (random.randint(0, 7))
    randomnum5 = (random.randint(0, 8))
    randomnum6 = (random.randint(0, 6))
    randomnum7 = (random.randint(0, 8))
    randomnum8 = (random.randint(0, 8))
    randomnum9 = (random.randint(0, 6))
    randomnum10 = (random.randint(0, 8))
    randomnum11 = (random.randint(0, 6))
    randomnum12 = (random.randint(0, 8))

    ship1smallx = enemyship_listx[randomnum1]
    ship1smally = enemyship_listy[randomnum2]
    ship2mediumx = enemyship_listx[randomnum3]
    ship2mediumy = enemyship_listy[randomnum4]
    ship3largex = enemyship_listx[randomnum5]
    ship3largey = enemyship_listy[randomnum6]
    ship4largex = enemyship_listx[randomnum7]
    ship4largey = enemyship_listy[randomnum8]
    ship5mediumx = enemyship_listx[randomnum9]
    ship5mediumy = enemyship_listy[randomnum10]
    ship6smallx = enemyship_listx[randomnum11]
    ship6smally = enemyship_listy[randomnum12]

    shipxcoor = [ship1smallx, ship2mediumx, ship3largex, ship4largex, ((ship4largex) + 50), ((ship4largex) + 100),
                 (ship5mediumx), ((ship5mediumx) + 50), ship6smallx]
    shipycoor = [ship1smally, ship2mediumy, ((ship2mediumy) + 50), ship3largey, ((ship3largey) + 50),
                 ((ship3largey) + 100), ship4largey, ship5mediumy, ship6smally]

    hitcoorx = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    hitcoory = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

    run = True
    gameOver = False

    while run:
        pygame.time.delay(100)

        while gameOver == True:
            win.fill(black)
            # if player wins:
            #message_to_screen("Congratulations, you have completed level 1 Press V to go to level 2 or Q to quit.", red)
            #pygame.display.update()
            # elif player loses:
            message_to_screen("Oops looks like you've been beaten you sailor!  Press C to play again or Q to quit.",
                              red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run == False
                        gameOver == False
                    elif event.key == pygame.K_c:
                        level_one()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when Exit button in the top right is pressed the window will close
                run = False

        x = 0  # x used for x axis not to be confused with other x axis variables
        y = 0  # y is used for y axis not to be confused with other y axis variables

        mouse = pygame.mouse.get_pos()

        if keys[pygame.K_a] and x>0:
            x = x - 1
            hitcoorx[x]
        if keys[pygame.K_d] and x < 9:
            x = x + 1
            hitcoorx[x]
        if keys[pygame.K_w] and y >0:
            y = y - 1
            hitcoory[x]
        if keys[pygame.K_s] and y< 9:
            y = y + 1
            hitcoory[y]

        win.fill(shipfinalcolour)

        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                new_variablex = x
                new_variabley = y

                shotlistx.append(new_variablex)
                shotlisty.append(new_variabley)

        pygame.draw.rect(win, (0, 100, 255), (550, 50, 500, 500))  # right side player ships and enemy hit

        pygame.draw.rect(win, shipfinalcolour, (ship1smallx, ship1smally, 50, 50))  # enemy first ship blends in
        pygame.draw.rect(win, shipfinalcolour, (ship2mediumx, ship2mediumy, 50, 100))
        pygame.draw.rect(win, shipfinalcolour, (ship3largex, ship3largey, 50, 150) )
        pygame.draw.rect(win, shipfinalcolour, (ship4largex,ship4largey,150, 50))
        pygame.draw.rect(win, shipfinalcolour, (ship5mediumx,ship5mediumy, 100, 50))
        pygame.draw.rect(win, shipfinalcolour, (ship6smallx,ship6smally, 50, 50))

        pygame.draw.rect(win, black, ((mouse[0] // 50) * 50, (mouse[1] // 50) * 50, 50, 50))  # using mouse create ships

        if keys[pygame.K_RIGHT]:
            pygame.draw.rect(win, black, (mouse[0]//50 * 50 + 50, mouse[1] // 50 *50,50, 50))
        if keys[pygame.K_LEFT]:
            pygame.draw.rect(win, black, (mouse[0]//50 * 50 - 50, mouse[1]// 50 * 50, 50, 50))
        if keys[pygame.K_UP]:
            pygame.draw.rect(win, black, (mouse[0]// 50 * 50, mouse[1]//50 * 50 - 50, 50 , 50))
        if keys[pygame.K_DOWN]:
            pygame.draw.rect(win, black, (mouse[0]//50*50, mouse[1]//50 *50 +50, 50, 50))
        pygame.draw.rect(win, black,(hitcoorx[x], hitcoory[y], 50, 50))  # player hit selector moves by 50 pixels eachtime is 50x50

        for i in range(0, len(shotlistx - 1)):
            for n in range(0, len(enemyship_listx - 1)):
                if enemyship_listx[n] == shotlistx[i]:
                    pygame.draw.rect(win, white, shotlistx[i], shotlisty[i], 50, 50)
                else:
                    pygame.draw.rect(win, red, shotlistx[i], shotlisty[i], 50, 50)

        for i in range(50,551,50):   # grid system for left side
            pygame.draw.line(win, black, (i,50), (i,550), 5)
            pygame.draw.line(win, black, (50,i), (550,i), 5)

        message_to_screen("Your Score", green, 400, 65)
        message_to_screen("Enemy score", green, 875, 65)


def game_intro():
    keys = pygame.key.get_pressed()
    intro = True
    while intro:
        pygame.time.delay(100)

        win.fill(white)

        message_to_screen("Welcome to Battleships", green, 200, 200)
        message_to_screen("Place your ships and try to hit the enemies!", black, 200, 300)
        message_to_screen("Press SPACE to continue into Level 1 and Q to quit.", red, 200, 400)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when Exit button in the top right is pressed the window will close
                quit()      

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_SPACE]:
                    level_one()
                elif keys[pygame.K_q]:
                    intro = False
                    pygame.quit()
                    quit()

        pygame.display.update()

    pygame.display.update()


game_intro()

pygame.quit()
quit()
