from app.solver import solver, lp_solver, cp_solver
from app.utils import load_sudoku
import pytest
import numpy as np

puzzles, solutions = load_sudoku.from_csv("./sudoku-solver-api/sudoku.csv", 10)


@pytest.mark.parametrize(
    "puzzle, solution",
    [(puzzles[i], solutions[i]) for i in range(len(puzzles))],
)
def test_solver(puzzle, solution):
    sudoku = puzzle
    solver.solve(sudoku)
    assert np.array_equal(sudoku, solution)


@pytest.mark.parametrize(
    "puzzle, solution",
    [(puzzles[i], solutions[i]) for i in range(len(puzzles))],
)
def test_lpSolver(puzzle, solution):
    sudoku = puzzle
    lp_solver.lpSolve(sudoku)
    assert np.array_equal(sudoku, solution)


@pytest.mark.parametrize(
    "puzzle, solution",
    [(puzzles[i], solutions[i]) for i in range(len(puzzles))],
)
def test_cpSolver(puzzle, solution):
    cp_solver.cpSolve(puzzle)
    assert np.array_equal(puzzle, solution)
