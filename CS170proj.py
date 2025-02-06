from copy import deepcopy
import heapq
# first we declare the base cases provided in the project layout to get a quick test or input
depth0puzzle = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]

depth2puzzle = [[1, 2, 3],
                [4, 5, 6],
                [0, 7, 8]]

depth4puzzle = [[1, 2, 3],
                [5, 0, 6],
                [4, 7, 8]]

depth8puzzle = [[1, 3, 6],
                [5, 0, 2],
                [4, 7, 8]]

depth12puzzle = [[1, 3, 6],
                [5, 0, 7],
                [4, 8, 2]]

depth16puzzle = [[1, 6, 7],
                [5, 0, 3],
                [4, 8, 2]]

depth20puzzle = [[7, 1, 2],
                [4, 8, 5],
                [6, 3, 0]]

depth24puzzle = [[0, 7, 2],
                 [4, 6, 1],
                 [3, 5, 8]]
#########################################
def main():

    puzzleStarter = 0

    while (puzzleStarter not in (1,2)):
    
        puzzleStarter = input("Choose '1' to receive a list of default tables to solve, choose"
                          "'2' in order to curate your own: ")
        
        puzzleStarter = int(puzzleStarter)
    
        if (puzzleStarter == 1):
            print('You chose option 1.')
            displayPuzzles()
            break

        if (puzzleStarter == 2):
            print('You chose option 2.')
            # used chunk of code from example in order to ensure getting a table
            print("Enter your puzzle, using a zero to represent the blank. " +
                    "Please only enter valid 8 puzzles. Enter the puzzle demilimiting " +
                    "the numbers with a space. RET only when finished." + '\n')
            
            puzzle_row_one = input("Enter the first row: ")
            puzzle_row_two = input("Enter the second row: ")
            puzzle_row_three = input("Enter the third row: ") 

            puzzle_row_one = puzzle_row_one.split()
            puzzle_row_two = puzzle_row_two.split()
            puzzle_row_three = puzzle_row_three.split()

            for i in range(0, 3):
                puzzle_row_one[i] = int(puzzle_row_one[i])
                puzzle_row_two[i] = int(puzzle_row_two[i])
                puzzle_row_three[i] = int(puzzle_row_three[i])

            customPuzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]

            puzzlePrinter(customPuzzle)

            heuristicOperator(customPuzzle)

        else:
            print('Not a valid input. Try again.')

    print(str(puzzleStarter))
#######################################
def displayPuzzles():

    print('What depth puzzle would you like solved?')
    print('The options are 0, 2, 4, 8, 12, 16, 20, and 24.')

    chooseDepth = input('Enter the desired puzzle solution depth: ')

    chooseDepth = int(chooseDepth)

    if (chooseDepth == 0):

        puzzlePrinter(depth0puzzle)
        heuristicOperator(depth0puzzle)

    elif (chooseDepth == 2):

        puzzlePrinter(depth2puzzle)
        heuristicOperator(depth2puzzle)

    elif (chooseDepth == 4):

        puzzlePrinter(depth4puzzle)
        heuristicOperator(depth4puzzle)

    elif (chooseDepth == 8):

        puzzlePrinter(depth8puzzle)
        heuristicOperator(depth8puzzle)

    elif (chooseDepth == 12):

        puzzlePrinter(depth12puzzle)
        heuristicOperator(depth12puzzle)

    elif (chooseDepth == 16):

        puzzlePrinter(depth16puzzle)
        heuristicOperator(depth16puzzle)

    elif (chooseDepth == 20):

        puzzlePrinter(depth20puzzle)
        heuristicOperator(depth20puzzle)


    elif (chooseDepth == 24):

        puzzlePrinter(depth24puzzle)
        heuristicOperator(depth24puzzle)

##########################################
def puzzlePrinter(puzzlePassed):

    for i in range(0,3):

        print(puzzlePassed[i])

 #########################################   
def heuristicOperator(puzzleFromPrinter):

        print('How would you like to solve this puzzle?')

        sendToHeuristic = input("Enter '1' for Uniform Search, '2' for Misplaced Tile, '3'"
                                "for Manhattan Distance: ")
        
        sendToHeuristic = int(sendToHeuristic)

        if (sendToHeuristic == 1):
            
            uniformCostSearch(puzzleFromPrinter)

        elif (sendToHeuristic == 2):

            misplacedTile(puzzleFromPrinter)

        elif (sendToHeuristic == 3):

            manhattanDistance(puzzleFromPrinter)
    
##########################################
def uniformCostSearch(puzzleFromOperator):
    
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    start = [(0, puzzleFromOperator)]  # no cost because we just started, start at unsolved puzzle

    visited = set() # get ready to note where we have already explored 

    nodesExpanded = 0 # get ready to track how many 

    maxQueueSize = 1 # default

    while start:
        # https://docs.python.org/3/library/heapq.html
        g, currentState = heapq.heappop(start)  # get the lowest-cost node

        nodesExpanded += 1

        # Print the state
        puzzlePrinter(currentState)

        print(f"g(n): {g}, h(n): 0") # adding f to deal with weird printing behavior

        if currentState == goalState: # we are in the goal state here

            print(f"Solution found at depth {g}")
            print(f"Nodes expanded: {nodesExpanded}")
            print(f"Max queue size: {maxQueueSize}")

            return
        # https://www.geeksforgeeks.org/python-map-function/
        # https://docs.python.org/3/tutorial/datastructures.html
        # https://www.w3schools.com/python/python_tuples.asp
        # hardest part of implementing this function
        visited.add(tuple(map(tuple, currentState)))

        for neighbor in getNeighbors(currentState):  # send to helper function

            if tuple(map(tuple, neighbor)) not in visited: # consult our visited tracker to make sure we havent been here
                # https://docs.python.org/3/library/heapq.html
                heapq.heappush(start, (g + 1, neighbor))
                # tracks the max queue size
                maxQueueSize = max(maxQueueSize, len(start))

#########################################
def misplacedTile(puzzleFromOperator):
    print(f'in misplaced tile')
##########################################
def manhattanDistance(puzzleFromOperator):
    print(f'in manhattan distance')
###########################################
# gives us a list of valid states to go from the current ones
def getNeighbors(state):
    
    neighbors = [] # will hold states we can go to
    x, y = None, None

    
    for i in range(3): # loop through table to find empty tile
        
        for j in range(3):

            if state[i][j] == 0:

                x, y = i, j
                break
    
    # up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves: 
        
        newX, newY = x + dx, y + dy # new coordinates of 0
        
        if 0 <= newX < 3 and 0 <= newY < 3: # make sure we are in tbale
            
            newState = deepcopy(state) # make a copy 

            newState[x][y], newState[newX][newY] = newState[newX][newY], newState[x][y] # move 0 to new state

            neighbors.append(newState) # updates our altered state
    
    return neighbors
######################################
main()