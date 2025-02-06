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
            # add call to custom puzzle builder

        else:
            print('Not a valid input. Try again.')

    print(str(puzzleStarter))

def displayPuzzles():

    print('What depth puzzle would you like solved?')
    print('The options are 0, 2, 4, 8, 12, 16, 20, and 24.')

    chooseDepth = input('Enter the desired puzzle solution depth: ')

    chooseDepth = int(chooseDepth)

    if (chooseDepth == 0):

        for i in range(0, 3):
            print(depth0puzzle[i])

    elif (chooseDepth == 2):

        for i in range(0, 3):
            print(depth2puzzle[i])

    
    

main()