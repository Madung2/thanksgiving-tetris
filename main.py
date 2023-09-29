import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

####### UI정의 ########
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over", True, Colors.white)
press_space_surface = title_font.render("Press Space", True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 50)
next_rect = pygame.Rect(320, 215, 170, 180)


####### 게임 스크린 정의 ########
screen = pygame.display.set_mode((500, 620)) # width, height
pygame.display.set_caption("Tetris")

####### 게임 루프 정의 ########
clock = pygame.time.Clock()
game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

while True:
    ######### 이벤트 처리 #########
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # 키보드를 눌렀을 때

            if event.key == pygame.K_LEFT and (not game.game_over):
                game.move_left()
            if event.key == pygame.K_RIGHT and (not game.game_over):
                game.move_right()
            if event.key == pygame.K_DOWN and (not game.game_over):
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and (not game.game_over):
                game.rotate()
            if event.key == pygame.K_SPACE:
                if not game.game_over:
                    game.drop()
                if game.game_over:
                    game.game_over = False
                    game.reset()
        if event.type == GAME_UPDATE and (not game.game_over): # 0.2초마다 블록이 한칸씩 내려감
            game.move_down()

    ######### 화면 그리기 #########
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20,50, 50))
    screen.blit(next_surface, (370, 170,50, 50))
    if game.game_over:
        screen.blit(game_over_surface, (330, 450, 50, 50))
        screen.blit(press_space_surface, (325, 500, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 5)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 5)
    game.draw(screen)

    ######### 게임 루프 #########
    pygame.display.update()
    clock.tick(60) # 60 frames per sec

## Start from 32min Create blocks