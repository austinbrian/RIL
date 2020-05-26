import numpy as np


class Board:
    """
    Object to describe the overall layout available to the reinforcement agent.
    size: size/shape of the board
    """

    def __init__(
        self, size=5, reward=None,
    ):
        self.size = size
        self.reward = reward

    def render():
        pass


class Agent:
    """
    Agent is the robot doing the checking
    """

    def __init__(
        self, policy=None, initial_state=None,
    ):
        self.policy = policy
        self.state = state
        self.gamma = policy["gamma"]

    def step(self):
        # update reward
        pass


if __name__ == "__main__":
    env = Board(size=5, reward=[-1, -1, -1, -1, 10])
    agent = Agent(policy={"gamma": 0.75})
