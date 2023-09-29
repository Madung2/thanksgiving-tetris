import pygame
from grid import Grid
from blocks import *
import random
import time


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.start_time = None
        self.elapsed_time = "00:00"
        self.line_cleared = 0
        
        #pygame.mixer.music.load('tetris/tetris/Sounds/BGM_Tetris.mp3')
        #pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, move_down_points):
        """점수를 업데이트하는 함수

        Args:
            lines_cleared (int): 지운 줄의 개수
            move_down_points (int): 블록을 한칸 내릴 때마다 얻는 점수
        """
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 800
        self.score += move_down_points

    def get_elapsed_time(self):
        if self.start_time is not None and not self.game_over:
            elapsed_seconds = int(time.time() - self.start_time)
            minutes = elapsed_seconds // 60
            seconds = elapsed_seconds % 60
            self.elapsed_time =  f"{minutes:02}:{seconds:02}"

    def get_random_block(self):
        """랜덤으로 블록을 생성하는 함수, 중복방지를 위해 사용된 블록은 리스트에서 제거한다. 블록이 없으면 새 블록 세트를 추가한다
        Returns:
            Block: 랜덤으로 생성된 블록
        """
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        """왼쪽으로 블록이 한칸 움직이게 하는 함수"""
        self.current_block.move(0, -1)
        if not (self.block_inside() and self.block_fits()):
            self.current_block.move(0, 1)
    
    def move_right(self):
        """오른쪽으로 블록이 한칸 움직이게 하는 함수"""
        self.current_block.move(0, 1)
        if not (self.block_inside() and self.block_fits()):
            self.current_block.move(0, -1)
    
    def move_down(self):
        """아래로 블록이 한칸 움직이게 하는 함수"""
        self.current_block.move(1, 0)
        if not (self.block_inside() and self.block_fits()):
            self.current_block.move(-1, 0)
            self.lock_block()
            
    def lock_block(self):
        """블록이 바닥에 닿거나 새 브록 생성될때 활성화되는 함수"""
        tiles = self.current_block.get_cell_positions()
        if not self.block_inside():
            raise Exception("블록이 그리드 밖으로 나갔습니다")
        
        for pos in tiles:
            self.grid.grid[pos.row][pos.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.rows_cleared = self.grid.clear_full_rows()
        self.line_cleared += self.rows_cleared
        self.update_score(self.rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.start_time = time.time()

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        return all(self.grid.is_empty(pos.row, pos.col) for pos in tiles)

    def drop(self):
        """블록을 떨어뜨리는 함수"""
        while self.block_fits():
            self.current_block.move(1, 0)

    def rotate(self):
        """블록을 회전시키는 함수, 회전이 불가능하면 회전하지 않는다"""
        self.current_block.rotate()
        if not self.block_inside():
            self.current_block.undo_rotate()        

    def block_inside(self):
        """블록이 그리드 안에 있는지 확인하는 함수

        Returns:
            bool: 모든 타일이 그리드 안에 있으면 True, 아니면 False
        """
        tiles = self.current_block.get_cell_positions()
        return all(self.grid.is_inside(tile.row, tile.col) for tile in tiles)

    def draw(self, screen):
        
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11) 
        if self.next_block.id == 2: #IBlock
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 7: #OBlock
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)

