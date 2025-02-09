import pygame, sys    #importing the pygamelibrary and the sys (used for exit)
from grid import Grid #importing the Grid class from the grid file 
from blocks import *
pygame.init() #must be wriiten to initate the pygame library

dark_blue = (44, 44, 127) #indentfing the color and assigning it to a variable

screen= pygame.display.set_mode ((300, 600))  #setting the width and height of the window
pygame.display.set_caption("Python Tetris")  #setting the window name

clock = pygame.time.Clock() #used to set the maximum frame rate to make sure it doesn't run too fast

game_grid = Grid() #instance for the class 

block = IBlock()
##########game_grid.print_grid() #printing the class

while True:   #the game loop 
    for event in pygame.event.get(): #the quit event (must be written in all pygame programmes)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
#Drawing
    screen.fill(dark_blue) #the fill method is used for colors
    game_grid.draw(screen) #this displays the grid on the display surface (main)
    block.draw(screen)

    pygame.display.update() #the display surface must always be updated 
    clock.tick (60) #setting the maximum framerate