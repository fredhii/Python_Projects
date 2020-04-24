import pygame
import numpy as np
import time

pygame.init()

# Screen width and height 
width, height = 800, 600

# Create Screen
screen = pygame.display.set_mode((width, height))
# Create black background
bg = 25, 25, 25
# Show background
screen.fill(bg)

# Size cells
nxC, nyC = 50, 50

# Cells dimentions
dimCW =  width // nxC
dimCH = height // nyC
# Cells Status. Alive = 1; Dead = 0
gameState = np.zeros((nxC, nyC))


gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

# Control game execution
pauseExect = False

#Infinite loop
while True:

    newGameState = np.copy(gameState)

    # Clean screen
    screen.fill(bg)
    time.sleep(0.1)

    # Get keyboard and mouse events
    ev = pygame.event.get()

    for event in ev:
        # Check if there is any key press
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
            print()
        # Check if mouse is pressed
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            if newGameState[celX, celY] == 1:
                newGameState[celX, celY] = not mouseClick[0]
            else:
                newGameState[celX, celY] = not mouseClick[2]

    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:
                # Calculate number of near alive cells, use of Toroidal field 
                n_neigh =   gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                            gameState[(x)     % nxC, (y - 1) % nyC] + \
                            gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                            gameState[(x - 1) % nxC, (y)     % nyC] + \
                            gameState[(x + 1) % nxC, (y)     % nyC] + \
                            gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                            gameState[(x)     % nxC, (y + 1) % nyC] + \
                            gameState[(x + 1) % nxC, (y + 1) % nyC]

                # ==============================================================
                # Game Rules
                # ==============================================================
                
                # Rule #1: If a cell is dead with 3 near alive cells, It'll revives
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Rule #2: If a cell is alive with less than 2 or more than 3 alive cells, It'll dies
                if gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0


            # Create polygon cells
            poly = [((x)     * dimCW, y          * dimCH),
                    ((x + 1) * dimCW, y          * dimCH),
                    ((x + 1) * dimCW, (y + 1)    * dimCH),
                    ((x)     * dimCW, (y + 1)    * dimCH)]
            # Draw cells for x and y
            if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Update game state
    gameState = np.copy(newGameState)

    # Update screen
    pygame.display.flip()
