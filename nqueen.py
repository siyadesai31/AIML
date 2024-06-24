# # perform best first search in state space to solve the n queens problem

# import random
# from copy import copy


# n = int(input("Enter the value of n: "))

# # store the state as a list of the positions of the queens, per row
# state = [random.randint(0, n-1) for i in range(n)]

# # store all the visited states:
# visited = []

# # flag if there is no solution
# noGoalFlag = True


# def heuristic(state):

#     # store the (x, y) coordinates of the queens
#     locations = list(enumerate(state))
#     heuristicValue = 0

#     for key_i, loc in enumerate(locations):
#         for loc2 in locations[key_i + 1:]:
#             # loc loc2 are two tuples
#             # (i, j)
#             #   (0,0)
#             #   Q _ _
#             #   _ _ _
#             #   _ _ Q (2,2)

#             # if the two queens are in the same column
#             if loc[1] == loc2[1]:
#                 heuristicValue += 1

#             # if the difference between the x and the y coordinates
#             # of both queens is the same, ie |(x2 - x1)| == |(y2 - y1)|
#             # it must be on a diagonal (hopefully)
#             if abs(loc[0] - loc2[0]) == abs(loc[1] - loc2[1]):
#                 heuristicValue += 1

#     return heuristicValue


# # generate all possible children of the state given
# def genChildren(state):
#     """
#     generate all possible children of the state given
#     ### Args:
#     state: a list of positions of each queen, per row
#     """
#     children = []

#     # loop to generate different children by changing each row at a time
#     for i in range(n):

#         child = copy(state)

#         # place queens in the i'th row in all other positions other than the current one
#         for j in range(n):
#             if j != state[i]:
#                 child[i] = j
#                 if child not in visited:
#                     children.append(copy(child))
#                     # add it to visited
#                     visited.append(copy(child))

#     return children


# def printBoard(state):

#     for row in state:
#         for column in range(n):
#             if column == row:
#                 print("Q", sep=" ", end=" ")
#             else:
#                 print("x", sep=" ", end=" ")
#         print()


# # ========================================================================================================


# def bestFirstNQueens(start):

#     # store the children of the current state
#     children = []
#     # a queue to store tuples of (heuristic, state) for all states in open list
#     queue = []

#     queue.append((heuristic(start), start))

#     while len(queue) != 0:

#         # get the best child from the queue
#         currentHeuristic, currentState = queue.pop(0)

#         # check if a goal state has been reached
#         if currentHeuristic == 0:
#             print("goal reached")
#             printBoard(currentState)
#             global noGoalFlag
#             noGoalFlag = False
#             return
#         # add it to visited
#         visited.append(copy(currentState))

#         # generate all children of the current state, that have not already been visited:
#         children = genChildren(currentState)

#         # compute the heuristic of each child, and add it to the queue:
#         for child in children:
#             queue.append((heuristic(child), copy(child)))

#         # sort the queue based on heuristic values:
#         queue.sort()


# bestFirstNQueens(state)

# if noGoalFlag:
#     print("No solution :(")



#function to print board
def display(state):                                 
    for i in range(n):
        for j in range(n):
            if state[i]==j:
                print(" Q ",end="")
            else: 
                print(" _ ",end="")
        print("")
    print("\n")

#function to calculate heuristic value of a state
def heuristics(state):
    h=0
    for i in range(n-1):
        for j in range(i+1,n):
            if abs((state[i]-state[j])/(i-j))==1:       #if two queens are in same diagonal, increase heuristic value
                h+=1
    return h

def nqueens():
    start=[]                                            #start state of board
    for i in range(n):                                  #every queen placed on diagonal
        start.append(i)
    print("\nInitial state is : ")
    display(start)                                      #displaying start state

    queue=[(start,heuristics(start))]                   #similar to open list but with heuristic value tupled
    open=[start]                                        #open list with only states
    closed=[]                                           #closed list
    flag=0                                              #flag to check if solution is found
    
    while len(queue)>0:
        a=queue.pop(0)
        open.remove(a[0])
        closed.append(a[0])

        if a[1]==0:                                      #a[1]=heuristic; if heuristic is 0 then no queen attacks; solution found
            print("\nSolution is : ",a[0],"\n")
            display(a[0])
            flag=1
            break
        else:                                           #finding new states generated from current state
            newstates=[]                                  
            current=a[0]                                #current state     
            for i in range(1,n):                        #for every queen from column 1-n
                tstate=[]                               #temporary state
                for x in current:                       #copy current state in temporary
                    tstate.append(x)                        
                temp=current[i]                         #position of queen in column i
                tstate[0],tstate[temp]=tstate[temp],tstate[0]       #swap with queen in column 0
                newstates.append(tstate)                 #add to new state
        newstates=[x for x in newstates if x not in open and x not in closed]       #remove from newstates if already present in open and closed list

        open.extend(newstates)                            #add newstates to open
        newstates=[(x,heuristics(x)) for x in newstates]    #form tuples with heuristic
        queue=newstates+queue                            #add new states to queue
        queue = sorted(queue, key=lambda x: x[1])        #sort according to heuristic

    if flag==0:                                          #if flag is 0 no solution
        print("No Solution Possible!!!")

n=int(input("Enter the value of n : "))                                                 # input n
nqueens()
