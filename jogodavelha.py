import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (0, 0, 255)
CROSS_COLOR = (255, 0, 0)

# Inicialize a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha")

# Tabuleiro do jogo
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Função para desenhar o tabuleiro
def draw_board():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Função para desenhar o X
def draw_x(row, col):
    x = col * SQUARE_SIZE
    y = row * SQUARE_SIZE
    pygame.draw.line(screen, CROSS_COLOR, (x, y), (x + SQUARE_SIZE, y + SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, CROSS_COLOR, (x + SQUARE_SIZE, y), (x, y + SQUARE_SIZE), LINE_WIDTH)

# Função para desenhar o O
def draw_o(row, col):
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    radius = SQUARE_SIZE // 2 - LINE_WIDTH // 2
    pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), radius, LINE_WIDTH)

# Função para verificar se o jogo terminou
def is_game_over():
    for row in board:
        if all([cell == 'X' for cell in row]) or all([cell == 'O' for cell in row]):
            return True
    for col in range(BOARD_COLS):
        if all([board[row][col] == 'X' for row in range(BOARD_ROWS)]) or all([board[row][col] == 'O' for row in range(BOARD_ROWS)]):
            return True
    if all([board[i][i] == 'X' for i in range(BOARD_ROWS)]) or all([board[i][i] == 'O' for i in range(BOARD_ROWS)]):
        return True
    if all([board[i][BOARD_COLS - i - 1] == 'X' for i in range(BOARD_ROWS)]) or all([board[i][BOARD_COLS - i - 1] == 'O' for i in range(BOARD_ROWS)]):
        return True
    return False

# Loop principal do jogo
player_turn = 'X'
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = player_turn
                if player_turn == 'X':
                    player_turn = 'O'
                else:
                    player_turn = 'X'

    screen.fill(WHITE)
    draw_board()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                draw_x(row, col)
            elif board[row][col] == 'O':
                draw_o(row, col)

    if is_game_over():
        game_over = True

    pygame.display.update()