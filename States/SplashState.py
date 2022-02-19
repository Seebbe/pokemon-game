import pygame
from States.BaseState import BaseState
import tiles as assets

"""
    State that shows a splash screen to the user for 10000 game ticks.
"""
class SplashState(BaseState):
    def __init__(self):
        super(SplashState, self).__init__()
        self.time_alive = 0
        self.next_state = "GameState"
        self.font = pygame.font.Font('img/pokemon_fire_red.ttf', 32)

    """
        If space is clicked, set time_alive > 10000 which will change the state
    """
    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.time_alive = 100000000

    """
        Calculates current time_alive, if the state has been alive 
        for more than 10000 game ticks, set state to done.        
    """
    def update(self, dt):
        self.time_alive += dt
        if self.time_alive >= 10000:
            print("CHANGE STATE")
            self.done = True

    """
        Draws the splash screen
    """
    def draw(self, surface):
        surface.fill((0, 0, 0))

        percent = self.time_alive / 5000

        # Draws pokemon logo, as well as Venusaur, Blastoise and Charizard to the screen.
        surface.blit(assets.poke_logo, (155, 10))
        surface.blit(assets.venu_splash, (180, 130))
        surface.blit(assets.char_splash, (500, 150))
        surface.blit(assets.blast_splash, (-100, 170))

        # Draws out text to the screen, which moves down-right based on how long the time
        x = 100 + percent * 100
        y = 100 + percent * 70
        textsurface = self.font.render("A Pokemon game by:", False, (0, 255, 0))
        textsurface2 = self.font.render("Alex, Johan, Sebastian and Tobias:", False, (0, 255, 0))
        surface.blit(textsurface, (x, y))
        surface.blit(textsurface2, (x + 40, y + 20))
