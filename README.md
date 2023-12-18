# Sudoku Solver

This Python project is a simple Sudoku solver using the backtracking algorithm.

## Introduction

Sudoku is a popular number puzzle where the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contains all of the digits from 1 to 9.

This project provides a Python implementation of a Sudoku solver that can take an incomplete Sudoku puzzle as input and attempt to find a solution by recursively filling in the empty cells based on the rules of Sudoku.

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/Alliyan732/sudoku-with-backtracking
```

2.Navigate to the project directory:
```bash
cd sudoku-with-backtracking
```

3. Run the Python script:
```bash
python SudokuWithBacktracking.py
```

## Project Details

- **Author:** AALLIYAN WAHEED ALVI
- **Date:** 22-JUNE, 2022

## Usage

### Input Format

To use the Sudoku solver, run the Python script and input the Sudoku puzzle as a series of rows. Enter "0" for empty cells. Follow the on-screen instructions to input the Sudoku grid.

### Options

1. **View Possible Solutions:** Enter "1" to view possible solutions for the provided Sudoku puzzle.
2. **Exit:** Enter "0" to exit the Sudoku solver.

## Example

```plaintext
Enter 0 in place of blank spaces
Note: Enter elements in rows without spaces and commas

Enter the elements of row 1: 530070000
Enter the elements of row 2: 600195000
Enter the elements of row 3: 098000060
Enter the elements of row 4: 800060003
Enter the elements of row 5: 400803001
Enter the elements of row 6: 700020006
Enter the elements of row 7: 060000280
Enter the elements of row 8: 000419005
Enter the elements of row 9: 000080079

### Grid ###
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
- - - - - - - - - - - 
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
- - - - - - - - - - - 
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 0 1 9 | 0 0 5
0 0 0 | 0 0 0 | 0 8 0

Please, Choose from the following Options:
1  >> Press 1 to view possible solutions
2  >> Press 0 to Exit the game

Enter your choice: 1

### Possible Solution ###
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
- - - - - - - - - - - 
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
- - - - - - - - - - - 
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
_______________________

Please, Choose from the following Options:
1  >> Press 1 to view possible solutions
2  >> Press 0 to Exit the game

Enter your choice: 0
```

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Aalliyan Alvi

## Support
If you encounter any issues or have any questions or suggestions, please feel free to open an issue. We appreciate your feedback and contributions to the project.

Email: alliyan732@gmail.com

LinkedIn: https://www.linkedin.com/in/alliyan-alvi/

Happy Coding!

