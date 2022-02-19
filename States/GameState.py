import pygame
import sys
import tiles as assets
import Helper
import Entities as ent
from Pokemons import pidgey,blastoise,jigglypuff
from States.BaseState import BaseState
sys.path.append("../")

"""
    The game state where the player can walk around in a world
    and interact with pokemons.
"""
class GameState(BaseState):
    def __init__(self):
        super(GameState, self).__init__()


        # Initialises important attributes for the class
        self.tile_width = 32
        self.tile_height = 32
        self.map_width = 26
        self.map_height = 26

        self.height = 32 * 26
        self.width = 32 * 26

        self.keys = {}

        self.tick = 0
        self.tickrate = 100

        # Initializes hero
        self.hero = ent.Hero(assets.pika)

        # Initializes enemies
        self.pidgey1 = pidgey.Pidgey(4, 20, assets.pidgey, self.hero)
        self.blastoise1 = blastoise.Blastoise(4, 7, assets.blasttoise, self.hero)
        self.jiggly1 = jigglypuff.Jigglypuff(3,10, assets.jiggly,self.hero)

        # Hold what enemy the player is talking to
        self.chat_enemy = None

        # List that holds all enemies on the playing field
        self.entities = [self.jiggly1, self.pidgey1, self.blastoise1]

        # 2D array that holds the map
        self.map1 = [[11, 3, 3, 3, 3, 3, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 1, 1, 7, 9, 1, 1, 1, 0, 0, 0, 0, 0, 0, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 1, 1, 5, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 6, 10, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [4, 0, 1, 1, 1, 1, 0, 0, 0, 0, 7, 8, 8, 8, 10, 10, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 6, 10, 10, 10, 10, 10, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 12, 10, 11, 3, 3, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 4, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 9, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 7, 9, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 7, 8, 8, 8, 8, 8, 9, 1, 1, 0, 0, 0, 6, 2, 1, 1, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 1, 6, 10, 10, 10, 10, 10, 2, 1, 1, 0, 0, 0, 6, 2, 1, 1, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 1, 5, 3, 12, 10, 10, 10, 10, 9, 1, 0, 0, 7, 10, 10, 9, 1, 0, 0, 0],
                     [1, 1, 1, 0, 0, 0, 1, 1, 1, 6, 10, 10, 10, 10, 2, 1, 0, 0, 5, 3, 3, 4, 1, 1, 0, 0],
                     [1, 1, 7, 9, 0, 0, 0, 1, 1, 5, 12, 10, 11, 3, 4, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                     [1, 1, 5, 4, 0, 0, 0, 0, 1, 1, 5, 3, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                     ]

        # Pygame images that holds a pre-generated image of the map. Generated with the function Helper.generateBackgroundForeground
        self.background, self.foreground = Helper.generateBackgroundForeground(self.map1, self.map_width,
                                                                               self.map_height, self.tile_width,
                                                                               self.tile_height, self.width,
                                                                               self.height)
        # The two fonts used for chat
        self.chatfont = pygame.font.Font('img/pokemon_fire_red.ttf', 24)
        self.chatfont2 = pygame.font.Font('img/pokemon_fire_red.ttf', 34)

        # List of chat-text when talking to an enemy.
        self.testchat = [
            "What type of strange mouse are you? ",
            "I eat little animals like you for breakfast!",
            "What was that???",
            "YOU PRICK",
            "Do you want to fight?"]

        # Variables used for handling the chatting with the enemy
        self.chat_index = 0
        self.chat_active = False
        self.chat_option = 0
        self.chat_option_color = ((0, 255, 0), (255, 0, 0))

    """
        Main update loop.
    """
    def update(self, dt):
        # Updates the hero every tick
        self.hero.update(dt)

        # Update all the enemies every tick. If the enemy is dead, remove it from the entities list.
        for e in self.entities:
            if e.alive:
                e.update(dt)
            else:
                self.entities.remove(e)

        self.keys = pygame.key.get_pressed()

        # If the chat interface is not open, handle the keyboard input.
        if not self.chat_active:

            # If the hero isn't currently walking to a tile, handle input to walk to next tile
            if self.hero.animation_time <= 0:

                # If left key is pressed. Turn hero sprite left and check if left tile is walkable
                # If it is walkable (No solid object or entity), move hero 1 tile left.
                if self.keys[pygame.K_LEFT]:
                    self.hero.left()
                    if Helper.inboundSolidEntity(self.hero.x - 1, self.hero.y, self.entities, self.map_width,
                                                 self.map_height, self.map1):
                        self.hero.move(self.hero.x - 1, self.hero.y)

                # If right key is pressed. Turn hero sprite right and check if right tile is walkable
                # If it is walkable (No solid object or entity), move hero 1 tile right.
                if self.keys[pygame.K_RIGHT]:
                    self.hero.right()
                    if Helper.inboundSolidEntity(self.hero.x + 1, self.hero.y, self.entities, self.map_width,
                                                 self.map_height, self.map1):
                        self.hero.move(self.hero.x + 1, self.hero.y)

                # If up key is pressed. Check if up tile is walkable
                # If it is walkable (No solid object or entity), move hero 1 tile up.
                if self.keys[pygame.K_UP]:
                    if Helper.inboundSolidEntity(self.hero.x, self.hero.y - 1, self.entities, self.map_width,
                                                 self.map_height, self.map1):
                        self.hero.move(self.hero.x, self.hero.y - 1)

                # If down key is pressed. Check if down tile is walkable
                # If it is walkable (No solid object or entity), move hero 1 tile down.
                if self.keys[pygame.K_DOWN]:
                    if Helper.inboundSolidEntity(self.hero.x, self.hero.y + 1, self.entities, self.map_width,
                                                 self.map_height, self.map1):
                        self.hero.move(self.hero.x, self.hero.y + 1)

    # Method that handles keyboard and mouse input
    def get_event(self, event):
        # If the chat is not open
        if not self.chat_active:

            # If a space-key was released, find an enemy within 1 tile of hero, and interact with it if the enemy was close by.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    e = self.hero.nearEntity(self.entities)
                    if e:
                        print("INTERACT with ", e)
                        self.chat_enemy = e
                        self.chat_active = True
        # If the chat interface is open.
        else:
            e = self.hero.nearEntity(self.entities)

            # If space-key was released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    # Go to next chat-dialog
                    print("GO TO NEXT")
                    self.chat_index += 1

                    # If the chat-index is larger than the number of chat dialoges
                    if self.chat_index >= len(self.testchat):
                        self.chat_index = 0
                        self.chat_active = False

                        # Check what option the player choose. self.chat_option 0 = yes, 1 = no
                        # If player says yes to fight, transition to fight state
                        # If the player said no, chat interface will close
                        if self.chat_option == 0:
                            if e:
                                print(e)
                                self.hero.health = 100
                                self.persist['enemy'] = e
                                self.persist['hero'] = self.hero
                                e.run = True
                                e.start(self.persist)

                            # Invokes state-change on next game tick to FightState
                            self.next_state = "FightState"
                            self.done = True

                            self.chat_option = 0

                # If escape-key was pressed, close chat-interface
                elif event.key == pygame.K_ESCAPE:
                    self.chat_index = 0
                    self.chat_active = False

                # If player is on the last chat-text, pressing left or right will switch between the chat options
                if self.chat_index == len(self.testchat) - 1:
                    if event.key == pygame.K_LEFT:
                        self.chat_option = 0
                    elif event.key == pygame.K_RIGHT:
                        self.chat_option = 1

    """
        Main draw method for GameState
    """
    def draw(self, surface):
        surface.fill((255, 255, 255))

        # Draws the pre-rendered background to the screen
        surface.blit(self.background, (0, 0))

        # Loops through all pokemons and draws them if they are alive
        for e in self.entities:
            if e.alive:
                x = e.x * self.tile_width + 16 - e.asset.get_width() / 2
                y = e.y * self.tile_height + 16 - e.asset.get_height() / 2
                surface.blit(e.asset, (x,y))


        # Draw hero
        surface.blit(self.hero.getAsset(),
                     self.hero.realpositiontuple(self.tick, self.tickrate, self.tile_width, self.tile_height))

        # Draws the pre-rendered foreground on top of everything
        surface.blit(self.foreground, (0, 0))

        # Draw entity text - currently obsolete
        """        
        for e in self.entities:
            if (e.displaymessage):
                textsurface = self.font.render(e.message, False, (0, 0, 0))

                tx = e.x * self.tile_width - textsurface.get_width() / 4
                ty = e.y * self.tile_height - 20

                pygame.draw.rect(surface, (255, 255, 255, 100),
                                 (tx - 4, ty - 4, textsurface.get_width() + 8, textsurface.get_height() + 8))
                surface.blit(textsurface, (tx, ty))
        """

        # If the chat is active - Draw the chat
        if (self.chat_active):

            # Draws a white rectacle at bottom of screen
            pygame.draw.rect(surface, (255, 255, 255, 50),
                             (0, self.height - self.height / 5, self.width, self.height / 5))

            # If there exists an enemy that the player is talking to, draw it's asset in the white box
            if self.chat_enemy:
                surface.blit(pygame.transform.scale(pygame.transform.flip(self.chat_enemy.fight_asset, -1, 0), (128,128)),
                            (10, self.height - self.height / 5 + 10, self.width, self.height / 5 + 10))

            # Renders a multi-line text in the white box
            textsurface = self.chatfont.render(self.testchat[self.chat_index], False, (0, 0, 0))
            surface_width = 150
            if textsurface.get_width() >= self.width - surface_width * 2:
                Helper.box_text(surface, self.chatfont, surface_width, self.width - surface_width,
                                self.height - self.height / 5 + 10, self.testchat[self.chat_index], (0, 0, 0))
            else:
                surface.blit(textsurface,
                             (self.width / 2 - textsurface.get_width() / 2, self.height - self.height / 5 + 10))

            # If the chat-text is the yes-no option
            if self.chat_index == len(self.testchat) - 1:

                if (self.chat_option == 0):
                    yes_color = (0, 255, 0)
                    no_color = (255, 0, 0)
                else:
                    yes_color = (255, 0, 0)
                    no_color = (0, 255, 0)

                # Renders the Yes or No options, with different colors based on what option is choosen
                textsurface_YES = self.chatfont2.render("YES", False, yes_color)
                textsurface_OR = self.chatfont2.render("or", False, (255, 0, 0))
                textsurface_NO = self.chatfont2.render("NO", False, no_color)

                full_width = textsurface_YES.get_width() + textsurface_OR.get_width() + textsurface_NO.get_width() + 40
                text_x = self.width / 2 - full_width / 2
                text_y = self.height - textsurface.get_height() * 2 - 10
                surface.blit(textsurface_YES, (text_x, text_y))
                surface.blit(textsurface_OR, (text_x + textsurface_YES.get_width() + 10, text_y))
                surface.blit(textsurface_NO,
                             (text_x + textsurface_YES.get_width() + textsurface_OR.get_width() + 20, text_y))

            else:
                #Renders text that says "Press space to continue"
                textsurface = self.chatfont2.render("PRESS SPACE TO CONTINUE", False, (0, 0, 0))
                surface.blit(textsurface, (
                self.width / 2 - textsurface.get_width() / 2, self.height - textsurface.get_height() * 2 - 10))
