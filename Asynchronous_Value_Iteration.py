import numpy as np


def simulation(old_state, action, number_possible_actions):
    s = old_state.copy()

    if number_possible_actions % 2 == 0:
        symbol = 'O'
    else:
        symbol = 'X'

    for i in range(3):
        if (i * 3) + 1 <= action <= (i + 1) * 3 and s[i][(action - 1) % 3] == ' ':
            s[i][(action - 1) % 3] = symbol
    return s


class Asynchronous:

    def __init__(self):
        self.value_function = {}

    def training(self, model, cur_move, old_state, new_state, reward):

        if reward == 1:
            self.value_function[str(old_state)] = 1
            return [old_state, str(cur_move)]

        elif reward == -1:
            self.value_function[str(new_state)] = -1

        ################################################################################################################

        possible_actions = np.array([])

        count = 0
        for row in old_state:
            for column in row:
                count += 1
                if column == ' ':
                    possible_actions = np.append(possible_actions, count)

        ################################################################################################################

        action_list = np.array([])
        maximum = -1000

        for action in possible_actions:

            between_state = simulation(old_state, int(action), len(possible_actions))

            value = 0
            count = 0
            if str(between_state) in model.policy_function:

                next_possible_actions = model.policy_function[str(between_state)]

                for next_action in next_possible_actions:
                    count += 1
                    if str(simulation(between_state, int(next_action),
                                      len(possible_actions) - 1)) in self.value_function:
                        value += (1 / count) * (self.value_function[str(simulation(between_state, int(next_action),
                                                                                   len(possible_actions) - 1))] - value)

                    else:
                        value = (1 - (1 / count)) * value

            else:

                next_possible_actions = np.setdiff1d(possible_actions, action)

                for next_action in next_possible_actions:
                    count += 1
                    if str(simulation(between_state, int(next_action),
                                      len(next_possible_actions))) in self.value_function:
                        value += (1 / count) * (self.value_function[str(simulation(between_state, int(next_action),
                                                                                   len(possible_actions) - 1))] - value)
                    else:
                        value = (1 - (1 / count)) * value

            if value > maximum:
                maximum = value
                action_list = np.array([])
                action_list = np.append(action_list, action)

            elif value == maximum:
                action_list = np.append(action_list, action)

        ################################################################################################################

        self.value_function[str(old_state)] = maximum

        ################################################################################################################

        concatenation = ""
        for action in action_list:
            concatenation += str(int(action))

        return [old_state, concatenation]
