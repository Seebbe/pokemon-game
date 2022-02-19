import sys
import pygame

#from States.MenuState import MenuState
from States.GameState import GameState
from States.SplashState import SplashState
from States.FightState import FightState
from States.MainGame import MainGame

# State machine - Based on: https://www.youtube.com/watch?v=PZTqfag3T7M

pygame.init()
pygame.font.init()
height = 32 * 26
width = 32 * 26
screen = pygame.display.set_mode([width, height], pygame.DOUBLEBUF, 32)

states = {
    "SplashState": SplashState(),
    "GameState": GameState(),
    "FightState": FightState()
}

game = MainGame(screen, states, "SplashState")


game.run()
pygame.quit()
sys.exit()
