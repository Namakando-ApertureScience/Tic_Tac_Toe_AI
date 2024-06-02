from Training_environment import Training_environment as Tr
from Training_place import Training_place as Tp
import numpy as np


pin1 = True
while pin1:
    game = Tr()
    possible_moves = np.arange(1, 10)
    count = 0

    print()
    print("Hello, you're playing Tic_Tac_Toe. (Use the keys 1-9 to play!)")
    one_or_two = int(input("Would you like to play 1 or 2 player? (1/2) ")) == 2

    if one_or_two:
        game.draw()
        n = 0

        ################

        pin2 = True
        while pin2:
            n = int(input("Player1 to move. "))
            if n in possible_moves:
                pin2 = False

        possible_moves = np.setdiff1d(possible_moves, n)

        ################

        game.player('X', n)
        game.draw()

        for i in range(4):
            count += 1

            ################

            pin2 = True
            while pin2:
                n = int(input("Player2 to move. "))
                if n in possible_moves:
                    pin2 = False

            possible_moves = np.setdiff1d(possible_moves, n)

            ################

            game.player('O', n)
            game.draw()

            ################

            if game.iswin():
                break
            count += 1

            ################

            pin2 = True
            while pin2:
                n = int(input("Player1 to move. "))
                if n in possible_moves:
                    pin2 = False

            possible_moves = np.setdiff1d(possible_moves, n)

            ################

            game.player('X', n)
            game.draw()

            ################

            if game.iswin():
                break

    # #######################################################################################################################

    else:
        po = Tp()
        n = int(input("What strength level should the bot have? (hint: Provide an integer between 10 and 5000): "))
        policy = po.tp(n)

        print()
        print("length of the policy1: " + str(len(policy[0].policy_function)))
        print("length of the value1: " + str(len(policy[2].value_function)))
        print("Sigma1: " + str(len(policy[0].policy_function) + len(policy[2].value_function)))
        print()

        print("length of the policy2: " + str(len(policy[1].policy_function)))
        print("length of the value2: " + str(len(policy[3].value_function)))
        print("Sigma2: " + str(len(policy[1].policy_function) + len(policy[3].value_function)))
        print()

        print("|Sigma1 - Sigma2|: " + str(abs((len(policy[0].policy_function) + len(policy[2].value_function)) -
                                              (len(policy[1].policy_function) + len(policy[3].value_function)))))
        print()

        print("policy1 win count: " + str(po.p1win_count))
        print("policy2 win count: " + str(po.p2win_count))
        print("draw count: " + str(po.draw_count))
        print()

        pin3 = True
        while pin3:
            game = Tr()
            possible_moves = np.arange(1, 10)
            count = 0

            player1_or_player2 = int(input("Would you like to be player1 or player2? (1/2) ")) == 1

            if player1_or_player2:
                game.draw()

                ################

                pin2 = True
                while pin2:
                    n = int(input("Player1 to move. "))
                    if n in possible_moves:
                        pin2 = False

                possible_moves = np.setdiff1d(possible_moves, n)

                ################

                game.player('X', n)
                game.draw()

                for i in range(4):
                    count += 1

                    ################

                    old_position = game.environment.copy()
                    move = policy[1].policy(game.environment)

                    possible_moves = np.setdiff1d(possible_moves, move)

                    game.player('O', move)

                    if str(old_position) in policy[3].value_function:
                        print("Eval: " + str(policy[3].value_function[str(old_position)]))
                    else:
                        print("Eval: -")

                    game.draw()

                    ################

                    if game.iswin():
                        break
                    count += 1

                    ################

                    pin2 = True
                    while pin2:
                        n = int(input("Player1 to move. "))
                        if n in possible_moves:
                            pin2 = False

                    possible_moves = np.setdiff1d(possible_moves, n)

                    ################

                    game.player('X', n)
                    game.draw()

                    ################

                    if game.iswin():
                        break

            # #######################################################################################################################

            else:

                old_position = game.environment.copy()
                move = policy[0].policy(game.environment)

                possible_moves = np.setdiff1d(possible_moves, move)

                game.player('X', move)

                if str(old_position) in policy[2].value_function:
                    print("Eval: " + str(policy[2].value_function[str(old_position)]))
                else:
                    print("Eval: -")

                game.draw()

                for i in range(4):
                    count += 1

                    ################

                    pin2 = True
                    while pin2:
                        n = int(input("Player2 to move. "))
                        if n in possible_moves:
                            pin2 = False

                    possible_moves = np.setdiff1d(possible_moves, n)

                    ################

                    game.player('O', n)
                    game.draw()

                    ################

                    if game.iswin():
                        break
                    count += 1

                    ################

                    old_position = game.environment.copy()
                    move = policy[0].policy(game.environment)

                    possible_moves = np.setdiff1d(possible_moves, move)

                    game.player('X', move)

                    if str(old_position) in policy[2].value_function:
                        print("Eval: " + str(policy[2].value_function[str(old_position)]))
                    else:
                        print("Eval: -")

                    game.draw()

                    ################

                    if game.iswin():
                        break

            # #######################################################################################################################

            if game.iswin():
                if count % 2 == 0:
                    print("Player1 wins !!!")

                else:
                    print("Player2 wins !!!")

            else:
                print("The game is a draw.")

            # #######################################################################################################################

            pin3 = input("Would you like to play against the bot again? (y/n) ") == 'y'

            # #######################################################################################################################

    if game.iswin():
        if count % 2 == 0:
            print("Player1 wins !!!")

        else:
            print("Player2 wins !!!")

    else:
        print("The game is a draw.")

    pin1 = input("Would you like to play again? (y/n) ") == 'y'
