import sys
import app.utils as utils
from app.detect_and_solve import detectAndSolve


def solveFromImage(image_path, solverMode=1, debug=False):
    """Uses the detectAndSolve function to solve a Sudoku puzzle from an image.

    Args:
        image_path (str): The path to the image containing the Sudoku puzzle.
        solverMode (int, optional): The mode to use for solving the puzzle.
            (Defaults to 1):
            0 - Use the default solver.
            1 - Use the constraint programming solver.
            2 - Use the linear programming solver.
        debug (bool, optional): Whether to display every step of the process.
    """
    puzzle_image = utils.loadPhoto(image_path)
    solved = detectAndSolve(puzzle_image, solverMode, debug)

    utils.printSudokuBoard(solved)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        raise ValueError(
            "Usage: python solve_from_image.py <image_path> [<solver_mode>] [<debug>]"
        )

    path = sys.argv[1]

    if not path:
        raise ValueError("Image path must be provided")

    solverMode = 1
    debug = False

    if len(sys.argv) > 2:
        solverMode = int(sys.argv[2])
        if solverMode not in [0, 1, 2]:
            raise ValueError("Invalid solver mode. Choose from 0, 1, or 2.")

    if len(sys.argv) > 3:
        debug = sys.argv[3].lower() in ["true", "1", "yes"]

    solveFromImage(path, solverMode, debug)
