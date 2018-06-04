import pygame
import random

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1050, 550))  # set display to a size of 1000x500 pixels

pygame.display.set_caption("Battleships")  # name this screen "Battleships"


# colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
shiptestcolour = (0, 50, 255)
shipfinalcolour = (0, 200, 255)
# fonts
myfont = pygame.font.SysFont('arial bold', 30)
textsurface1 = myfont.render('Your score: ', False, (0, 255, 0))  # add in score keeping variable
textsurface2 = myfont.render('Enemy score: ', False, (0, 255, 0))
textsurface3 = myfont.render('A      B      C      D      E      F      G      H      I      J', False, black)

enemyship_listx = [50,100,150,200,250,300,350,400,450,500]
enemyship_listy = [50,100,150,200,250,300,350,400,450,500]

randomnum1=(random.randint(0, 8))
randomnum2=(random.randint(0, 8))
randomnum3=(random.randint(0, 8))
randomnum4=(random.randint(0, 7))
randomnum5=(random.randint(0, 8))
randomnum6=(random.randint(0, 6))
randomnum7=(random.randint(0, 8))
randomnum8=(random.randint(0, 8))
randomnum9=(random.randint(0, 6))
randomnum10=(random.randint(0, 8))
randomnum11=(random.randint(0, 6))
randomnum12=(random.randint(0, 8))

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

enemyship_listx = [50,100,150,200,250,300,350,400,450,500]
enemyship_listy = [50,100,150,200,250,300,350,400,450,500]

shipxcoor= [ship1smallx, ship2mediumx, ship3largex, ship4largex, ship5mediumx, ship6smallx]
shipycoor= [ship1smally, ship2mediumy, ship3largey, ship4largey, ship5mediumy, ship6smally ]

hitcoorx = [50,100,150,200,250,300,350,400,450,500]
hitcoory = [50,100,150,200,250,300,350,400,450,500]

x = 0 #x used for x axis not to be confused with other x axis variables
y = 0 #y is used for y axis not to be confused with other y axis variables

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when the player presses the Exit button in the top right the window will close
            run = False

    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

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

    if keys[pygame.K_SPACE]:
        new_variablex = x
        new_variabley = y

        if enemyship_listx[new_variablex] == ship1smallx and enemyship_listy[new_variabley] == ship1smally:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship2mediumx and enemyship_listy[new_variabley] == ship2mediumy:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship2mediumx and enemyship_listy[new_variabley] == ship2mediumy + 50:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship3largex and enemyship_listy[new_variabley] == ship3largey:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship3largex and enemyship_listy[new_variabley] == ship3largey + 50:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship3largex and enemyship_listy[new_variabley] == ship3largey + 100:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship4largex and enemyship_listy[new_variabley] == ship4largey:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship4largex + 50 and enemyship_listy[new_variabley] == ship4largey:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship4largex + 100 and enemyship_listy[new_variabley] == ship4largey:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship5mediumx and enemyship_listy[new_variabley] == ship5mediumy:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship5mediumx + 50 and enemyship_listy[new_variabley] == ship5mediumy:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        elif enemyship_listx[new_variablex] == ship6smallx and enemyship_listy[new_variabley] == ship6smally:
            pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

        else:
            pygame.draw.rect(win, red, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))

    for i in range(50,551,50):   # grid system for left side
        pygame.draw.line(win, black, (i,50), (i,550), 5)
        pygame.draw.line(win, black, (50,i), (550,i), 5)

    win.blit(textsurface1, (400, 65))
    win.blit(textsurface2, (875, 65))
    win.blit(textsurface3, (75, 10))

    pygame.display.update()