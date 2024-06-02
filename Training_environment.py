import numpy as np


class Training_environment:

    def __init__(self):
        self.environment = np.array([[' ', ' ', ' '],
                                     [' ', ' ', ' '],
                                     [' ', ' ', ' ']])

    def draw(self):
        for i in self.environment:
            print(i)

    def iswin(self):
        for i in self.environment:
            if np.all(i == i[0]) and i[0] != ' ':
                return True

        environment = np.transpose(self.environment)

        for i in environment:
            if np.all(i == i[0]) and i[0] != ' ':
                return True

        if self.environment[0][0] == self.environment[1][1] and self.environment[0][0] == self.environment[2][2] and \
                self.environment[0][0] != ' ':
            return True

        if self.environment[0][2] == self.environment[1][1] and self.environment[0][2] == self.environment[2][0] and \
                self.environment[0][2] != ' ':
            return True

        return False

    def player(self, symbol, n):
        for i in range(3):
            if (i * 3) + 1 <= n <= (i + 1) * 3 and self.environment[i][(n - 1) % 3] == ' ':
                self.environment[i][(n - 1) % 3] = symbol
