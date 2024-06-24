# perform best first search in state space to solve the n queens problem

import random
from copy import copy


n = int(input("Enter the value of n: "))

# store the state as a list of the positions of the queens, per row
state = [random.randint(0, n-1) for i in range(n)]

# store all the visited states:
visited = []

# flag if there is no solution
noGoalFlag = True


def heuristic(state):

    # store the (x, y) coordinates of the queens
    locations = list(enumerate(state))
    heuristicValue = 0

    for key_i, loc in enumerate(locations):
        for loc2 in locations[key_i + 1:]:
            # loc loc2 are two tuples
            # (i, j)
            #   (0,0)
            #   Q _ _
            #   _ _ _
            #   _ _ Q (2,2)

            # if the two queens are in the same column
            if loc[1] == loc2[1]:
                heuristicValue += 1

            # if the difference between the x and the y coordinates
            # of both queens is the same, ie |(x2 - x1)| == |(y2 - y1)|
            # it must be on a diagonal (hopefully)
            if abs(loc[0] - loc2[0]) == abs(loc[1] - loc2[1]):
                heuristicValue += 1

    return heuristicValue


# generate all possible children of the state given
def genChildren(state):
    """
    generate all possible children of the state given
    ### Args:
    state: a list of positions of each queen, per row
    """
    children = []

    # loop to generate different children by changing each row at a time
    for i in range(n):

        child = copy(state)

        # place queens in the i'th row in all other positions other than the current one
        for j in range(n):
            if j != state[i]:
                child[i] = j
                if child not in visited:
                    children.append(copy(child))
                    # add it to visited
                    visited.append(copy(child))

    return children


def printBoard(state):

    for row in state:
        for column in range(n):
            if column == row:
                print("Q", sep=" ", end=" ")
            else:
                print("x", sep=" ", end=" ")
        print()


# ========================================================================================================


def bestFirstNQueens(start):

    # store the children of the current state
    children = []
    # a queue to store tuples of (heuristic, state) for all states in open list
    queue = []

    queue.append((heuristic(start), start))

    while len(queue) != 0:

        # get the best child from the queue
        currentHeuristic, currentState = queue.pop(0)

        # check if a goal state has been reached
        if currentHeuristic == 0:
            print("goal reached")
            printBoard(currentState)
            global noGoalFlag
            noGoalFlag = False
            return
        # add it to visited
        visited.append(copy(currentState))

        # generate all children of the current state, that have not already been visited:
        children = genChildren(currentState)

        # compute the heuristic of each child, and add it to the queue:
        for child in children:
            queue.append((heuristic(child), copy(child)))

        # sort the queue based on heuristic values:
        queue.sort()


bestFirstNQueens(state)

if noGoalFlag:
    print("No solution :(")



# import random


# def heuristic(board):
#     conflicts = 0
#     for i in range(len(board)):
#         for j in range(i + 1, len(board)):
#             if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
#                 conflicts += 1
#     return conflicts


# def print_board(board):
#     for row in range(1, 9):
#         row_str = ""
#         for col in board:
#             if col == row:
#                 row_str += "Q "
#             else:
#                 row_str += "_ "
#         print(row_str)


# def solve_queens(initial_board):
#     print("Initial Board:", initial_board)
#     current_board = initial_board.copy()
#     current_heuristic = heuristic(current_board)
#     same_state_count = 0
#     max_same_state_count = 3
#     print("Initial Heuristic:", current_heuristic)

#     while current_heuristic > 0:
#         # Generate a random move (swap two rows)
#         row1, row2 = random.sample(range(1, 9), 2)
#         current_board[row1 - 1], current_board[row2 - 1] = (
#             current_board[row2 - 1],
#             current_board[row1 - 1],
#         )

#         new_heuristic = heuristic(current_board)
#         if new_heuristic < current_heuristic:
#             current_heuristic = new_heuristic
#             same_state_count = 0  # Reset same state counter
#             print("Current Board:", current_board)
#             print("Current Heuristic:", current_heuristic)
#             print_board(current_board)
#         else:
#             # Undo the move if it doesn't lead to improvement
#             current_board[row1 - 1], current_board[row2 - 1] = (
#                 current_board[row2 - 1],
#                 current_board[row1 - 1],
#             )
#             same_state_count += 1

#         if same_state_count >= max_same_state_count:
#             # Perform a random move to a neighboring state
#             row1, row2 = random.sample(range(1, 9), 2)
#             current_board[row1 - 1], current_board[row2 - 1] = (
#                 current_board[row2 - 1],
#                 current_board[row1 - 1],
#             )
#             same_state_count = 0  # Reset same state counter

#     print("Solution Found!")
#     print("Final Board:", current_board)
#     print("Final Heuristic:", current_heuristic)
#     print_board(current_board)


# initial_board = []
# t = 8
# print("Initial Board")
# while t:
#     inp = int(input())  # column is input and row is the index
#     initial_board.append(inp)
#     t = t - 1

# print("Initial Board:")
# print_board(initial_board)
# solve_queens(initial_board)