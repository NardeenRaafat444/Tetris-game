import pygame
from color import Colors

class Grid:    #creating a class called Grid
    
    
    #class attributes
    def __init__(self): #init stands for initation + this function is usually used for assigning the class attributes
        self.num_rows = 20  #number of rows
        self.num_cols = 10 #number of columns 
        self.cell_size = 30 #sell size
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]  #this a way to create a 2d (List Comprehension)   # a 2d list is a list containing lists  # column resemples the elemnts and rows resemples the num of lists  
        self.colors = Colors.get_cell_colors() #the color attribute stores the get_cell_colors method  
    
    
    
    
    #class methods (functiones)
    
    def print_grid(self):   
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end =" ")  #the default end value is \n so  end = " " prints the values on the same row
            print() #   ====== print("\n") #it is used to put the new row in a new line (creating the columns)

    
    

 


    def draw(self, screen): # this the draw fuc used to draw rects on the surface  #we pass screen as an argument because we are in the grid file # but the rect method needs the surface value
        for row in range(self.num_rows):
            for column in range(self.num_cols): #nested for loop used to change the og 0 value to [1:7] #each index resemples a specific color determined in the get_cell_color function #it also darws the rect in each cell 
                cell_value = self.grid[row][column] #This line retrieves the value stored in the current cell of the grid.
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size-1) #Rect(left, top, width, height) #the +1 -1 are used to create a border between the cells #the math logic is that the rect is posioned as far from the top (x coordinate) as 10 cells or 20 cells and the same goes for the left (y coordinate)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)  #rect(surface, color, rect) #draw a colored rectangle