from utils.print_sudoku_board import print_sudoku_board
import utils.load_sudoku as load_sudoku
from solver.lp_solver import lpSolve


sudoku_puzzle, sudoku_solution = load_sudoku.from_csv("sudoku.csv", 1)
# print_sudoku_board(sudoku_puzzle[0])
print(sudoku_puzzle[0])
print("\n")
print("Solving the puzzle...\n")
result = lpSolve(sudoku_puzzle[0])
print_sudoku_board(result)
print("\n")
print("The correct solution:")
print_sudoku_board(sudoku_solution[0])
