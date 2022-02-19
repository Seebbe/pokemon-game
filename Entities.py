import pygame

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import sys
import asyncio
import time
import random


class Hero:
    def __init__(self, asset):
        self.x = 5
        self.y = 5
        self.dir = 0
        self.prevx = 5
        self.prevy = 5
        self.max_health = 100
        self.health = 100
        self.cd_thundershock = 0
        self.cd_mega_volt = 0

        self.asset = asset
        self.flipped = pygame.transform.flip(self.asset.copy(), True, False)

        self.animation_time = 0
        self.animation_time_max = 100

    def update(self, dt):


        if self.animation_time > 0:
            self.animation_time -= dt

            if self.animation_time <= 0:
                self.animation_time = 0
                self.prevposition()
        else:
            self.prevposition()

    def getAsset(self):
        if self.dir == 1:
            return self.flipped
        return self.asset

    def move(self, x, y):
        self.x = x
        self.y = y
        self.animation_time = self.animation_time_max

    def prevposition(self):
        self.prevx = self.x
        self.prevy = self.y

    def left(self):
        self.dir = 0

    def right(self):
        self.dir = 1

    def nearEntity(self, entities):
        near = False
        for e in entities:
            if abs(e.x - self.x) <= 1 and abs(e.y - self.y) <= 1:
                return e
        return None

    def realpositiontuple(self, tick, tickrate, tile_width, tile_height):
        offx = self.x - self.prevx
        offy = self.y - self.prevy

        herorealx = (self.prevx + offx * ((self.animation_time_max - self.animation_time) % self.animation_time_max / self.animation_time_max)) * tile_width
        herorealy = (self.prevy + offy * ((self.animation_time_max - self.animation_time) % self.animation_time_max / self.animation_time_max)) * tile_height

        return (herorealx, herorealy)


class Pokemon:
    def __init__(self, x, y, asset):
        self.x = x
        self.y = y
        self.asset = asset
        self.message = "WANNA FIGHT NOOB???"
        self.time_talking = 0
        self.displaymessage = False


    def talk(self):
        self.displaymessage = True
        self.time_talking = 1000

    def update(self, dt):

        if (self.time_talking > 0):
            self.time_talking -= dt
        else:
            self.displaymessage = False
