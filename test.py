import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class DummyAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0

        async def run(self):
            print("Counter: {}".format(self.counter))
            self.counter += 1
            if self.counter > 3:
                self.kill(exit_code=10)
                return
            await asyncio.sleep(1)

        async def on_end(self):
            print("Behaviour finished with exit code: {} ".format(self.exit_code))
    async def setup(self):
        print("Agent is waking up . . .")
        self.my_behav = self.MyBehav()
        self.add_behaviour(self.my_behav)

if __name__ == "__main__":
    dummy = DummyAgent("testhd@chatserver.space", "thD7654321")
    future = dummy.start()

    future.result()

    while not dummy.my_behav.is_killed():
        time.sleep(1)

    print("Bye Bye I was killed {}".format(str(dummy.jid)))
    dummy.stop()