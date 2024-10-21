from app.solver import solver
import app.utils.load_sudoku as load_sudoku
import pytest
import numpy as np

puzzles, solutions = load_sudoku.from_csv("sudoku.csv", 100)


@pytest.mark.parametrize(
    "puzzle, solution",
    [(puzzles[i], solutions[i]) for i in range(len(puzzles))],
)
def test_solver(puzzle, solution):
    sudoku = puzzle
    solver.solve(sudoku)
    assert np.array_equal(sudoku, solution)
