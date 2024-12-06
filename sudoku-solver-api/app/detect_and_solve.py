import cv2
import app.image as image
import app.utils as utils
from app.utils.print_sudoku_board import printSudokuBoard
import app.solver as solver


def detectAndSolve(img, solverMode=1, debug=False):
    """
    Detects and solves a Sudoku puzzle from an input image.

    Args:
        img (numpy.ndarray): The input image containing the Sudoku puzzle.
        solverMode (int, optional): The mode to use for solving the puzzle.
            (Defaults to 1):
            0 - Use the default solver.
            1 - Use the constraint programming solver.
            2 - Use the linear programming solver.
        debug (bool, optional): Whether to display every step of the process.

    Returns:
        numpy.ndarray: The solved Sudoku puzzle as a 2D array.

    Raises:
        ValueError: If the Sudoku box cannot be found in the image or if an invalid solver mode is provided.
    """
    grey = image.preprocess(img)
    corners = image.findSudokuBox(grey)
    if corners is not None:
        sudoku_box = image.extractSudokuBox(img, corners)
        sudoku = image.preprocess(sudoku_box)
        grid_lines = image.getGridLines(sudoku)
        mask = image.createGridMask(grid_lines)
        masked_grid = image.applyGridMask(sudoku, mask)
        cells = image.splitIntoCells(masked_grid)
        clean_cells = image.cleanCells(cells)
        recognized_digits = image.recognizeDigits(clean_cells)
        puzzle = image.utils.convertTo2D(recognized_digits)
        if solverMode == 0:
            solved = solver.solve(puzzle.copy())
        elif solverMode == 1:
            solved = solver.cpSolve(puzzle.copy())
        elif solverMode == 2:
            solved = solver.lpSolve(puzzle.copy())
        else:
            raise ValueError("Invalid solver mode")

        if debug:
            cv2.imshow("grey", grey)
            cv2.imshow("sudoku_box", sudoku_box)
            cv2.imshow("sudoku", sudoku)
            cv2.imshow("grid_lines", grid_lines)
            cv2.imshow("mask", mask)
            cv2.imshow("masked_grid", masked_grid)
            cv2.imshow("clean_sudoku", image.utils.sudokuFromCells(clean_cells))
            print("Recognized Digits:")
            printSudokuBoard(puzzle)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if solved is not None:
            return solved
        else:
            raise ValueError("No solution found")
    else:
        raise ValueError("Could not find sudoku box in image")
