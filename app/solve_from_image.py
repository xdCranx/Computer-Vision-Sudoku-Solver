import sys
import cv2
import image
import image.utils
import solver
import utils
import utils.print_sudoku_board


def solveFromImage(image_path):
    puzzle_image = utils.loadPhoto(image_path)
    print(puzzle_image.shape)

    grey = image.preprocess(puzzle_image)
    cv2.imshow("grey", grey)
    corners = image.findSudokuBox(grey)

    if corners is not None:
        sudoku_box = image.extractSudokuBox(puzzle_image, corners)
        # cv2.imshow("sudoku_box", sudoku_box)
        sudoku = image.preprocess(sudoku_box)
        # cv2.imshow("sudoku", sudoku)

        grid_lines = image.getGridLines(sudoku)
        # cv2.imshow("grid_lines", grid_lines)

        mask = image.createGridMask(grid_lines)
        # cv2.imshow("mask", mask)
        
        masked_grid = image.applyGridMask(sudoku, mask)
        cv2.imshow("masked_grid", masked_grid)
        cells = image.splitIntoCells(masked_grid)
        clean_cells = image.cleanCells(cells)
        clean_sudoku = image.utils.sudokuFromCells(clean_cells)
        cv2.imshow("clean_sudoku", clean_sudoku)

        recognized_digits = image.recognizeDigits(clean_cells)
        puzzle = image.utils.convertTo2D(recognized_digits)
        print("Recognized Digits:")
        utils.printSudokuBoard(puzzle)

        # solved = solver.cpSolve(puzzle)
        # if solved:
        #     utils.printSudokuBoard(solved)
        # else:
        #     print("No solution found")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: python solve_from_image.py <image_path>")
    path = sys.argv[1]
    solveFromImage(path)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
