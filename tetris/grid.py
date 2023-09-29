import pygame
from colors import Colors

class Grid:
    """게임 그리드를 정의하는 클래스"""
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0] * self.num_cols for _ in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()
    
    def is_inside(self, row, col):
        """블록이 그리드 안에 있는지 확인하는 함수"""
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols
    
    def is_empty(self, row, col):
        """블록이 비어있는지 확인하는 함수
        
        Args:
            row (int): 행
            col (int): 열
        Returns:
            bool: 모두 비어있으면 True, 아니면 False
        """
        if row < 0 or row >= self.num_rows or col < 0 or col >= self.num_cols:
            return False # 그리드 밖으로 나가는 경우 에러 방지
        return True if self.grid[row][col] == 0 else False
    
    def is_full(self, row):
        """블록이 꽉 차있는지 확인하는 함수

        Args:
            row (int): 행
        Returns:
            bool: 모두 꽉 차있으면 True, 아니면 False
        """
        return all(self.grid[row][col] != 0 for col in range(self.num_cols))
    
    def clear_row(self, row):
        """한줄을 지우는 함수
        
        Args:
            row (int): 행
        """
        for col in range(self.num_cols):
            self.grid[row][col] = 0 

    def move_down_rows(self, row, num_rows):
        """한줄 위의 모든 줄을 한칸씩 내리는 함수
        
        Args:
            row (int): 행
        """
        for col in range(self.num_cols):
            self.grid[row+num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clear_full_rows(self):
        """꽉 찬 줄을 인지하고 지우는 함수

        Returns:
            int: 지워진 줄의 개수
        """
        row_completed = 0
        for row in range(self.num_rows-1, 0 , -1):
            if self.is_full(row):
                self.clear_row(row)
                self.move_down_rows(0, row)
                row_completed += 1
            elif row_completed > 0:
                self.move_down_rows(row, row_completed)
        return row_completed
    
    def reset(self):
        """그리드를 초기화하는 함수
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0

    def draw(self,screen):
        """그리드를 그리는 함수""" 
        cs = self.cell_size
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_val = self.grid[row][col]
                cell_rect = pygame.Rect(col * cs +11 , row * cs +11 , cs-1, cs-1)
                pygame.draw.rect(screen, self.colors[cell_val], cell_rect)