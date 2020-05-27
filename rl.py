import numpy as np


class Board:
    """
    Object to describe the overall layout available to the reinforcement agent.
    shape: size/shape of the board
    """

    def __init__(
        self, shape=(1, 5), reward=None,
    ):
        self.board = np.zeros(shape)
        self.reward = np.array(reward)

        # Simple shape-checking
        if self.board.shape == self.reward.shape:
            self.reward = np.array(reward)
        else:
            try:
                self.reward.reshape(self.board.shape)
            except:
                raise ("Incompatible reward and size")

        self.shape = self.board.shape

    def render(self):
        """
        Show the board in ASCII graphics, with rewards per location
        """
        # loaded = self.reward.reshape(self.board.shape)
        rows, cols = self.board.shape
        vals = self.reward.reshape((rows * cols))  # flatten it out
        left = "|"
        right = "|"
        # make a little box for each reward to generate a "board"
        board_row = left + "|".join([f" {v} " for v in vals[:cols]]) + right
        # put the X in what is the same box
        return board_row

    def __repr__(self):
        board_row = self.render()

        top = "_"
        return f"""{'_'*len(board_row)}\n{board_row}\n{'_'*len(board_row)}"""


class Agent:
    """
    Agent is the robot doing the checking; keeper of the reward status
    """

    def __init__(self, policy=None, initial_state=None, gamma=None, eps=None):
        self.state = initial_state
        self.gamma = gamma
        self.eps = eps
        self.reward = 0
        _num_actions = 2
        self._actions = dict(zip(range(_num_actions), ["left", "right"]))
        self.policy = self.apply_policy(policy)

    def step(self):
        # update reward
        """
        Return:
            observation: Board object
            reward: 
            done
            info
        """

        # TODO: take random action
        pass

    def check_policy(self, policy):
        return dict(zip(self._actions.values(), policy))

    def apply_policy(self, policy):
        return self.check_policy(policy)

    def check_eps_value(self):
        if self.eps:
            if np.random.uniform(0, 1) < self.eps:
                return True
        else:
            return False


class Critic:
    """Device to assess the Agent's actions vs the Board and Policy.
    The Critic is the keeper of the policy
    """

    def __init__(self, env: Board, actor: Agent):
        self.env = env
        self.actor = actor

    def interpret_policy(self):
        p = np.array(self.actor.policy)
        b = np.array(self.env.board)
        if p.shape == b.shape:
            return p
        else:
            s = np.broadcast(p, b.reshape(p.shape))
            return s


def set_random_initial_state(env: Board):
    np.random.choice(range(self.size))
    pass


if __name__ == "__main__":
    env = Board(shape=(1, 5), reward=[-1, -1, -1, -1, 10])
    # initialize the agent with a policy of always left (100%, 0%)
    policy_always_left = np.tile([1, 0], env.shape)
    # agent = Agent(policy=[0.1, 0.9], gamma=0.75)
    agent = Agent(policy=policy_always_left, gamma=0.75)
    crtiic = Critic(env, agent)

    print(env)
    for _ in range(50):
        pass
