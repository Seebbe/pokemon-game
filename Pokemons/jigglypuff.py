from Entities import Pokemon
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State
import sys
import tiles as assets
sys.path.append("../")
from Pokemons.Attack import Base_attack as auto
import asyncio
import time
import random

"""
    Declaring all the states that the agent should have and be able to transist to.

"""


STATE_ONE = "STATE_ONE"
STATE_TWO = "STATE_TWO"
STATE_THREE = "STATE_THREE"
STATE_FOUR = "STATE_FOUR"
STATE_FIVE = "STATE_FIVE"
STATE_SIX = "STATE_SIX"


"""
    Windows have a issue where they get stucked in a loop that leads to a crash.
    This statement looks if the system is that kind of systems and then prevent that kind of crash.
"""

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


"""
    Defining jigglypuff class and inheriting attributes from Pokemon class / entity.
    Instansiating the Pokemon constructor aswell so we can overide values from the parent class that we
    want to in this class, but also setting class specific attributes.

    auto.Attack: refers to Attack class.
    assets.jigglypuff_fighting: Picture/asset of jigglypuff when he is fighting

"""


class Jigglypuff(Pokemon):
    def __init__(self, x, y,asset,hero):
        Pokemon.__init__(self, x, y,asset)
        self.message = "I am Jigglypuff"
        Jigglypuff.health = 100
        Jigglypuff.current_hp = 100
        Jigglypuff.max_health = 100
        Jigglypuff.dodge = 0
        Jigglypuff.resilience = 1
        Jigglypuff.alive = True
        Jigglypuff.hero = hero
        Jigglypuff.run = True
        Jigglypuff.name = "Jigglypuff"
        Jigglypuff.attack_turn = False
        Jigglypuff.attack = auto.Attack(5, "Jigglypuff Attack!")
        Jigglypuff.fight_asset = assets.jiggly_fighting




    """
    Agent behavior on start and on end. Using Finite State Machine Behvaiour as argument.
    We just wanted to print something to make sure that the agent is starting and ending where we want.
    And then put the actual behavior in the states so the agent can behave differently based on what happens
    in a pokemon fight.

    """

    class Jigglypuffbehaviour(FSMBehaviour):
        async def on_start(self):
            print("Starting Jigglypuff Agent")


        async def on_end(self):
            print(f"Behaviour finished with exit code {self.exit_code}")
            await self.agent.stop()


    """
    Blueprint for our agent states.

    Here we wanted to be able to make the agent act in different ways based on what happens in the pokemon fight.
    Therefore we load in from our dictionary both the enemy which in this case is jigglypuff
    and the Hero which will represent the player. How the import of the dictonary works we will
    go through more deeply in the start function at the bottom of this file where we actually starts
    our agent.

    We have based our states on the health of the Agent where it goes into a new stage when
    the health has reached a certain level. The logic behind each state and how the fighting is going
    is that the agent has an attribute attack_turn. Which we are setting to False when the Agent has attacked
    which makes the Agent unable to attack again. When the player or the "hero" has made an attack of their choise,
    attack_turn for the Agent will be set to True again making the Agent available to attack again. For each state we have a while
    loop that is repeating the logic until the health has reached a certain level where the loop brakes and the agent move on to the next state.
    If the pokemon is defeated we are setting the attribute alive to False which makes the Pokemon dissapear from the map.
    If you kill, lose or run away from the Pokemon, the Agent is stopped.

    """


    class StateOne(State):
        async def run(self):
            enemy = self.get("enemy")["enemy"]
            hero = self.get("enemy")["hero"]
            print(enemy.attack.damage)
            print("STATE ONE")
            while enemy.alive == True and enemy.run == True:
                if hero.health <= 0:
                    self.set_next_state(STATE_TWO)
                    break
                time.sleep(1)
                if enemy.attack_turn:
                    print(f"Jigglypuff attack Pikachu, dealing {enemy.attack.damage} damage")
                    hero.health-=enemy.attack.damage
                    time.sleep(1)
                    enemy.attack_turn = False
                else:
                    pass
                if enemy.health <= 90:
                    print(f"{enemy} health is going down im going BERSERK")

                    self.set_next_state(STATE_TWO)
                    break
            print(f"New health {enemy.health}")

    class StateTwo(State):
        async def run(self):
            enemy = self.get("enemy")["enemy"]
            hero = self.get("enemy")["hero"]
            print(f"State TWO!")

            enemy.attack.damage = 7
            while enemy.alive == True and enemy.run == True:
                if hero.health <= 0:
                    self.set_next_state(STATE_THREE)
                    break

                time.sleep(1)
                if enemy.attack_turn:
                    print(f"Jigglypuff attack Pikachu, dealing {enemy.attack.damage} damage")
                    hero.health-=enemy.attack.damage
                    enemy.attack_turn = False
                else:
                    pass
                if enemy.health <= 75:
                    print("I will recover from you!!")
                    self.set_next_state(STATE_THREE)
                    break

    class StateThree(State):
        async def run(self):
            enemy = self.get("enemy")["enemy"]
            hero = self.get("enemy")["hero"]

            print(f"State THREE!")
            while enemy.alive == True and enemy.run == True:
                if hero.health <= 0:
                    self.set_next_state(STATE_FOUR)
                    break
                time.sleep(1)
                if enemy.attack_turn:
                    print(f"Jigglypuff attack Pikachu, dealing {enemy.attack.damage} damage")
                    hero.health-=enemy.attack.damage
                    enemy.attack_turn = False
                else:
                    pass

                if enemy.health <= 60:
                    print("I will recover from you!")
                    self.set_next_state(STATE_FOUR)
                    break

    #State four
    #Gain damage resilience
    class StateFour(State):
        async def run(self):
            enemy = self.get("enemy")["enemy"]
            hero = self.get("enemy")["hero"]
            print(f"State FOUR!")
            enemy.resilience = 0.8
            while enemy.alive == True and enemy.run == True:
                if hero.health <= 0:
                    self.set_next_state(STATE_FIVE)
                    break
                time.sleep(1)
                if enemy.attack_turn:
                    print(f"Jigglypuff attack Pikachu, dealing {enemy.attack.damage} damage")
                    hero.health-=enemy.attack.damage
                    enemy.attack_turn = False
                else:
                    pass
                if enemy.health <= 40:
                    print("You should run you silly!!")
                    self.set_next_state(STATE_FIVE)
                    break
    #STATE 5
    #Gain Dodge chance
    class StateFive(State):
        async def run(self):
            enemy = self.get("enemy")["enemy"]
            hero = self.get("enemy")["hero"]
            enemy.dodge = 2
            print(f"State FIVE!")
            while enemy.alive == True and enemy.run == True:
                if hero.health <= 0:
                    self.set_next_state(STATE_SIX)
                    break
                time.sleep(1)
                if enemy.attack_turn:
                    print(f"Jigglypuff attack Pikachu, dealing {enemy.attack.damage} damage")
                    hero.health-=enemy.attack.damage
                    enemy.attack_turn = False
                else:
                    pass
                if enemy.health <= 20:
                    print("I will never escape me!")
                    self.set_next_state(STATE_SIX)
                    break

    #LAST STATE
    #Gain more damage and a heal and more dodge
    class StateSix(State):
        async def run(self):
            enemy = self.get("enemy")["enemy"]
            hero = self.get("enemy")["hero"]
            print(f"State SIX!")

            enemy.dodge = 4

            enemy.health += 15
            while enemy.alive == True and enemy.run == True:
                if hero.health <= 0:
                    break

                time.sleep(1)
                if enemy.attack_turn:
                    print(f"Jigglypuff attack Pikachu, dealing {enemy.attack.damage} damage")
                    hero.health-=enemy.attack.damage
                    enemy.attack_turn = False
                else:
                    pass
                if enemy.health <= 0:
                    enemy.alive = False
                    print("You have defeated Jigglypuff")
                    hero.health = 100
                    hero.cd_thundershock = 0
                    hero.cd_mega_volt = 0
                    break


    #async def setup(self):
        #print("Agent is waking up....")
        #self.my_behav = self.Jigglypuffbehaviour()
        #self.add_behaviour(self.my_behav)


    """
    Here we are adding all the states to our Agent so it knows what states it is capable of.
    The name is reffering to the name of the state and the state is the actual class for the state of the agent.
    Initial = True is telling the agent that this is the first state,

    Then we are adding the transition for the stages so when we are breaking the while loop
    and refering to a new state the agent knows where to go next.

    With the add_behaviour method we are adding this behaviors to the Agent.

    """
    class JigglypuffAgent(Agent):
        async def setup(self):
            fsm = Jigglypuff.Jigglypuffbehaviour()
            #States
            fsm.add_state(name=STATE_ONE, state=Jigglypuff.StateOne(), initial=True)
            fsm.add_state(name=STATE_TWO, state=Jigglypuff.StateTwo())
            fsm.add_state(name=STATE_THREE, state=Jigglypuff.StateThree())
            fsm.add_state(name=STATE_FOUR, state=Jigglypuff.StateFour())
            fsm.add_state(name=STATE_FIVE, state=Jigglypuff.StateFive())
            fsm.add_state(name=STATE_SIX, state=Jigglypuff.StateSix())

            #Transitions
            fsm.add_transition(source=STATE_ONE, dest=STATE_TWO)
            fsm.add_transition(source=STATE_TWO, dest=STATE_THREE)
            fsm.add_transition(source=STATE_THREE, dest=STATE_FOUR)
            fsm.add_transition(source=STATE_FOUR, dest=STATE_FIVE)
            fsm.add_transition(source=STATE_FIVE, dest=STATE_SIX)

            self.add_behaviour(fsm)



    """
    Here we are defing a function that we are using when we want to start the agent,
    the reason for this is that we want to start the agent when we are challenging the Pokemon,
    and not before or when this file is executed as the main.

    We are using our XMPP crendentials for the agent.

    Dummy.set is a way to store data in the dummy agent where "enemy" is the key and persist is the value.
    We can access this data with: self.get("enemy")
    persist = {
            "enemy": enemy.object
            "hero" : hero.object
    }
    When we are calling the start function we are also loading the dict with what enemy the hero is challening.
    See GameState.py row 157-161


    """
    def start(self,persist):
        try:
            dummy = Jigglypuff.JigglypuffAgent("kingen@chatserver.space", "*4VVbMZ662Od")
            future = dummy.start()
            dummy.set("enemy", persist)
            future.result()
        except ConnectionError as e:
            print(e)
