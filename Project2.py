# File: Project2.py
# Student: Jawad Kazi
# UT EID: JAK4774
# Course Name: CS303E
#
# Date: 11/6/22
# Description of Program: This program allows an individual to play tic tac toe against a machine.

import random

# Some global constants:

HUMAN = 0
MACHINE = 1

YOU_WON = "Congratulations! You won!\n"
YOU_TIED = "Looks like a tie.  Better luck next time!"
YOU_LOST = "Sorry!  You lost!"
WELCOME = "Welcome to our Tic-Tac-Toe game!\n Please begin playing."


def initialBoard():
    return [[" ", " ", " "], \
            [" ", " ", " "], \
            [" ", " ", " "]]


class TicTacToe:
    def __init__(self):
        self.__board = initialBoard()
        self.current_player = random.randint(HUMAN, MACHINE)
        self.current_player = self.getPlayer()
    # Initialize the game with the board and current player

    def __str__(self):
        board = "|".join(self.__board[0])
        for i in range(2):
            board += "\n-----\n"
            board += "|".join(self.__board[i+1])
        return board
    # Return a string representation of the board.

    def getPlayer(self):
        return self.current_player

    # Return the current player.

    def isWin(self):
        if self.current_player == HUMAN:
            win = ['X'] * 3
        else:
            win = ['O'] * 3
        for row in range(3):
            col_combination = []
            for col in range(3):
                col_combination.append(self.__board[col][row])
            # if the column or row is equal to current player in all 3 spots its a win
            # print(col_combination)
            if col_combination == win or self.__board[row] == win:
                return True
        # diagonals
        # print([self.__board[0][0], self.__board[1][1], self.__board[2][2]])
        if [self.__board[0][0], self.__board[1][1], self.__board[2][2]] == win or [self.__board[0][2], self.__board[1][1], self.__board[2][0]] == win:
            return True
        return False
    # See if the board represents a win for the current
    # player. A win is three of the current player's tokens
    # in a single row, column, or either diagonal.

    def swapPlayers(self):
        if self.current_player == HUMAN:
            self.current_player = MACHINE
        else:
            self.current_player = HUMAN
    # Change the current player from HUMAN to MACHINE or
    # vice versa.

    def humanMove(self):
        while True:
            move = input("Your turn:\n  Specify a move r, c:")

            # CHECKING TO SEE IF INPUT IS X,X where X is the string of an integer
            illegal_move = False
            for text in move.split(","):
                if not text.isnumeric():
                    illegal_move = True
            if illegal_move:
                print("Response should be r, c. Try again!")
                continue
            index = [int(x) for x in move.split(",")]
            if str(index[0]) == move:
                print("Response should be r, c. Try again!")
                continue

            # CHECKING TO SEE IF MOVE IS A NUMBER BETWEEN 0 AND 2
            r, c = index[0], index[1]
            if self.__board[r][c] == " " and -1 < r < 3 and -1 < c < 3:
                self.__board[r][c] = "X"
                return
            else:
                print("Illegal move specified.  Try again!")
                continue

    # Ask the HUMAN to specify a move.  Check that it's
    # valid (syntactically, in range, and the space is
    # not occupied).  Update the board appropriately.

    def machineMove(self):
        # This is the MACHINE's move.  It picks squares randomly
        # until it finds an empty one. Update the board appropriately.
        # Note: this is a really dumb way to play tic-tac-toe.
        print("Machine's turn:")
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if self.__board[r][c] == " ":
                print("  Machine chooses: ", r, ", ", c, sep="")
                self.__board[r][c] = "O"
                return


def driver():
    """ This plays tic-tac-toe in a pretty simple-minded
    fashion.  The human player goes first with token "X" and
    alternates with the machine using token "O".  We print
    the board before the first move and after each move. """

    # Print the welcome message
    print(WELCOME)

    # Initialize the board and current player
    ttt = TicTacToe()
    print(ttt)

    # There are up to 9 moves in tic-tac-toe.
    for move in range(9):
        # The current player may be HUMAN
        # or MACHINE
        if ttt.getPlayer() == HUMAN:
            # If HUMAN, take a move, print the board,
            # and see if it's a win.
            ttt.humanMove()
            print(ttt)
            if ttt.isWin():
                print(YOU_WON)
                return

        else:
            # Else MACHINE takes a move.  Print the
            # board and see if the machine won.
            ttt.machineMove()
            print(ttt)
            if ttt.isWin():
                print(YOU_LOST)
                return

        # Swap players.
        ttt.swapPlayers()

    # After nine moves with no winner, it's a tie.
    print(YOU_TIED)


driver()
