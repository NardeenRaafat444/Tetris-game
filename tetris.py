import pygame
import random

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GRID_SIZE = 25
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Tetris shapes and colors
SHAPES = [
    [[1, 1, 1, 1], [0, 0, 0, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 1]],
    [[1, 1, 1], [1, 1, 0]],
    [[1, 1], [1, 1]]
]

COLORS = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 165, 0)   # Orange
]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)
        piece = {
            'shape': shape,
            'color': color,
            'x': GRID_WIDTH // 2 - len(shape[0]) // 2,
            'y': 0
        }
        return piece

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(self.screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, self.grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def draw_piece(self):
        for i, row in enumerate(self.current_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen,
                        self.current_piece['color'],
                        ((self.current_piece['x'] + j) * GRID_SIZE, (self.current_piece['y'] + i) * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                    )

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def move_piece(self, dx, dy):
        self.current_piece['x'] += dx
        self.current_piece['y'] += dy

    def rotate_piece(self):
        self.current_piece['shape'] = list(zip(*self.current_piece['shape'][::-1]))

    def check_collision(self, dx, dy):
        for i, row in enumerate(self.current_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    if (
                        self.current_piece['x'] + j + dx < 0
                        or self.current_piece['x'] + j + dx >= GRID_WIDTH
                        or self.current_piece['y'] + i + dy >= GRID_HEIGHT
                        or self.grid[self.current_piece['y'] + i + dy][self.current_piece['x'] + j + dx]
                    ):
                        return True
        return False

    def merge_piece(self):
        for i, row in enumerate(self.current_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + i][self.current_piece['x'] + j] = self.current_piece['color']

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for line in lines_to_clear:
            del self.grid[line]
            self.grid.insert(0, [0] * GRID_WIDTH)
            self.score += 1

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and not self.check_collision(-1, 0):
                        self.move_piece(-1, 0)
                    elif event.key == pygame.K_RIGHT and not self.check_collision(1, 0):
                        self.move_piece(1, 0)
                    elif event.key == pygame.K_DOWN and not self.check_collision(0, 1):
                        self.move_piece(0, 1)
                    elif event.key == pygame.K_UP:
                        self.rotate_piece()

            if not self.check_collision(0, 1):
                self.move_piece(0, 1)
            else:
                self.merge_piece()
                self.clear_lines()
                self.current_piece = self.new_piece()
                if self.check_collision(0, 0):
                    self.game_over = True

            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_piece()
            self.draw_score()
            pygame.display.flip()
            self.clock.tick(5)

        pygame.quit()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()

#######################################
# import pygame, sys    #importing the pygamelibrary and the sys (used for exit)
# from grid import Grid #importing the Grid class from the grid file 

# pygame.init() #must be wriiten to initate the pygame library

# dark_blue = (44, 44, 127) #indentfing the color and assigning it to a variable

# screen= pygame.display.set_mode ((300, 600))  #setting the width and height of the window
# pygame.display.set_caption("Python Tetris")  #setting the window name

# clock = pygame.time.Clock()

# game_grid = Grid()

# game_grid.grid[0][0] = 1
# game_grid.grid[3][5] = 4
# game_grid.grid[17][8] = 7

# game_grid.print_grid()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()    
# #Drawing
#     screen.fill(dark_blue)
#     game_grid.draw(screen)

#     pygame.display.update()
#     clock.tick (60)



###############################
import pygame
class Grid:
    def __init__(self):
        self.num_rows = 20 
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end =" ")
            print()

    def get_cell_colors(self):

        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]
    
    def draw(self, screen): #we pass screen as an argument because we are in the grid file but the rect method needs the surface value
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size-1)
                pygame.draw.rect(screen,self.colors[cell_value], cell_rect) 