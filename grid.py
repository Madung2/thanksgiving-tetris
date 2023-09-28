import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    # def print_grid(self):
    #     for row in range(self.num_rows):
    #         for col in range(self.num_cols):
    #             print(self.grid[row][col], end = " ")
    #         print()
    
    def is_inside(self, row, col):
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols


    def draw(self,screen):
        cs = self.cell_size
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_val = self.grid[row][col]
                cell_rect = pygame.Rect(col * cs +1 , row * cs +1 , cs-1, cs-1)
                pygame.draw.rect(screen, self.colors[cell_val], cell_rect)