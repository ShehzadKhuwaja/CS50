"""
Tic Tac Toe Player
"""

import math

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
    if terminal(board): return X # if board in its terminal state we can arbitrary return any player X or O. 

    """
    assuming player X plays first, if the count is even then it is X's turn otherwise player y will play.  
    """

    count = 0 # sum of X's and O's on the board
    for i in range(len(board)): 
        for j in range(len(board)):
            if board[i][j] is not EMPTY: count += 1
    
    if count % 2 == 0: return X
    else: return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board): return set() # empty set is returned if board is in terminal state

    actions = set() # set of actions
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY: actions.add((i, j)) # i'th row and j'th column is empty add the (i, j) block to actions 

    return actions 
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x, y = action
    if board[x][y] is not EMPTY: raise Exception("invalid move!")

    # creating a deep copy of the board
    new_board = [[EMPTY] * len(board) for _ in range(len(board))] # creating board temporary with intial state
    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i][j] = board[i][j]
    
    # find whose turn it is X or O and then mark postion (x, y) in the new board with it 
    new_board[x][y] = player(board)
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # assuming board is in valid state
    left_digonal_x, left_digonal_o = 0, 0
    right_digonal_x, right_digonal_o = 0, 0
    for i in range(len(board)):
        horizontal_count_x = 0
        horizontal_count_o = 0
        vertical_count_x = 0
        vertical_count_o = 0
        for j in range(len(board)):
            # check for a row win
            if board[i][j] == X:
                horizontal_count_x += 1
            elif board[i][j] == O:
                horizontal_count_o += 1
            
            # check for column win
            if board[j][i] == X:
                vertical_count_x += 1
            elif board[j][i] == O:
                vertical_count_o += 1
        if horizontal_count_x == 3 or vertical_count_x == 3: return X
        elif horizontal_count_o == 3 or vertical_count_o == 3: return O
    
        # check for left digonal win
        if board[i][i] == X:
            left_digonal_x += 1
        elif board[i][i]: left_digonal_o += 1

        # check for right digonal win
        if board[i][len(board) - i - 1] == X:
            right_digonal_x += 1
        elif board[i][len(board) - i - 1] == O:
            right_digonal_o += 1

    if left_digonal_x == 3 or right_digonal_x == 3:
        return X
    elif left_digonal_x == 3 or right_digonal_o == 3:
        return O
    else:
        return None
        
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None: return True

    # game will end if no spot is left empty
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:
                return False # empty spot found, so not a terminal state       
    return True # no empty spot found on the entire board ,thus terminal state
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # assuming that the board is in terminal state
    won = winner(board)
    if won == X: return 1
    elif won == O: return -1
    else: return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    mydict = {}
    if player(board) == X:
        for action in actions(board):
            mydict[action] = min_value(result(board, action))
        return max(mydict, key=mydict.get)
    else:
        for action in actions(board):
            mydict[action] = max_value(result(board, action))
        return min(mydict, key=mydict.get)


def max_value(board):
    v = -math.inf
    if terminal(board): return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
       

def min_value(board):
    v = math.inf
    if terminal(board): return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
  
    



        
