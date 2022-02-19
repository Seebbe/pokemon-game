import pygame

"""
    Main-Game class which handles switching between states,
    and updating them with both events (Keyboard input etc.) 
    as well as the draw and main update loops for the states.
"""


class MainGame(object):
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    """
        Retrieves the current events and sends them to the state for processing
    """

    def event_loop(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.state.quit = True
            self.state.get_event(e)

    """
        If this method is called, the game switches to next_state.
        Whatever data is saved in state.persist is also sent to the next state.
    """

    def change_state(self, next_state):
        current_state = self.state_name
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    """
        Main update loop. This invokes an update in the current state.
        If the state is marked as done, it will invoke a change in states.
    """

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.change_state(self.state.next_state)
        self.state.update(dt)

    """
        Main draw loop. This invokes a draw call to the current state.
    """

    def draw(self):
        self.state.draw(self.screen)

    """
        Main-loop. This loop sets the fps, and calls the update, draw and event_loop.
    """

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
