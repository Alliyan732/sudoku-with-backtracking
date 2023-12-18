"""                            
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@ ______________________________________________________________________ @@
    @@|                                                                      |@@
    @@|                 *** Artificial intelligence (AI) ***                 |@@
    @@|                           (SEMISTER PROJECT)                         |@@
    @@|                                                                      |@@
    @@|                                                                      |@@
    @@|                   SUBMITTED BY: AALLIYAN WAHEED ALVI                 |@@
    @@|                   SUBMITTED TO: Ma'am. Shahela Saif                  |@@
    @@|                                                                      |@@
    @@|                                                                      |@@
    @@|      PROJECT Part-1:                                                 |@@
    @@|                           ** Sudoku Solver **                        |@@
    @@|                                                                      |@@
    @@|                                                                      |@@
    @@|      DATE: 22-JUNE, 2022.                                            |@@
    @@|                                                                      |@@
    @@|                                     ~Code By Alliyan Waheed Alvi     |@@
    @@|______________________________________________________________________|@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

# Sudoko Solver
# NumPy is a Python library used for working with arrays
# used in arrays, multidimentional arrays, matrix
# here we are using it for printing Sudoku Grid
import numpy as np # short name 'np' can be used in code
import sys


print("\n\n\t\t\t\t\t\t\t       *###* Sudoku Solver *###*");	
print("\n\t\t\t\t\t\t\t            *** DASHBOARD ***\n");	
        
print("\n\t\t\t\t\t\tPlease,  Choose from the following Options: \n")
print("\t\t\t\t\t\t _________________________________________________________________")
print("\t\t\t\t\t\t|                                           	                  |\n")
print("\t\t\t\t\t\t|             1  >> Press 1 to continue                           |\n")
print("\t\t\t\t\t\t|             0  >> Press 0 to Exit the game                      |\n")
print("\t\t\t\t\t\t|_________________________________________________________________|\n\n")
    

choice = int(input("Enter your choice: "))

if (choice == 1):

        # # Given Sudoko problem grid
        # # here zeros are representing empty spaces

        # sudoku_grid = [[5,   3,   0,   0,   7,   0,   0,   0,   0],
        #                [6,   0,   0,   1,   9,   5,   0,   0,   0],
        #                [0,   9,   8,   0,   0,   0,   0,   6,   0],
        #                [8,   0,   0,   0,   6,   0,   0,   0,   3],
        #                [4,   0,   0,   8,   0,   3,   0,   0,   1],
        #                [7,   0,   0,   0,   2,   0,   0,   0,   6],   
        #                [0,   6,   0,   0,   0,   0,   2,   8,   0],
        #                [0,   0,   0,   0,   1,   9,   0,   0,   5],
        #                [0,   0,   0,   0,   0,   0,   0,   0,   0]]


    
        # **************** Taking values from User ****************

        sudoku_grid = []
        print("\n\n\nEnter 0 in place of blank spaces")
        print("Note: Enter elements in rows without spaces and commas\n\n")
        for i in range(9): # 9 rows
            # format shows value of i+1 in {}
            row = list(input("Enter the elements of row {}: ".format(i+1))) 
            # python by defaults takes input as string, here we are converting
            # every item to int
            row = [int(i) for i in row]
            # append rows to the empty list created above
            sudoku_grid.append(row)
        
        # print("\n\n***** ###* Grid *### *****\n");	
        # print(np.matrix(sudoku_grid))

        # ********* # Checking for possibility for a number # *********
        def print_grid(grid):
            for i in range(len(grid)):
                if i % 3 == 0 and i != 0:
                    print("- - - - - - - - - - - - ")
            
                for j in range (len(grid[0])):
                    if j % 3 == 0 and j != 0:
                        print(" | ", end="")
                
                    if j == 8:
                        print(grid[i][j])
                    else:
                        print(str(grid[i][j]) + " ", end="")
        
        print("\n\n**** ###* Grid *### ****\n");	
        print_grid(sudoku_grid)

    
        # ********* # Checking for possibility for a number # *********

        def check_possibility(row, column, number):
            # making sudoku_grid global to use it anywhere
            global sudoku_grid
            # ******* check if the number is present in the given row *******
            for i in range(0,9):
                if sudoku_grid[row][i] == number:
                    return False

            # ******* check if the number is present in the given column *******
            for i in range(0,9):
                if sudoku_grid[i][column] == number:
                    return False
    
            # ******* check if the number is present in the given square *******

            # we can divide the squares in sections, e.g for r1, r2, r3
            # r//3 = 0, so we can say it as section 0
            # we can divide the squares in sections, e.g for r4, r5, r6
            # r//3 = 1, so we can say it as section 1
            # we can divide the squares in sections, e.g for r7, r8, r9
            # r//3 = 2, so we can say it as section 2

            # to get the starting point of each section,
            # use (column // 3) * 3 , (row // 3) * 3
            # starting point of sqaures will always be (0 or 3 or 6)

            x_startingPoint = (column // 3) * 3
            y_startingPoint = (row // 3) * 3
            # every square has 3 rows
            for i in range(0,3):
                # every square has 3 columns
                for j in range(0,3):
                    if sudoku_grid[y_startingPoint + i][x_startingPoint + j] == number:
                        return False

            return True


        # **************** function ****************

        def solve_sudoku():
            global sudoku_grid
            # looping throught the whole grid
            for row in range(0,9):
                for column in range(0,9):
                    # checking for 0, the empty field
                    if sudoku_grid[row][column] == 0:
                        for number in range(1,10):
                            if check_possibility(row, column, number):
                                # if possible, set number
                                sudoku_grid[row][column] = number
                                # recursive call (Backtracking)
                                solve_sudoku()
                                # if it stucks, or cannot move, then again set [row][col] to empty i.e 0
                                sudoku_grid[row][column] = 0

                        return

        
            print("\n\n### Possible Solution ###")
            print("_______________________\n")
            print_grid(sudoku_grid)
            print("_______________________\n\n")

            
            # print("_____________________\n\n")
            # print("\n ### Possible Solution ###")
            # print("_____________________\n")
    
            # # using numpy module for printing
            # print(np.matrix(sudoku_grid))

            # print("_____________________\n\n")


        print("\n\t\t\t\t\t\tPlease,  Choose from the following Options: \n")
        print("\t\t\t\t\t\t _________________________________________________________________")
        print("\t\t\t\t\t\t|                                           	                  |\n")
        print("\t\t\t\t\t\t|             1  >> Press 1 to view possible solutions            |\n")
        print("\t\t\t\t\t\t|             2  >> Press 0 to Exit the game                      |\n")
        print("\t\t\t\t\t\t|_________________________________________________________________|\n\n")

        option = int(input("Enter your choice: "))

        if (option == 1):
            solve_sudoku()                
            
        elif (option == 0):
            print("\n\n\t\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("\t\t\t\t\t@@ ______________________________________________________________________ @@")
            print("\t\t\t\t\t@@|                            		                                 |@@")
            print("\t\t\t\t\t@@|                               		                         |@@")
            print("\t\t\t\t\t@@|                               		                         |@@")
            print("\t\t\t\t\t@@|                                           	                         |@@")
            print("\t\t\t\t\t@@|                                                                      |@@")
            print("\t\t\t\t\t@@|                                                                      |@@")
            print("\t\t\t\t\t@@|                          THANKS FOR USING OUR                        |@@")
            print("\t\t\t\t\t@@|                                                                      |@@")
            print("\t\t\t\t\t@@|                            Sudoku Solver                             |@@")
            print("\t\t\t\t\t@@|                                                                      |@@")
            print("\t\t\t\t\t@@|                                                                      |@@")
            print("\t\t\t\t\t@@|                                                                      |@@")
            print("\t\t\t\t\t@@|                             closing...                               |@@")
            print("\t\t\t\t\t@@|                                                                      |@@")
            print("\t\t\t\t\t@@|                                     ~Code By Alliyan Waheed Alvi     |@@")
            print("\t\t\t\t\t@@|______________________________________________________________________|@@")
            print("\t\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n\n\t\t\t\t\t")
            
        else:
            print("Invalid entry!!!, Please Try again")
    

elif(choice == 0):
    
        print("\n\n\t\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("\t\t\t\t\t@@ ______________________________________________________________________ @@")
        print("\t\t\t\t\t@@|                            		                                 |@@")
        print("\t\t\t\t\t@@|                               		                         |@@")
        print("\t\t\t\t\t@@|                               		                         |@@")
        print("\t\t\t\t\t@@|                                           	                         |@@")
        print("\t\t\t\t\t@@|                                                                      |@@")
        print("\t\t\t\t\t@@|                                                                      |@@")
        print("\t\t\t\t\t@@|                          THANKS FOR USING OUR                        |@@")
        print("\t\t\t\t\t@@|                                                                      |@@")
        print("\t\t\t\t\t@@|                            Sudoku Solver                             |@@")
        print("\t\t\t\t\t@@|                                                                      |@@")
        print("\t\t\t\t\t@@|                                                                      |@@")
        print("\t\t\t\t\t@@|                                                                      |@@")
        print("\t\t\t\t\t@@|                             closing...                               |@@")
        print("\t\t\t\t\t@@|                                                                      |@@")
        print("\t\t\t\t\t@@|                                     ~Code By Alliyan Waheed Alvi     |@@")
        print("\t\t\t\t\t@@|______________________________________________________________________|@@")
        print("\t\t\t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n\n\t\t\t\t\t")
else:
        print('Invalid entry!!!, Try again')















    
            

