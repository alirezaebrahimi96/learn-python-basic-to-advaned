import sys
from settings import Settings
import pygame
from ship import Ship


class AlienInvansion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption('Alien Invansion')
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)

    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self.update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.ship.rect.x += 1
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvansion()
    ai.run_game()

