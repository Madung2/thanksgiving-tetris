
import asyncio
import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

####### 게임 스크린 정의 ########
screen = pygame.display.set_mode((500, 620)) # width, height
pygame.display.set_caption("Tetris")

####### 기타 UI정의 ########
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
start_surface = title_font.render("Start", True, Colors.white)
rotate_surface = title_font.render("Rotate", True, Colors.white)
start_rect = pygame.Rect(320, 440, 170, 50)
rotate_rect = pygame.Rect(320, 500, 100, 100)
press_space_surface = title_font.render("Press Space", True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 50)
next_rect = pygame.Rect(320, 215, 170, 180)

####### 게임 루프 정의 ########
clock = pygame.time.Clock()
game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)


##게임 시작 기본 상태
game.game_over = True
start_time = None # 게임 시작 초기화
game.grid.reset()

async def main():
    while True:
        
        ######### 이벤트 처리 #########
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # 키보드를 눌렀을 때

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
            if event.type == GAME_UPDATE and (not game.game_over):  # 0.2초마다 블록이 한칸씩 내려감
                game.move_down()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_pos[0] < 150 and (not game.game_over): # 화면 왼쪽 반을 클릭
                    game.move_left()
                elif 150< mouse_pos[0]< 310 and (not game.game_over):
                    game.move_right()
                elif start_rect.collidepoint(mouse_pos):
                    game.game_over = False
                    game.reset()
                elif rotate_rect.collidepoint(mouse_pos):
                    game.rotate()

        ######### 화면 그리기 #########
        score_value_surface = title_font.render(str(game.score), True, Colors.white)
        clock_value_surface = title_font.render(game.elapsed_time, True, Colors.white)
        line_value_surface = title_font.render(f'lines:{game.line_cleared}', True, Colors.white)
        screen.fill(Colors.dark_blue)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (370, 400, 50, 50))
        if game.game_over:
            screen.blit(start_surface, (370, 450, 50, 50))
            screen.blit(press_space_surface, (325, 500, 50, 50))
            pygame.draw.rect(screen, Colors.white, start_rect, 5)
        elif not game.game_over:
            screen.blit(rotate_surface, (326, 535, 50, 50))
            pygame.draw.rect(screen, Colors.white, rotate_rect, 5)
        pygame.draw.rect(screen, Colors.light_blue, score_rect, 5)
        screen.blit(score_value_surface, score_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery))
        screen.blit(clock_value_surface, clock_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery + 50))
        screen.blit(line_value_surface, line_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery + 100))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 5)
        game.draw(screen)

        ######### 게임 루프 #########
        game.get_elapsed_time()
        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(60)  # 60 frames per sec

# Call the main function
asyncio.run(main())