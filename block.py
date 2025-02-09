from color import Colors
import pygame
class Block: #creating a Block calss an using inheiratnce (to avoid repeating code)
    def __init__(self, id): #identifing id to difrenciae between diffrent blocks
        self.id = id
        self.cells = {} #why dict? 
        self.cell_size = 30
        self.rotation_state = 0 ###kiro's part?  @@@@
        self.colors = Colors.get_cell_colors() #get_colors_function is in the Colors class 

    def draw(self, screen): #drawing blocks on the display surface
        tiles = self.cells[self.rotation_state] #identifing the key  @@@
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1) #column/row? tile.column @@@@
            pygame.draw.rect(screen, self.colors[self.id], tile_rect) #rect(surface, color, rect) #draw a colored rectangle for the block

    

