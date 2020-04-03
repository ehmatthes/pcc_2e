from random import random

import pygame

from alien_invasion import AlienInvasion

class AIPlayer:

    def __init__(self, ai_game):
        """Automatic player for Alien Invasion."""

        # Need a reference to the game object.
        self.ai_game = ai_game

    def run_game(self):
        """Replaces the original run_game(), so we can interject our own
        controls.
        """

        # Start out in an active state, and hide the mouse.
        self.ai_game.stats.game_active = True
        pygame.mouse.set_visible(False)

        # Speed up the game for development work.
        self._modify_speed(5)

        # Get the full fleet size.
        self.fleet_size = len(self.ai_game.aliens)

        # Start the main loop for the game.
        while True:
            # Still call ai_game._check_events(), so we can use keyboard to
            #   quit. Also call our own method to initiate events.
            self.ai_game._check_events()
            self._implement_strategy()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()

            self.ai_game._update_screen()

    def _implement_strategy(self):
        """Implement an automated strategy for playing the game."""
        
        # Get specific alien to chase.
        target_alien = self._get_target_alien()

        # Move toward target alien.
        ship = self.ai_game.ship
        if ship.rect.x < target_alien.rect.x:
            ship.moving_right = True
            ship.moving_left = False
        elif ship.rect.x > target_alien.rect.x:
            ship.moving_right = False
            ship.moving_left = True

        # Fire a bullet whenever possible.
        firing_frequency = 1.0
        if random() < firing_frequency:
            self.ai_game._fire_bullet()

    def _get_target_alien(self):
        """Get a specific alien to target."""
        # Find the right-most alien in the bottom row.
        #   Pick the first alien in the group. Then compare all others, 
        #   and return the alien with the greatest x and y rect attributes.
        target_alien = self.ai_game.aliens.sprites()[0]
        for alien in self.ai_game.aliens.sprites():
            if alien.rect.y > target_alien.rect.y:
                # This alien is farther down than target_alien.
                target_alien = alien
            elif alien.rect.y < target_alien.rect.y:
                # This alien is above target_alien.
                continue
            elif alien.rect.x > target_alien.rect.x:
                # This alien is in the same row, but farther right.
                target_alien = alien
        
        return target_alien

    def _sweep_right_left(self):
        """Sweep the ship right and left continuously."""
        ship = self.ai_game.ship
        screen_rect = self.ai_game.screen.get_rect()

        if not ship.moving_right and not ship.moving_left:
            # Ship hasn't started moving yet; move to the right.
            ship.moving_right = True
        elif (ship.moving_right
                    and ship.rect.right > screen_rect.right - 10):
            # Ship about to hit right edge; move left.
            ship.moving_right = False
            ship.moving_left = True
        elif ship.moving_left and ship.rect.left < 10:
            ship.moving_left = False
            ship.moving_right = True

    def _modify_speed(self, speed_factor):
        self.ai_game.settings.ship_speed *= speed_factor
        self.ai_game.settings.bullet_speed *= speed_factor
        self.ai_game.settings.alien_speed *= speed_factor

if __name__ == '__main__':
    ai_game = AlienInvasion()

    ai_player = AIPlayer(ai_game)
    ai_player.run_game()