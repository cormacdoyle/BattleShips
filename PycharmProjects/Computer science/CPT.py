import pygame
import time
import random

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1000, 500))  # set display to a size of 1000x500 pixels

pygame.display.set_caption("Battleships")  # name this screen "Battleships"

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

myfont = pygame.font.SysFont('arial bold', 30)
textsurface1 = myfont.render('Your score: ', False, (0, 255, 0))  # add in score keeping variable
textsurface2 = myfont.render('Enemy score: ', False, (0, 255, 0))

x = 50
y = 50
width = 50
height = 50
vel = 50

x1 = 50
x2 = 50

ship1smallxrand = random.randint(0, 9)
ship1smallyrand = random.randint(0, 9)
ship1smallx = ship1smallxrand * 50
ship1smally = ship1smallyrand * 50

ship2mediumxrand = random.randint(0, 9)
ship2mediumyrand = random.randint(0, 9)
ship2mediumx = ship2mediumxrand * 50
ship2mediumy = ship2mediumyrand * 50

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when the player presses the Exit button in the top right the window will close
            run = False

    playershots = []

    ship1 = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel - width:
        x = x - vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x = x + vel
    if keys[pygame.K_UP] and y > vel - height:
        y = y - vel
    if keys[pygame.K_DOWN] and y < 500 - height:
        y = y + vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0),
                     (x, y, width, height))  # player hit selector moves by 50 pixels each time is 50x50
    pygame.draw.rect(win, (0, 200, 255), (0, 0, 500, 500))  # left side player hit side and enemy ship locations
    pygame.draw.rect(win, (0, 100, 255), (500, 0, 500, 500))  # right side player ships and enemy hit
    pygame.draw.rect(win, (0, 50, 255), (
    ship1smallx, ship1smally, 50, 50))  # enemy first ship blends in with background coordinates decided using random
    pygame.draw.rect(win, (0, 50, 255), (ship2mediumx, ship2mediumy, 50, 100))
    pygame.draw.rect(win, (0, 0, 0), ((ship1[0] // 50) * 50, (ship1[1] // 50) * 50, 50, 50))  # using mouse create ships
    pygame.draw.rect(win, (255, 0, 0),
                     (x, y, width, height))  # player hit selector moves by 50 pixels each time is 50x50
    win.blit(textsurface1, (350, 15))
    win.blit(textsurface2, (825, 15))
    pygame.display.update()


