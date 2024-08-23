from pprint import pprint


def find_next_empty(puzzle):

    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == -1:
                return r, c

    return None, None  
def is_valid(puzzle, guess, row, col):

    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):

    row, col = find_next_empty(puzzle)

    if row is None:  
        return True 
    
    for guess in range(1, 10): 
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = -1

    return False

def print_sudoku(puzzle):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)  # Print a horizontal line after every 3 rows
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")  # Print a vertical line after every 3 columns

            if c == 8:
                print(puzzle[r][c])  # Print the last number in the row and move to the next line
            else:
                print(puzzle[r][c], end=" ")

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    if solve_sudoku(example_board):
        print("Sudoku solved successfully!")
        print_sudoku(example_board)
    else:
        print("Failed to solve Sudoku.")
