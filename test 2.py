# Import knihovny pro práci s "náhodou" a s grafikou
import random
import pygame

# Velikost hracího pole a velikost jednoho políčka v pixelech
BOARD_SIZE = 8
CELL_SIZE = 50

# Počet min na hracím poli
NUM_MINES = 10

# Třída pro jedno políčko na hracím poli
class Cell:
    def __init__(self, x, y):
        # Souřadnice políčka
        self.x = x
        self.y = y

        # Výchozí stav: políčko je zakryté
        self.covered = True

        # Výchozí stav: na políčku není mina
        self.mine = False

        # Výchozí stav: počet sousedních políček s minou
        self.adjacent_mines = 0

# Funkce pro vykreslení jednoho políčka na obrazovku
def draw_cell(screen, cell):
    # Zjistíme souřadnice levého horního rohu políčka
    x = cell.x * CELL_SIZE
    y = cell.y * CELL_SIZE

    # Pokud je políčko zakryté, vykreslíme na něj šedý čtverec
    if cell.covered:
        pygame.draw.rect(screen, (192, 192, 192), (x, y, CELL_SIZE, CELL_SIZE))
    # Jinak vykreslíme bílý čtverec a na něj buď minu, nebo počet sousedních min
    else:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, CELL_SIZE, CELL_SIZE))
        if cell.mine:
            pygame.draw.circle(screen, (255, 0, 0), (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 5)
        else:
            font = pygame.font.SysFont("comicsansms", 20)
            text = font.render(str(cell.adjacent_mines), True, (0, 0, 0))
            screen.blit
