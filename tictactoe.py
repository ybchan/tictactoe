"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0

    # count the number of X or O on board
    for row in board:
        count_X += row.count(X)
        count_O += row.count(O)

    # O turn if number of X more than number of O
    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = []

    # find all empty spot on board and add to action_list
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_list.append((i, j))
    
    return set(action_list)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    # check action is legitimate or not
    if board[i][j] != EMPTY:
        raise IllegitimateMove
    else:
        new_board = copy.deepcopy(board)
        new_board[i][j] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for r in board:
        if r[0] == r[1] == r[2] is not None:
            return r[0]

    # check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] is not None:
            return board[0][j]

    # check diagonal
    if board[0][0] == board[1][1] == board[2][2] is not None or board[0][2] == board[1][1] == board[2][0] is not None:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # terminal board if there is a winner or no move can be made
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(s):
        if terminal(s):
            return utility(s)

        v = float("-inf") 
        for action in actions(s):
            v = max(v, min_value(result(s, action)))
        return v

    def min_value(s):
        if terminal(s):
            return utility(s)

        v = float("inf")
        for action in actions(s):
            v = min(v, max_value(result(s, action)))
        return v

    # check if board is done
    if terminal(board):
        return None

    # create list of possible actions and corresponding values
    action_list = list(actions(board))
    random.shuffle(action_list)
    value_list = []

    # find action with min or max value and return action from action_list
    if player(board) == X:
        for action in action_list:
            value_list.append(min_value(result(board, action)))
        return action_list[value_list.index(max(value_list))]
    else:
        for action in action_list:
            value_list.append(max_value(result(board, action)))
        return action_list[value_list.index(min(value_list))]


