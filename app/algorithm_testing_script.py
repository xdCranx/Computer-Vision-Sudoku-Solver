from utils.print_sudoku_board import print_sudoku_board
import utils.load_sudoku as load_sudoku
from solver import cp_solver
import cv2

vhard_puzzle = [
    [3, 0, 0, 6, 0, 0, 0, 8, 4],
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 7, 5, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 5, 0, 6, 7],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [6, 0, 1, 0, 0, 0, 0, 0, 2],
    [5, 0, 0, 0, 0, 4, 7, 0, 0],
    [0, 0, 0, 9, 0, 0, 2, 4, 0],
    [0, 0, 6, 0, 0, 7, 0, 0, 0],
]


sudoku_puzzle, sudoku_solution = load_sudoku.from_csv("sudoku.csv", 1)
# print(sudoku_puzzle[0])
# print("\n")
print("Solving the puzzle...\n")
result = cp_solver.cpSolve(vhard_puzzle)
print_sudoku_board(result)
# print("\n")
# print("The correct solution:")
# print_sudoku_board(sudoku_solution[0])


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
