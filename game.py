from grid import Grid
from blocks import *
import random
class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside():
            self.current_block.move(0, 1)
    
    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside():
            self.current_block.move(0, -1)
    
    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside():
            self.current_block.move(-1, 0)

    
    def drop(self):
        while self.current_block.can_move(1, 0):
            self.current_block.move(1, 0)

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col):
                return False
        return True

    def draw(self, screen):
        ## print(screen) = <Surface(300x600x32)>
        self.grid.draw(screen)
        self.current_block.draw(screen) 

