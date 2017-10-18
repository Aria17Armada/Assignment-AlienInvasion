from background import Background
from settings import Settings
import pygame
import game_functions as gf
from pygame.sprite import Group
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width,
                                      ai_settings.height))
    ship = Ship(ai_settings, screen)
    pygame.display.set_caption("For The True Emperor!")
    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)
    # Start the main loop for the game.

    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, play_button, sb, ship, aliens, bullets)


        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            gf.update_alien(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(screen, ai_settings, sb, ship, stats, bullets, aliens, play_button)

       
        ship.blitme()
        ship.update()
            # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

