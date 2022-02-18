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

        self.asset = asset
        self.flipped = pygame.transform.flip(self.asset.copy(), True, False)


    def getAsset(self):
        if self.dir == 1:
            return self.flipped
        return self.asset

    def move(self, x, y):
        self.x = x
        self.y = y

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

        herorealx = (self.prevx + offx * (tick % tickrate / tickrate)) * tile_width
        herorealy = (self.prevy + offy * (tick % tickrate / tickrate)) * tile_height

        return (herorealx, herorealy)

class Pokemon:
    def __init__(self, x, y, asset):
        self.x = x
        self.y = y
        self.asset = asset
        self.message = "WANNA FIGHT NOOB???"
        self.tick = 0
        self.displaymessage = False


    def talk(self):
        self.displaymessage = True
        self.tick = 1000

    def update(self):
        if(self.tick > 0):


            self.tick -= 1
        else:
            self.displaymessage = False

class Pidgey(Pokemon):
    def __init__(self,x,y,asset):
        Pokemon.__init__(self,x,y,asset)
        self.message = "I am Pidgey"
    class pidgeyAgent(Agent):
        class MyBehav(CyclicBehaviour):
            async def on_start(self):
                print("Starting Behavior....")
                self.counter = 0

            async def run(self):
                print(f"counter: {self.counter}")
                self.counter += 1
                if self.counter > 100:
                    self.kill(exit_code=10)
                    return
                await asyncio.sleep(1)

            async def on_end(self):
                print(f"Behaviour finished with exit code {self.exit_code}")

        async def setup(self):
            print("Agent is waking up....")
            self.my_behav = self.MyBehav()
            self.add_behaviour(self.my_behav)

    def start(self):
        dummy = Pidgey.pidgeyAgent("kingen@chatserver.space", "*4VVbMZ662Od")
        future = dummy.start()
        future.result()
