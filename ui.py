import pygame
import sys
import tiles as assets

"""
    Button class. Has a text, font, pygame.rect and action attribues
"""
class Button:
    def __init__(self, rect, action, text, show, font):
        self.rect = rect
        self.action = action
        self.text = text
        self.show = show
        self.font = font
        self.active = False



    def update(self, dt):
        pass

    # If the button is clicked, invoke the its action
    def click(self):
        if callable(self.action):
            self.action()

    # Draw function, if the button is active, draw different asset
    def draw(self, surface):
        # If the button is supposed to be shown, draw button
        if self.show:

            if self.active:
                if self.rect.width > 500:
                    surface.blit(assets.box2, (self.rect.x, self.rect.y))
                else:
                    surface.blit(assets.box1, (self.rect.x, self.rect.y))
            else:
                if self.rect.width > 500:
                    surface.blit(assets.box2_hover, (self.rect.x, self.rect.y))
                else:
                    surface.blit(assets.box1_hover, (self.rect.x, self.rect.y))
            # Draw button text
            button_text = self.font.render(self.text, True, (16, 4, 4))
            button_text_rect = button_text.get_rect(center=(self.rect.center))
            surface.blit(button_text, button_text_rect)