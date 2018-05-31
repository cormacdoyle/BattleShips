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
gridname1= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


randomnum1=(random.randint(0, 10))
randomnum2=(random.randint(0, 10))
randomnum3=(random.randint(0, 10))
randomnum4=(random.randint(0, 9))
randomnum5=(random.randint(0, 10))
randomnum6=(random.randint(0, 8))
randomnum7=(random.randint(0, 10))
randomnum8=(random.randint(0, 10))
randomnum9=(random.randint(0, 9))
randomnum10=(random.randint(0, 10))
randomnum11=(random.randint(0, 8))
randomnum12=(random.randint(0, 10))

enemyship_listx = [50,100,150,200,250,300,350,400,450,500,550]
enemyship_listy = [50,100,150,200,250,300,350,400,450,500,550]

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

enemyship_listx = [50,100,150,200,250,300,350,400,450,500,550]
enemyship_listy = [50,100,150,200,250,300,350,400,450,500,550]

shipxcoor= [ship1smallx, ship2mediumx, ship3largex,ship4largex, (ship4largex) + 50, (ship4largex) + 100, (ship5mediumx), (ship5mediumx)+50, ship6smallx]
shipycoor = [ship1smally,ship2mediumy, (ship2mediumy) + 50, ship3largey, (ship3largey)+50, (ship3largey)+100, ship4largey, ship5mediumy, ship6smally]


hitcoorx = [50,100,150,200,250,300,350,400,450,500,550]
hitcoory = [50,100,150,200,250,300,350,400,450,500,550]

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

    pygame.draw.rect(win, shiptestcolour, (ship1smallx, ship1smally, 50, 50))  # enemy first ship blends in
    pygame.draw.rect(win, shiptestcolour, (ship2mediumx, ship2mediumy, 50, 100))
    pygame.draw.rect(win,shiptestcolour, (ship3largex, ship3largey, 50, 150) )
    pygame.draw.rect(win, shiptestcolour, (ship4largex,ship4largey,50, 150))
    pygame.draw.rect(win, shiptestcolour, (ship5mediumx,ship5mediumy, 50, 100))
    pygame.draw.rect(win, shiptestcolour, (ship6smallx,ship6smally, 50, 50))

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
        for i in range(0, 8):
            if (hitcoorx[new_variablex] == shipxcoor[i]) and (hitcoory[new_variabley] == shipycoor[i]):
                pygame.draw.rect(win, white, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))
            else:
                pygame.draw.rect(win, red, (hitcoorx[new_variablex], hitcoory[new_variabley], 50, 50))
        print(hitcoorx[new_variablex], hitcoory[new_variabley])
        print(shipxcoor[i], shipycoor[i])

    for i in range(50,551,50):   # grid system for left side
        pygame.draw.line(win, black, (i,50), (i,550), 5)
        pygame.draw.line(win, black, (50,i), (550,i), 5)

    win.blit(textsurface1, (400, 65))
    win.blit(textsurface2, (875, 65))

    pygame.display.update()
