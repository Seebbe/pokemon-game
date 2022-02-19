import pygame

"""
   Parent class for all States. This class has all methods and attributes
   That are required of every state.
"""
class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font('img/pokemon_fire_red.ttf', 16)

    """
        Startup method. Is called every time the state starts. 
        Saves data that was sent from previous state in self.persist
    """
    def startup(self, persistent):
        self.persist = persistent
        if "enemy" in self.persist:
            self.enemy = self.persist['enemy']

    """
        Method that handles mouse and keyboard events
    """
    def get_event(self, event):
        pass

    """
        Method that is updated once every 1/30 seconds.
        Used for logical updates
    """
    def update(self, dt):
        pass

    """
        Method that is updated once every 1/30 seconds.
        Used for drawing 
    """
    def draw(self, surface):
        pass
