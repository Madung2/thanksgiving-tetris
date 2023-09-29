from colors import Colors
import pygame
from position import Position

class Block:
    """블록 클래스"""
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0 # 블록의 위치를 나타내는 변수
        self.col_offset = 0 # 블록의 위치를 나타내는 변수
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
    
    def move(self, row, col):
        """블록을 움직이는 함수

        Args:
            row (int): 움직인 행
            col (int): 움직인 열
        """
        self.row_offset += row
        self.col_offset += col

    def get_cell_positions(self):
        """블록의 위치를 나타내는 함수

        Returns:
            list: 블록의 위치
        """
        if self.rotation_state<0: # rotation_state가 0보다 작아지는 에러 방지
            self.rotation_state = 0
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for pos in tiles:
            position = Position(pos.row + self.row_offset, pos.col + self.col_offset)    
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        """블록을 회전시키는 함수"""
        self.rotation_state +=1
        if self.rotation_state ==len(self.cells):
            self.rotation_state = 0

    def undo_rotate(self):
        """블록 회전을 되돌리는 함수"""
        self.rotation_state -=1
        if self.rotation_state ==0:
            self.rotation_state = len(self.cells)-1
    
    def draw(self, screen, offset_x, offset_y):
        """블록을 그리는 함수

        Args:
            screen (screen): 화면
            offset_x (int): 타일 x좌표
            offset_y (int): 타일 y좌표
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size + offset_x, tile.row * self.cell_size + offset_y, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
