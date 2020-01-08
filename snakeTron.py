# by Nathaniel Fernandes
# 2019

# Import a library of functions called 'pygame'
import pygame
import random

playAgain = True

score1 = 0
score2 = 0

while (playAgain):
        # Constants

    R_1 = (237, 59, 68)
    R_2 = (252, 95, 95)

    B_1 = (55, 167, 242)
    B_2 = (104, 197, 255)

    Y_1 = (255, 221, 86)
    Y_2 = (252, 255, 86)
    G_1 = (56, 247, 110)
    G_2 = (203, 238, 98)

    GREY = (89, 91, 94)
    lightGrey = (122, 122, 122)

    BLACK    = (   42,   42,   42)
    WHITE    = ( 255, 255, 255)
    BLUE     = (   0,   0, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)
    PI = 3.141592653
    variColour = [0, 0, 0]

    # Classes

    class player():
        
        def _init_(self):

            self.image = pygame.Surface([10, 10])
            self.image.fill(colour)

            self.colour = BLACK
            self.xpos = 0
            self.ypos = 0
            self.speedx = 0
            self.speedy = 0
            self.collided = False

        def draw(self):
            pygame.draw.rect(screen, self.colour, [self.xpos, self.ypos, 10, 10])
            #pygame.draw.rect(screen, BLACK, [self.xpos, self.ypos, 9, 9], 2)

        def collision(self, trailOneX, trailOneY, trailTwoX, trailTwoY):

            self.collided = False

            x = self.xpos
            y = self.ypos
            
            if (x > 980) or (x < 10) or (y > 980) or (y < 10):

                self.collided = True
            
            for i in range(len(trailOneX) - 1):
                if ((x == trailOneX[i]) and (y == trailOneY[i])):
                    
                    self.collided = True
            for i in range(len(trailTwoX) - 1):
                if ((x == trailTwoX[i]) and (y == trailTwoY[i])):
                    
                    self.collided = True

            if self.collided:
                self.colour = GREY
                for player in playerList:   
                    player.speedx = 0
                    player.speedy = 0

    class trail():

        def _init_(self):
            self.colour = BLACK
            self.xpos = 0
            self.ypos = 0
            self.speedx = 0
            self.speedy = 0
        def draw(self):
            pygame.draw.rect(screen, self.colour, [self.xpos, self.ypos, 10, 10])

    class food():
        def _init_(self):
            self.colour = RED
            self.xpos = 0
            self.ypos = 0
            self.collidedOne = False
            self.collidedTwo = False

        def collision(self, playerOneX, playerOneY, playerTwoX, playerTwoY):
            self.collidedOne = False
            self.collidedTwo = False
            if ((playerOneX == self.xpos) and (playerOneY == self.ypos)):
                self.collidedOne = True
            if ((playerTwoX == self.xpos) and (playerTwoY == self.ypos)):
                self.collidedTwo = True

        def draw(self):
            pygame.draw.rect(screen, self.colour, [self.xpos, self.ypos, 10, 10])


    ## Main ##
    # Initialize the game engine
    pygame.init()

    # Set the height and width of the screen
    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    # print screen.get_width()
    
    pygame.display.set_caption("SLITHER")
    
    #Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    ## MODEL ##

    #directions
    trueSpeed = 10

    #List of things
    playerList = []
    trailList = []
    playerOneCords = []
    playerTwoCords = []
    #player one
    playerOne = player()
    playerOne.colour = R_1
    playerOne.xpos = 200
    playerOne.ypos = 500
    playerOne.speedx = 0
    playerOne.speedy = 0

    playerList.append(playerOne)

    playerOneCords = []
    #player two
    playerTwo = player()
    playerTwo.colour = B_1
    playerTwo.xpos = 790
    playerTwo.ypos = 500
    playerTwo.speedx = 0
    playerTwo.speedy = 0

    playerList.append(playerTwo)

    #Trail Cords
    trailOneCordsX = []
    trailOneCordsY = []

    trailTwoCordsX = []
    trailTwoCordsY = []

    #Trail One
    trailOne = trail()
    trailOne.colour = R_2
    trailOne.xpos = playerOne.xpos
    trailOne.ypos = playerOne.ypos

    trailOneCordsX.append(trailOne.xpos)
    trailOneCordsY.append(trailOne.ypos)
    trailList.append(trailOne)

    #Trail Two
    trailTwo = trail()
    trailTwo.colour = B_2
    trailTwo.xpos = playerTwo.xpos
    trailTwo.ypos = playerTwo.ypos

    trailTwoCordsX.append(trailTwo.xpos)
    trailTwoCordsY.append(trailTwo.ypos)
    trailList.append(trailTwo)

    food_list = []

    theFood = food()
    theFood.colour = Y_1
    theFood.xpos = ((random.randrange(2, 98)) * 10)
    theFood.ypos = ((random.randrange(2, 98)) * 10)

    food_list.append(theFood)

    started = False
    preStartOne = False
    preStartTwo = False

    w = True
    s = True
    a = True
    d = True

    up = True
    down = True
    left = True
    right = True

    playerOne.collided = False
    playerTwo.collided = False

    x1 = 0
    x2 = 0
    x3 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    slide = 1

    snekkOne = 5
    snekkTwo = 5

    # Loop as long as done == False
    while not done:

        ## CONTROL ##
        for event in pygame.event.get(): # User did something
            if (event.type == pygame.QUIT): # If user clicked close
                playAgain = False
                done = True # Flag that we are done so we exit this loop
                
            elif (event.type == pygame.KEYDOWN):

                #player one controls
                if w:
                    if (event.key == pygame.K_w):
                        playerOne.speedx = 0
                        playerOne.speedy = (trueSpeed * -1)
                        w = True
                        s = False
                        a = True
                        d = True

                if s:
                    if (event.key == pygame.K_s):  
                        playerOne.speedx = 0
                        playerOne.speedy = trueSpeed
                        w = False
                        s = True
                        a = True
                        d = True
                if a:
                    if (event.key == pygame.K_a):   
                        playerOne.speedy = 0            
                        playerOne.speedx = (trueSpeed * -1)
                        w = True
                        s = True
                        a = True
                        d = False
                if d:
                    if (event.key == pygame.K_d):
                        playerOne.speedy = 0
                        playerOne.speedx = trueSpeed
                        w = True
                        s = True
                        a = False
                        d = True


                    #player two controls
                if up:
                    if (event.key == pygame.K_UP):  
                        playerTwo.speedx = 0
                        playerTwo.speedy = (trueSpeed * -1)
                        up = True
                        down = False
                        left = True
                        right = True
                if down:
                    if (event.key == pygame.K_DOWN):
                        playerTwo.speedx = 0
                        playerTwo.speedy = trueSpeed
                        up = False
                        down = True
                        left = True
                        right = True
                if left:
                    if (event.key == pygame.K_LEFT):
                        playerTwo.speedy = 0
                        playerTwo.speedx = (trueSpeed * -1)
                        up = True
                        down = True
                        left = True
                        right = False
                if right:
                    if (event.key == pygame.K_RIGHT):
                        playerTwo.speedy = 0
                        playerTwo.speedx = trueSpeed
                        up = True
                        down = True
                        left = False
                        right = True

                if ((playerOne.speedx != 0) or (playerOne.speedy != 0)):
                    preStartOne = True
                if ((playerTwo.speedx != 0) or (playerTwo.speedy != 0)):
                    preStartTwo = True
                if (preStartOne and preStartTwo):        
                    if (event.key == pygame.K_SPACE) and (not playerOne.collided) and (not playerTwo.collided):
                        started = True
                        playerOne.colour = R_1
                        playerTwo.colour = B_1

        if started:
        

            playerOne.collided = False
            playerTwo.collided = False
                
            playerOne.collision(trailOneCordsX, trailOneCordsY, trailTwoCordsX, trailTwoCordsY)
            playerTwo.collision(trailOneCordsX, trailOneCordsY, trailTwoCordsX, trailTwoCordsY)
                            
            if (playerOne.collided) and (playerTwo.collided):
                started = False
                trailOne.colour = lightGrey
                trailTwo.colour = lightGrey
                done = True

            elif (playerOne.collided):
                started = False
                trailOne.colour = lightGrey
                score2 += 90
                done = True
                    #playerTwo.colour = Y_1
                    #trailTwo.colour = Y_2
                    
            elif (playerTwo.collided):
                started = False
                trailTwo.colour = lightGrey
                score1 += 90
                done = True
                    #playerOne.colour = Y_1
                    #trailOne.colour = Y_2

            theFood.collision(playerOne.xpos, playerOne.ypos, playerTwo.xpos, playerTwo.ypos)
            if (theFood.collidedOne):
                del food_list[0]
                
                # theFood = food()
                theFood.colour = Y_1
                theFood.xpos = ((random.randrange(2, 98)) * 10)
                theFood.ypos = ((random.randrange(2, 98)) * 10)

                # theFood.collided = False
                snekkOne += 10
                food_list.append(theFood)
            
            if (theFood.collidedTwo):
                del food_list[0]
                
                # theFood = food()
                theFood.colour = Y_1
                theFood.xpos = ((random.randrange(2, 98)) * 10)
                theFood.ypos = ((random.randrange(2, 98)) * 10)

                # theFood.collided = False
                snekkTwo += 10
                food_list.append(theFood)
 

        #playerOne updates
        
            playerOne.ypos += playerOne.speedy
            playerOne.xpos += playerOne.speedx

            trailOneCordsX.append(playerOne.xpos)
            trailOneCordsY.append(playerOne.ypos)


        #playerTwo updates
            playerTwo.ypos += playerTwo.speedy
            playerTwo.xpos += playerTwo.speedx

            trailTwoCordsX.append(playerTwo.xpos)   
            trailTwoCordsY.append(playerTwo.ypos)

        ## VIEW ##
        # All drawing code happens after the for loop and but
        # inside the main while not done loop.
        
        # Clear the screen and set the screen background

        screen.fill(G_2)
        pygame.draw.rect(screen, BLACK, [0, 0, 1000, 1000], 20)
        #background_image = pygame.image.load("backGround.jpg").convert()
        #screen.blit(background_image, [0, 0])
        
        #draws player one trail
        for i in range(len(trailOneCordsX)):
            trailOne.xpos = trailOneCordsX[i]
            trailOne.ypos = trailOneCordsY[i]
            trailOne.draw()

        #draws player two trail
        for i in range(len(trailTwoCordsX)):
            trailTwo.xpos = trailTwoCordsX[i]
            trailTwo.ypos = trailTwoCordsY[i]
            trailTwo.draw()

        if ((len(trailOneCordsX)) > snekkOne):
            del trailOneCordsX[0]
            del trailOneCordsY[0]

        if ((len(trailTwoCordsX)) > snekkTwo):
            del trailTwoCordsX[0]
            del trailTwoCordsY[0]
 
        #draws players
        for player in playerList:
        
            player.draw()

        for food in food_list:
            food.draw()
        pygame.draw.rect(screen, BLACK, [theFood.xpos, theFood.ypos, 9, 9], 2)

        if (not started) and (not playerOne.collided) and (not playerTwo.collided):
            if ((playerOne.speedx != 0) or (playerOne.speedy != 0)):
                playerOne.colour = G_1
                pygame.draw.rect(screen, BLACK, [playerOne.xpos, playerOne.ypos, 9, 9], 2)

            if ((playerTwo.speedx != 0) or (playerTwo.speedy != 0)):
                playerTwo.colour = G_1
                pygame.draw.rect(screen, BLACK, [playerTwo.xpos, playerTwo.ypos, 9, 9], 2)

        slide *= -1

        if (not preStartOne):
            controlsWASD_image = pygame.image.load("controlsWASD.png").convert()
            controlsWASD_image.set_colorkey(WHITE)

            screen.blit(controlsWASD_image, [x1, y2])

            x1 += slide
            y1 += slide
            

        if (not preStartTwo):
            controlsUP_image = pygame.image.load("controlsUP.png").convert()
            controlsUP_image.set_colorkey(WHITE)       

            screen.blit(controlsUP_image, [x1, y2])

            x2 += slide
            y2 += slide
            

        if (preStartOne) and (preStartTwo) and (not started):
            space_image = pygame.image.load("space.png").convert()
            space_image.set_colorkey(WHITE)
            screen.blit(space_image, [x3, y3])

            if (playerOne.collided) and (playerTwo.collided):

                tie12_image = pygame.image.load("tie12.png").convert()
                tie12_image.set_colorkey(WHITE)   
                screen.blit(tie12_image, [0, 0])

            
            elif (playerOne.collided):
                win2_image = pygame.image.load("win2.png").convert()
                win2_image.set_colorkey(WHITE)
                screen.blit(win2_image, [0, 0])
                

            elif (playerTwo.collided):
                win1_image = pygame.image.load("win1.png").convert()
                win1_image.set_colorkey(WHITE)
                screen.blit(win1_image, [0, 0])
                
            if (playerOne.collided) or (playerTwo.collided):
                bothnumbers_image = pygame.image.load("bothnumbers.png").convert()
                bothnumbers_image.set_colorkey(WHITE)

                #score
                screen.blit(bothnumbers_image, (20, 20), [score1, 0, 90, 90])
                screen.blit(bothnumbers_image, (890, 20), [score2, 90, 90, 90])
                
                
            x3 += slide
            y3 += slide
            #pygame.time.wait(0)
        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(30)
      
    # Be IDLE friendly
    end = True
    while (end):
        for event in pygame.event.get(): # User did something    
            if (event.type == pygame.QUIT): # If user clicked close
                end = False
                playAgain = False
                done = True
                
            elif (event.type == pygame.KEYDOWN):
                
                if (event.key == pygame.K_SPACE):
                    end = False
                    playAgain = True
pygame.quit()
