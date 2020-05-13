import pygame
from file_with_settings import Settings
from  file_with_ship import Ship
import file_with_functions as fwf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()


    while True:
        fwf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        fwf.update_screen(ai_settings, screen, ship, bullets)

        pygame.display.flip()


run_game()
