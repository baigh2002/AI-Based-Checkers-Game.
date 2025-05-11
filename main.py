import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
pygame.font.init()

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def draw_winner(win, winner_color):
    win.fill((0, 0, 0))  # Clear the screen
    font = pygame.font.SysFont('comicsans', 60)
    if winner_color == WHITE:
        win_text = "AI Wins!"
    elif winner_color == RED:
        win_text = "YOU Wins!"
    else:
        win_text = "It's a Draw!"

    text = font.render(win_text, True, (0, 255, 0))
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    depth = 2

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), depth, WHITE, game)
            game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

        winner = game.winner()
        if winner is not None:
            draw_winner(WIN, winner)
            run = False
    
    pygame.quit()

main()
