from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0 
        self.col_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
    
    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    def get_cell_positions(self):
        if self.rotation_state<0: # rotation_state가 0보다 작아지는 에러 방지
            self.rotation_state = 0
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for pos in tiles:
            position = Position(pos.row + self.row_offset, pos.col + self.col_offset)    
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state +=1
        if self.rotation_state ==len(self.cells):
            self.rotation_state = 0

    def undo_rotate(self):
        self.rotation_state -=1
        if self.rotation_state ==0:
            self.rotation_state = len(self.cells)-1
    
    def draw(self, screen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
