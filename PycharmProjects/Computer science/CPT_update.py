import pygame, random



#  Colours
light_green = (34,177,76)
dark_green = (68,119,60)
black = (0,0,0)
shiptestcolour = (0, 50, 255)
shipfinalcolour = (0, 200, 255)

#  Font
pygame.font.init()
big_title_font = pygame.font.Font(None, 80)
intro_title_font = pygame.font.Font(None, 140)

#  text files
pygame.font.init()
myfont = pygame.font.Font(None, 36)
mybigfont = pygame.font.Font(None, 40)
text1 = myfont.render("Change Ship Size", True, (255, 255, 255))
text2 = mybigfont.render("+", True, (255, 255, 255))
text2_1 = mybigfont.render("-", True, (255, 255, 255))
text3 = myfont.render("Ship Orientation", True, (255, 255, 255))
text4 = myfont.render("Up", True, (255, 255, 255))
text5 = myfont.render("User Score", True, (255, 255, 255))
text6 = myfont.render("Computer Score", True, (255, 255, 255))
text7 = myfont.render("Sideways", True, (255, 255, 255))

text10 = mybigfont.render("Ships Left: ", True, (255, 255, 255))


#  Intro Screen click logic
def mouse_selction(x,y):
    if (x > 100 and x < 500) and (y > 200 and y < 400):
        level_one(True)
        return False
    if (x > 700 and x < 1100) and (y > 200 and y < 400):
        print("highscore")
    if (x > 525 and x < 675) and (y > 450 and y < 550):
        quit()


#  Loads intro screen
def intro_screen(state):
    #  Sets display window
    intro_display = pygame.display.set_mode([1200,600])
    #  Makes mouse visible
    pygame.mouse.set_visible(True)
    while state:
        #  Background
        pygame.draw.rect(intro_display, light_green , (0,0,1200,600))
        #  Tiles
        pygame.draw.rect(intro_display, dark_green, (100, 200, 400, 200))
        pygame.draw.rect(intro_display, dark_green, (700, 200, 400, 200))
        pygame.draw.rect(intro_display, dark_green, (525, 450, 150, 100))
        #  Text
        txt_start = big_title_font.render("START", True, black)
        txt_highscore = big_title_font.render("HIGHSCORE", True, black)
        txt_quit = big_title_font.render("QUIT", True, black)
        txt_battleships = intro_title_font.render("Battleships_1.0", True, dark_green)
        #  Blit
        intro_display.blit(txt_start, (200,275))
        intro_display.blit(txt_highscore, (730, 275))
        intro_display.blit(txt_quit, (530, 475))
        intro_display.blit(txt_battleships, (250,50))
        #  UI
        for event in pygame.event.get():
            #  Quit button
            if event.type == pygame.QUIT:
                quit()
            #  If there is a mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                #  Unpack two variables from pygame.mouse function x and y position of mouse
                x,y = pygame.mouse.get_pos()
                #  Activate click logic
                state = mouse_selction(x,y)
        #  Updates screen
        pygame.display.update()

#  Function controls logic for computer to choose tiles to click
def computer_move():
    x_length = 0
    y_length = 0
    x = random.randint(0,9)
    y = random.randint(0,9)
    y_or_x = random.randint(0,1)
    if y_or_x:
        x_length = random.randint(0,3)
    else:
        y_length = random.randint(0, 3)
    return x,y,x_length,y_length

#  Function controls tip on screen at each moment during game
def tutorial(state):
    if state == 0:
        return "Place your ships!"
    if state == 1:
        return "Choose where to bomb!"
    if state == 2:
        return "Direct Hit!, User Scored 1 point"
    if state == 3:
        return "Miss, try again!"
    if state == 4:
        return "Already a ship placed here"
    if state == 5:
        return "Computer's turn!"
    if state == 6:
        return "Direct Hit!, Computer Scored 1 point"


#  Loads all paramteres for level one
def level_one(state):

    clock = pygame.time.Clock()

    #  Starts tip at tip #1
    tut_count = 0
    #  Allows game inputs to be locked, True is unlocked, False is locked
    game_lock = True
    #  Sets display parameters
    display = pygame.display.set_mode([1280, 720])
    #  Mouse is visible
    pygame.mouse.set_visible(True)
    #  Level 1 allows you to use 5 ships
    ships_left = 5
    #  Unpacks x and y position of mouse to variables l and k
    l, k = pygame.mouse.get_pos()
    #  Set ship size to 1 block
    ship_size_x = 1
    ship_size_y = 1
    #  x_or_y is a variable that controls the orientation of the ship , 0 is sideways 1 is up
    x_or_y = 0
    #  Sets coords of first grid for x axis
    grid_coords = [100,150,200,250,300,350,400,450,500,550,600,-50]
    #  Sets coords of second grid for x axis
    computer_grid_coords = [740, 790, 840, 890, 940, 990, 1040,1090, 1140,1190]
    #  Sets inital state to an off screen position
    x_boat_coords = [11,11,11,11,11,11]
    y_boat_coords = [11,11,11,11,11,11]
    #  Sets initial to a length of one
    x_boat_length = [1,1,1,1,1,1]
    y_boat_length = [1,1,1,1,1,1]
    #  Intializes score
    ai_score = 0
    user_score = 0
    #  intializes Shot counter
    shots_left = 15
    #  User grid is a 10x10 multi dimensional array which uses integers to denote the status of each block in the grid
    user_grid = [
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    ]
    computer_grid = [
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
        [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    ]
    while True:
        #  Iterated through user grid
        for i in range(9):
            for x in range(9):
                #  The integer 1 denotes a ship position
                if user_grid[i][x] == 1:
                    pygame.draw.rect(display,black, (grid_coords[i],grid_coords[x], 50,50))
                #  The integer 2 denotes a missed shot
                if user_grid[i][x] == 2:
                    pygame.draw.rect(display, (255,0,0), (grid_coords[i],grid_coords[x],50,50))
                #  The integer 3 denotes a hit ship
                if user_grid[i][x] == 3:
                    pygame.draw.rect(display, (0, 255, 0), (grid_coords[i], grid_coords[x], 50, 50))

        for i in range(9):
            for x in range(9):
                #  The integer 2 will denote a missed shot
                if computer_grid[i][x] == 2:
                    pygame.draw.rect(display, (255, 0, 0), (computer_grid_coords[i],grid_coords[x], 50, 50))
                #  The integer 3 will denote a hit ship
                if computer_grid[i][x] == 3:
                    pygame.draw.rect(display, (0, 255, 0), (computer_grid_coords[i], grid_coords[x], 50, 50))

        pygame.display.update()
        #  Ship size is a single intgeer and thus must be multiplied by 50 to fit to the 50 x 50 block size
        ship_x = 50 * ship_size_x
        ship_y = 50 * ship_size_y
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #  Cast the postion of the mouse to variabels l and k
                l, k = pygame.mouse.get_pos()
                l = (l * 50) // 50
                k = (k * 50) // 50
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #  If the mouse is clicked on the increase ship size tile
                if (l > 20 and l < 85) and (k > 650 and k < 700):
                    #  Checks upper and lower bounds of size of ship
                    if (ship_size_x > 0 and ship_size_x < 4) and (ship_size_y > 0 and ship_size_y < 3):
                        #  Applies increase in ship size to correct axis based on x_or_y variable
                        if x_or_y == 1:
                            ship_size_y = ship_size_y + 1
                            print(1)
                        if x_or_y == 0:
                            ship_size_x = ship_size_x + 1
                            print(0)
                #  Handles the clicking of the decrease size button
                if (l > 110 and l < 175) and (k > 650 and k < 700):
                    #  Check upper and lower bounds
                    if (ship_size_x > 0 and ship_size_x < 4) and (ship_size_y > 0 and ship_size_y < 3):
                        #  Applies decrease to correct axis
                        if x_or_y == 1:
                            ship_size_y = ship_size_y - 1
                        if x_or_y == 0:
                            ship_size_x = ship_size_x - 1
                #  Changes the orientation of the ship
                if (l > 290 and l < 385) and (k > 650 and k < 700):
                    x_or_y = 1
                    ship_size_x = 1
                #  Chnages the orientation of the ship
                if (l > 420 and l < 515) and (k > 650 and k < 700):
                    x_or_y = 0
                    ship_size_y = 1
                #  Gamelock breakc point
                if game_lock:
                    #  If a ship is placed in the first grid
                    if (l > 100 and l < 600) and (k > 100 and k < 600):
                        #  x spot reduces the position of the click to an index for the coordinate system that is grid
                        x_spot = int(round((l - 124) / 50))
                        x_boat_coords[5-ships_left] = x_spot
                        #  include boat length information when placing ship
                        x_boat_length[5-ships_left] = ship_size_x -1
                        y_spot = int(round(k - 124) / 50)
                        y_boat_coords[5-ships_left] = y_spot
                        y_boat_length[5 - ships_left] = ship_size_y - 1

                        #  The case in which a ship is placed above a ship already present
                        if user_grid[x_spot][y_spot] == 1:
                            tut_count = 4
                            ships_left = ships_left + 1
                        #  Assign value of 1 in grid system to signnify a ship present
                        user_grid[x_spot][y_spot] = 1
                        #  Adjusts if ship is larger than 1 unit so that etire ship is saved
                        if ship_size_x > 1:
                            for i in x_boat_length:
                                user_grid[x_spot+i][y_spot] = 1
                        if ship_size_y > 1:
                            for i in y_boat_length:
                                user_grid[x_spot][y_spot + i] = 1
                        #  Reduces number of ships left
                        ships_left = ships_left - 1
                        #  Accounts for what to do when all ships are used
                        if ships_left == 0:
                            #  Change tip
                            tut_count = 1
                            #  Computer will place 5 ships at random using random computer_move() function
                            for i in range(5):
                                x,y,xl,yl = computer_move()
                                computer_grid[x][y] = 1
                                for i in range(xl):
                                    #  Accounts for ship size which extends the bounds of the grid
                                    if (x+i) > 9:
                                        computer_grid[x][y] = 1
                                    else:
                                        computer_grid[x+i][y] = 1
                                for i in range(yl):
                                    if (y+i) > 9:
                                        computer_grid[x][y]
                                    else:
                                        computer_grid[x][y+i] = 1

                # Another game_lock breakpoint
                if game_lock:
                    #  Manages button clicks in second grid
                    if (l > 740 and l < 1250) and (k > 100 and k < 600):
                        #  Reduces position of click to an index
                        x_spot = int(round((l - 774) / 50))
                        y_spot = int(round(k - 124) / 50)
                        #  Hit logic, if cell point = 1 then a ship is present
                        if computer_grid[x_spot][y_spot] == 1:
                            user_score = user_score + 1
                            tut_count = 2
                            computer_grid[x_spot][y_spot] = 3
                        else:
                            #  if no ship present show miss
                            computer_grid[x_spot][y_spot] = 2
                            tut_count = 3
                        #  Reduces shop counter
                        shots_left = shots_left - 1
                        #  Change tip
                        tut_count = 5
                        #  Unpacks random nits from computer logic
                        x,y,xl,yl = computer_move()
                        #  Accoutns for computer hit logic
                        if user_grid[x][y] == 1:
                            #  Change tip
                            tut_count = 6
                            #  Increase ai score
                            ai_score = ai_score + 1
                            #  Changes block to hit block
                            user_grid[x][y] = 3
                        else:
                            #  If no hit change to a miss
                            user_grid[x][y] = 2
                #  Locks ths game when user runs out of shots
                if shots_left == 0:
                    game_lock = False
        #  If user clicks quit game will end
        if event.type == pygame.QUIT:
                quit()
        #  Sets y bound
        y_text = 630
        #  Draw Buttons and tiles
        pygame.draw.rect(display, shipfinalcolour, (0, 0, 640, 720))
        pygame.draw.rect(display, (0, 0, 128), (640, 0, 640, 720))
        pygame.draw.rect(display, black, (20, 650, 65, 50))
        pygame.draw.rect(display, shipfinalcolour, (22, 652, 60, 45))
        pygame.draw.rect(display, black, (110, 650, 65, 50))
        pygame.draw.rect(display, shipfinalcolour, (112, 653, 60, 45))
        pygame.draw.rect(display, black, (290, 650, 95, 50))
        pygame.draw.rect(display, shipfinalcolour, (292, 652, 90, 45))
        pygame.draw.rect(display, black, (420, 650, 95, 50))
        pygame.draw.rect(display, shipfinalcolour, (422, 652, 90, 45))

        #  Initializes font values

        #  Creates text files to be used
        text8 = myfont.render(str(ai_score), True, (255, 255, 255))
        text9 = myfont.render(str(user_score), True, (255, 255, 255))
        text11 = mybigfont.render(str(ships_left), True, (255, 255, 255))
        text12 = mybigfont.render("Tip: " + tutorial(tut_count), True, (255, 255, 255))
        display.blit(text1, (25, y_text))
        display.blit(text2, (45, y_text + 30))
        display.blit(text2_1, (140, y_text + 30))
        display.blit(text3, (350, y_text))
        display.blit(text4, (325, y_text + 38))
        display.blit(text5, (800, 650))
        display.blit(text6, (1000, 650))
        display.blit(text7, (430, y_text + 38))
        display.blit(text8, (1150, 650))
        display.blit(text9, (900, 650))
        display.blit(text10, (250, 25))
        display.blit(text11, (400, 25))
        display.blit(text12, (800, 25))

        #  Draw grid
        for i in range(0, 11):
            coordinate_change_blk_2 = i * 50 + 740
            coordinate_change = i * 50 + 100
            pygame.draw.line(display, [0, 0, 0], (coordinate_change, 100), (coordinate_change, 600), 4)
            pygame.draw.line(display, [0, 0, 0], (100, coordinate_change), (600, coordinate_change), 4)
            pygame.draw.line(display, [0, 0, 0], (coordinate_change_blk_2, 100), (coordinate_change_blk_2, 600), 4)
            pygame.draw.line(display, [0, 0, 0], (740, coordinate_change), (1240, coordinate_change), 4)

        #Draw grid characters
        for i in range(0, 10):
            x_coord_change_blk_2 = i * 50 + 760
            x_coord_change = i * 50 + 120
            y_coord_change = i * 50 + 110
            Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

            text = myfont.render(Letters[i], True, (255, 255, 255))
            numbers = myfont.render(numbers[i], True, (255, 255, 255))
            display.blit(text, (x_coord_change, 65))
            display.blit(numbers, (65, y_coord_change))
            display.blit(text, (x_coord_change_blk_2, 65))
            display.blit(numbers, (700, y_coord_change))
            #  Draw block on grid as mouse moves
            if (l > 100 and l < 600) and (k > 100 and k < 600):
                pygame.draw.rect(display, black, (l - 25, k - 25, ship_x, ship_y))
            if (l > 740 and l < 1250) and (k > 100 and k < 600):
                pygame.draw.rect(display, black, (l - 25, k - 25, ship_x, ship_y))
        pygame.display.update()

        clock.tick(60)

#  Run
intro_screen(True)