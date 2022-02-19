import pygame
import sys
import random
sys.path.append("../")
from States.BaseState import BaseState
import tiles as assets
import ui
import random
import math
from Pokemons import pidgey,blastoise,jigglypuff
offset = 8

"""
    The game state that handles the battle between hero-pokemon and enemy-pokemon
"""
class FightState(BaseState):
    def __init__(self):
        super(FightState, self).__init__()
        self.next_state = "GameState"



        # Alot of attributes that has to do with the buttons displayed at the bottom of the screen
        self.button_font = pygame.font.Font('img/pokemon_fire_red.ttf', 34)
        self.button_background = pygame.Rect((0, 416), (832, 416))
        self.fight_button = pygame.Rect((0 + offset, 416 + offset), (416 - offset * 2, 208 - offset * 2))
        self.heal_button = pygame.Rect((416 + offset, 416 + offset), (416 - offset * 2, 208 - offset * 2))
        self.run_button = pygame.Rect((0 + offset, 416 + offset + 208), (416 * 2 - offset * 2, 208 - offset * 2))

        self.attack1_button = pygame.Rect((0 + offset, 416 + offset), (416 - offset * 2, 208 - offset * 2))
        self.attack2_button = pygame.Rect((416 + offset, 416 + offset), (416 - offset * 2, 208 - offset * 2))
        self.attack3_button = pygame.Rect((0 + offset, 416 + offset + 208), (416 - offset * 2, 208 - offset * 2))
        self.back_button = pygame.Rect((416 + offset, 416 + offset + 208), (416 - offset * 2, 208 - offset * 2))

        # These are the buttons that display the FIGHT, HEAL and RUN
        self.main_buttons = [ui.Button(self.fight_button, self.fight_press, "FIGHT", True, self.button_font),
                             ui.Button(self.heal_button, self.heal_press, "HEAL", True, self.button_font),
                             ui.Button(self.run_button, self.run_press, "RUN", True, self.button_font)]

        # These are the buttons that displays pikachus attacks, or BACK option.
        self.attack_buttons = [ui.Button(self.attack1_button, self.attack1_press, "Skull Bash", True, self.button_font),
                               ui.Button(self.attack2_button, self.attack2_press, "Thunder Shock", True, self.button_font),
                               ui.Button(self.attack3_button, self.attack3_press, "MegaVolt", True, self.button_font),
                               ui.Button(self.back_button, self.back_press, "BACK", True, self.button_font)]

        # This list are the current active buttons that are drawn to the screen, and can be interacted with
        # By setting self.active_buttons = self.attack buttons, the attack buttons will be displayed
        self.active_buttons = [ui.Button(self.fight_button, self.fight_press, "FIGHT", True, self.button_font),
                               ui.Button(self.heal_button, self.heal_press, "HEAL", True, self.button_font),
                               ui.Button(self.run_button, self.run_press, "RUN", True, self.button_font)]

        # This variable holds what button is currently hovered, is represents what index in the self.active_buttons list the button has
        self.active_button = 0

        # Holds what tick the hero's animation is on. Can range between 0 and 7
        self.hero_animation_time = 0
        # Holds the current animation state for hero, can hold idle, tackle or projectile
        self.hero_animation_state = "idle"

        # Holds what tick the enemy's animation is on. Can range between 0 and 7
        self.enemy_animation_time = 0
        # Holds the current animation state for enemy, can hold idle, tackle or projectile
        self.enemy_animation_state = "idle"

        self.prevEnemyFightTurn = False


        self.max_animation_time = 7

        self.test = 0

        self.turn = "hero"
        self.turn_action = False


    """
        Handles the events like Mouse-input and keyboard input
    """
    def get_event(self, event):
        # If O button is pressed, change state to GameState (For testing purpose only)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                self.next_state = "GameState"
                self.done = True

        if event.type == pygame.KEYUP:
            # IF right is clicked, move the active button to the right
            if event.key == pygame.K_RIGHT:
                if self.active_button < len(self.active_buttons) - 1:
                    self.active_button += 1
            elif event.key == pygame.K_LEFT:
                # IF left is clicked, move the active button to the left
                if self.active_button > 0:
                    self.active_button -= 1
            elif event.key == pygame.K_UP:
                # IF up is clicked, move the active button two step back
                # IF active_button is outside list range, set to 0
                if self.active_button >= 2:
                    self.active_button -= 2
                    if self.active_button < 0:
                        self.active_button = 0
            elif event.key == pygame.K_DOWN:
                # IF up is clicked, move the active button two step forward
                # IF active_button is outside list range, set to last index of list
                if self.active_button >= 0:
                    self.active_button += 2
                    if self.active_button >= len(self.active_buttons):
                        self.active_button = len(self.active_buttons) - 1

            # If space is pressed, click the button that is currently active
            if event.key == pygame.K_SPACE:
                if 0 <= self.active_button < len(self.active_buttons):
                    self.active_buttons[self.active_button].click()

        # If mouse-button left is clicked, call method handle_ui with the event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.handle_ui(event)

    def update(self, dt):
        # If enemy is dead, go back to game-state
        if self.persist["enemy"].health <= 0:
            self.next_state = "GameState"
            self.done = True
        # If you died, go back to game state, and print that you died
        if self.persist["hero"].health <= 0:
            print("You have been defeated")
            self.next_state = "GameState"
            self.done = True

        # Handle mouse input
        # If mouse hoovers the button, set it to the active button
        mx, my = pygame.mouse.get_pos()
        for i in range(len(self.active_buttons)):
            button = self.active_buttons[i]
            if button.rect.collidepoint((mx, my)):
                self.active_button = i
                break

        # Handle animation for the hero
        # If animation_state is not idle, add tick by 1
        if self.hero_animation_state != "idle":
            self.hero_animation_time += 1
            if self.hero_animation_time > self.max_animation_time:
                self.hero_animation_time = 0
                self.hero_animation_state = "idle"

        # Handle animation for the enemy
        # If animation_state is not idle, add tick by 1
        if self.enemy_animation_state != "idle":
            self.enemy_animation_time += 1
            if self.enemy_animation_time > self.max_animation_time:
                self.enemy_animation_time = 0
                self.enemy_animation_state = "idle"

        if self.prevEnemyFightTurn and not self.enemy.attack_turn:
            if type(self.enemy) is blastoise.Blastoise:
                self.enemy_animation_state = "projectile"
            else:
                self.enemy_animation_state = "tackle"
        self.prevEnemyFightTurn = self.enemy.attack_turn

    """
        Main draw method for the fight state
    """
    def draw(self, surface):
        surface.fill((255, 255, 255))
        # Draws the battle background
        surface.blit(assets.battle_scene, (0,0))

        # Method that draws the pokemons
        self.draw_pokemon(surface)

        # Method that draws the health ui
        self.draw_health_ui(surface)

        # Method draws the ui
        self.draw_ui(surface)

    # Method that draws the fighting pokemons
    def draw_pokemon(self, surface):
        if 'enemy' in self.persist:

            # Draws the enemy based on it's animation state
            enemy = pygame.transform.scale(self.persist['enemy'].fight_asset, (200, 200))
            if self.enemy_animation_state == "idle":
                surface.blit(enemy, (600, 10))
            elif self.enemy_animation_state == "tackle":
                self.tackle_animation_enemy(surface, enemy, 600, 10, 200)
            elif self.enemy_animation_state == "projectile":
                self.projectile_animation_enemy(surface, enemy, 600, 10, 200, assets.water_attack)


        # Draws hero based on it's animation state
        pika = pygame.transform.scale(assets.pikachu_fighting, (300, 300))
        if self.hero_animation_state == "idle":
            surface.blit(pika, (10, 160))
        elif self.hero_animation_state == "tackle":
            self.tackle_animation_hero(surface, pika, 10, 160, 300)
        elif self.hero_animation_state == "projectile":
            self.projectile_animation_hero(surface, pika, 10, 160, 300, assets.lightning_attack)

    """
        Method that draws the health ui
    """
    def draw_health_ui(self, surface):
        self.font = pygame.font.Font('img/pokemon_fire_red.ttf', 30)
        bar_length = 300
        hero = None
        # Draws hero ui
        if 'hero' in self.persist:
            x = 9
            y = 390
            hero = self.persist['hero']
            #convert to health bar length
            hp_ratio = hero.max_health / bar_length

            pygame.draw.rect(surface, (112,248,168),(x,y,hero.health/hp_ratio,25))
            pygame.draw.rect(surface, (0,0,0),(9,390,bar_length,25),3)
            textsurface = self.font.render("HP", False, (209, 125, 46))
            surface.blit(textsurface, (313,386))

        # Draws enemy ui
        enemy = None
        if 'enemy' in self.persist:
            enemy = self.persist['enemy']
            hp_ratio2 = enemy.max_health / bar_length

            pygame.draw.rect(surface, (112,248,168),(500,220, enemy.health/hp_ratio2,25))
            pygame.draw.rect(surface, (0,0,0),(500,220,bar_length,25),3)
            textsurface2 = self.font.render("HP", False, (209, 125, 46))
            surface.blit(textsurface, (803,216))

    # Draws the tackle animation for hero based on self.hero_animation_time
    def tackle_animation_hero(self, surface, hero, x_start, y_start, scale_start):
        x = x_start + self.hero_animation_time / self.max_animation_time * 500
        y = y_start - self.hero_animation_time / self.max_animation_time * 120
        rot = 0 - self.hero_animation_time / self.max_animation_time * 40
        scale = (scale_start - self.hero_animation_time / self.max_animation_time * 100, scale_start - self.hero_animation_time / self.max_animation_time * 100)
        scaled_hero = pygame.transform.scale(hero, scale)
        rotated_hero = pygame.transform.rotate(scaled_hero, rot)
        rotated_hero_rect = rotated_hero.get_rect(center = scaled_hero.get_rect(center = (x, y)).center)
        surface.blit(rotated_hero, (x, y))

    # Draws the tackle animation for enemy based on self.enemy_animation_time
    def tackle_animation_enemy(self, surface, enemy, x_start, y_start, scale_start):
        x = x_start - self.enemy_animation_time / self.max_animation_time * 500
        y = y_start + self.enemy_animation_time / self.max_animation_time * 40
        rot = 0 + self.enemy_animation_time / self.max_animation_time * 40
        scale = (scale_start + self.enemy_animation_time / self.max_animation_time * 100, scale_start + self.enemy_animation_time / self.max_animation_time * 100)
        scaled_enemy = pygame.transform.scale(enemy, scale)
        #Rotate image around center ->  https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
        rotated_enemy = pygame.transform.rotate(scaled_enemy, rot)
        rotated_enemy_rect = rotated_enemy.get_rect(center = scaled_enemy.get_rect(center = (x, y)).center)
        surface.blit(rotated_enemy, (x, y))

    # Draws the projectile animation for hero based on self.hero_animation_time
    def projectile_animation_hero(self, surface, hero, x_start, y_start, scale_start, attack_img):
        x = x_start + self.hero_animation_time / self.max_animation_time * 100
        y = y_start - self.hero_animation_time / self.max_animation_time * 50

        rot = 0 - self.hero_animation_time / self.max_animation_time * 10
        scale = (scale_start - self.hero_animation_time / 5 * 30, scale_start - self.hero_animation_time / self.max_animation_time * 30)
        scaled_hero = pygame.transform.scale(hero, scale)
        rotated_hero = pygame.transform.rotate(scaled_hero, rot)
        rotated_hero_rect = rotated_hero.get_rect(center = scaled_hero.get_rect(center = (x, y)).center)

        #Projectile

        num_projectile = 15
        for i in range(1,num_projectile):

            projectile_x = x_start + self.hero_animation_time / self.max_animation_time * 500 * i / num_projectile + scale_start / 2
            projectile_y = y_start - self.hero_animation_time / self.max_animation_time * 150 * i / num_projectile + scale_start / 2 - 30
            if not attack_img:
                pygame.draw.circle(surface, (255,0,0), (projectile_x, projectile_y), 20)
            else:
                rotated_attack = pygame.transform.rotate(attack_img, -25)
                rotated_hero_rect = rotated_attack.get_rect(center = attack_img.get_rect(center = (x, y)).center)
                surface.blit(rotated_attack, (projectile_x, projectile_y))

                for j in range(random.randint(10, 20)):
                    pygame.draw.circle(surface, (255, 234, 0,100), (projectile_x + 16 + random.randint(0, 30) * - 1 * random.randint(0, 1), projectile_y + 16 + random.randint(0, 30) - 1 * random.randint(0, 1)), 1)


        surface.blit(rotated_hero, (x, y))

    # Draws the projectile animation for enemy based on self.enemy_animation_time
    def projectile_animation_enemy(self, surface, enemy, x_start, y_start, scale_start, attack_img):
        x = x_start - self.enemy_animation_time / self.max_animation_time * 100
        y = y_start + self.enemy_animation_time / self.max_animation_time * 50

        rot = 0 + self.enemy_animation_time / self.max_animation_time * 10
        scale = (scale_start - self.enemy_animation_time / self.max_animation_time * 5, scale_start - self.enemy_animation_time / self.max_animation_time * 5)
        scaled_enemy = pygame.transform.scale(enemy, scale)
        rotated_enemy = pygame.transform.rotate(scaled_enemy, rot)
        rotated_hero_rect = rotated_enemy.get_rect(center = scaled_enemy.get_rect(center = (x, y)).center)

        #Projectile

        num_projectile = 15
        for i in range(1, num_projectile):

            projectile_x = x_start - self.enemy_animation_time / self.max_animation_time * 580 * i / num_projectile + scale_start / 2
            projectile_y = y_start + self.enemy_animation_time / self.max_animation_time * 180 * i / num_projectile + scale_start / 2 - 30
            if not attack_img:
                pygame.draw.circle(surface, (255,0,0), (projectile_x, projectile_y), 20)
            else:
                rotated_attack = pygame.transform.rotate(attack_img, -25)
                rotated_hero_rect = rotated_attack.get_rect(center = attack_img.get_rect(center = (x, y)).center)
                surface.blit(rotated_attack, (projectile_x, projectile_y))

                for j in range(random.randint(10, 20)):
                    pygame.draw.circle(surface, (0, 0, 200,100), (projectile_x + 16 + random.randint(0, 30) * - 1 * random.randint(0, 1), projectile_y + 16 + random.randint(0, 30) - 1 * random.randint(0, 1)), 1)


        surface.blit(rotated_enemy, (x, y))

    """
        Method that handles the mouse click on button
    """
    def handle_ui(self, event):
        mx, my = pygame.mouse.get_pos()

        for button in self.active_buttons:
            if button.rect.collidepoint((mx, my)):
                button.click()

    """
        Method that draws the all the active buttons. 
        It also sets a button to active if it's the active button
    """
    def draw_ui(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.button_background)

        for i in range(len(self.active_buttons)):
            button = self.active_buttons[i]
            button.active = i == self.active_button
            button.draw(surface)

    """
        Method that's invoked when fight button is pressed
    """
    def fight_press(self):
        self.active_buttons = self.attack_buttons
        self.active_button = 0
        print("FIGHT")

    """
        Method that's invoked when heal button is pressed
    """
    def heal_press(self):
        target = self.persist['enemy']
        if target.attack_turn == False:
            if self.persist['hero'].health <= 100 and self.persist['hero'].health > 80:
                self.persist['hero'].health = 100

            else:
                self.persist['hero'].health += 20
            print(f"Pikachi heals himself up")
            target.attack_turn = True

    """
        Method that's invoked when run button is pressed
    """
    def run_press(self):
        print("You ran away!")
        self.persist['enemy'].run = False
        self.next_state = "GameState"
        self.done = True

    """
        Method that's invoked when attack1 button is pressed
    """
    def attack1_press(self):
        target = self.persist['enemy']
        hero = self.persist['hero']
        if target.attack_turn == False:
            self.hero_animation_state = "tackle"
            try:
                n = random.randint(1,10)
                if target.dodge < n:
                    dmg = 5 * target.resilience
                    target.health -= dmg
                    print(f"Attacking {target.name} with SkullBash, dealing {dmg} damage.")
                    if hero.cd_mega_volt != 0:
                        hero.cd_mega_volt -= 1
                    if hero.cd_thundershock != 0:
                        hero.cd_thundershock -= 1
                else:
                    print("Nooo, I missed my attack")
                    if hero.cd_mega_volt != 0:
                        hero.cd_mega_volt -= 1
                    if hero.cd_thundershock != 0:
                        hero.cd_thundershock -= 1
                print(hero.cd_mega_volt)
                target.attack_turn = True
            except:
                print(f"No target")

    """
        Method that's invoked when attack2 button is pressed
    """
    def attack2_press(self):
        hero = self.persist['hero']
        target = self.persist['enemy']
        if hero.cd_thundershock == 0:

            if target.attack_turn == False:
                self.hero_animation_state = "projectile"
                try:
                    n = random.randint(1,10)
                    if target.dodge < n:
                        dmg = 15 * target.resilience
                        target.health -= dmg
                        print(f"Attacking {target.name} with Thunder Shock, dealing {dmg} damage.")
                        hero.cd_thundershock = 3
                        if hero.cd_mega_volt != 0:
                                hero.cd_mega_volt -= 1
                    else:
                        print("Nooo, I missed my attack")
                        if hero.cd_mega_volt != 0:
                            hero.cd_mega_volt -= 1
                        hero.cd_thundershock = 3

                    target.attack_turn = True
                except:
                    print(f"No target")
        else:
            print("Thunder Shock still on cooldown")

    """
        Method that's invoked when attack3 button is pressed
    """
    def attack3_press(self):
        hero = self.persist['hero']
        target = self.persist['enemy']
        if target.attack_turn == False:
            try:
                if hero.cd_mega_volt == 0:
                    n = random.randint(1,10)
                    if target.dodge < n:
                        dmg = 20 * target.resilience
                        target.health -= dmg
                        print(f"Attacking {target.name} with MegaVolt, dealing {dmg} damage.")
                        print(f"MegaVolt has put {target.name} in a shocking state, unable to fight for the next turn")
                        self.hero_animation_state = "projectile"
                        hero.cd_mega_volt = 6
                        if hero.cd_thundershock != 0:
                            hero.cd_thundershock -= 1
                    else:
                        print("Nooo, I missed my attack")
                        hero.cd_mega_volt = 6
                        if hero.cd_thundershock != 0:
                            hero.cd_thundershock -= 1
                        target.attack_turn = True
                else:
                    print("MegaVolt still on cooldown")

            except:
                print(f"No target")

    """
        Method that's invoked when back button is pressed
    """
    def back_press(self):
        print("BACK")
        self.active_buttons = self.main_buttons
        self.active_button = 0
