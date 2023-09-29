import pygame
import sys
from game import Game

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600)) # width, height
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # 키보드를 눌렀을 때                
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_SPACE:
                    game.drop()
        if event.type == GAME_UPDATE: # 0.2초마다 블록이 한칸씩 내려감
            game.move_down()

    # draw
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60) # 60 frames per sec

## Start from 32min Create blocks