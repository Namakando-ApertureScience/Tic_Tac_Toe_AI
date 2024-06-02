from Training_environment import Training_environment as Tr
from Asynchronous_Value_Iteration import Asynchronous as As
from Policylib import Policy as Po


class Training_place:

    def __init__(self):
        self.iterator1 = As()
        self.policy1 = Po()

        self.iterator2 = As()
        self.policy2 = Po()

        self.p1win_count = 0
        self.p2win_count = 0
        self.draw_count = 0

    def tp(self, strength_level):
        count = 0
        draws_in_a_row = 0

        boolean = True
        while boolean:

            training_game = Tr()
            print("Training games: " + str(count + 1), end='\r')

            #training_game.draw()
            #input()

            holder1 = training_game.environment.copy()
            cur_move1 = self.policy1.policy(training_game.environment)

            training_game.player('X', cur_move1)

            for j in range(4):

                #training_game.draw()
                #input()

                holder2 = training_game.environment.copy()
                cur_move2 = self.policy2.policy(training_game.environment)

                training_game.player('O', cur_move2)

                if training_game.iswin():
                    self.policy1.improve(self.iterator1.training(self.policy2, cur_move1, holder1, training_game.environment, -1))
                    self.policy2.improve(self.iterator2.training(self.policy1, cur_move2, holder2, training_game.environment, 1))
                    self.p2win_count += 1
                    draws_in_a_row = 0
                    break

                else:
                    self.policy1.improve(self.iterator1.training(self.policy2, cur_move1, holder1, training_game.environment, 0))

                #training_game.draw()
                #input()

                holder1 = training_game.environment.copy()
                cur_move1 = self.policy1.policy(training_game.environment)

                training_game.player('X', cur_move1)

                if training_game.iswin():
                    self.policy2.improve(self.iterator2.training(self.policy1, cur_move2, holder2, training_game.environment, -1))
                    self.policy1.improve(self.iterator1.training(self.policy2, cur_move1, holder1, training_game.environment, 1))
                    self.p1win_count += 1
                    draws_in_a_row = 0
                    break

                else:
                    self.policy2.improve(self.iterator2.training(self.policy1, cur_move2, holder2, training_game.environment, 0))

            if not training_game.iswin():
                self.draw_count += 1
                draws_in_a_row += 1

            if draws_in_a_row == strength_level:
                boolean = False

            count += 1

            #training_game.draw()
            #input()

        #print()

        return [self.policy1, self.policy2, self.iterator1, self.iterator2]
