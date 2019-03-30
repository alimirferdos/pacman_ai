import pygame
from pacman_ai import Game

if __name__ == '__main__':
    game = Game.Game()
    game.start_game()
    pygame.quit()
