import numpy as np


class Policy:

    def __init__(self):
        self.policy_function = {}

    def policy(self, state):

        possible_actions = np.array([])

        if str(state) in self.policy_function:
            for action in self.policy_function[str(state)]:
                possible_actions = np.append(possible_actions, action)

        else:
            count = 0
            for row in state:
                for column in row:
                    count += 1
                    if column == ' ':
                        possible_actions = np.append(possible_actions, count)

        return int(np.random.choice(possible_actions))

    def improve(self, improvement):
        self.policy_function[str(improvement[0])] = improvement[1]