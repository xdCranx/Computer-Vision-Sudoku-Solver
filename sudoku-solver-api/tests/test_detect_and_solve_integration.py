import pytest
import numpy as np
from app.detect_and_solve import detectAndSolve
from app.utils.load_photo import loadPhoto


@pytest.fixture
def loaded_image(img_path):
    try:
        return loadPhoto(img_path)
    except Exception as e:
        return e


@pytest.mark.parametrize(
    "img_path, solution",
    [
        (
            "./sudoku-solver-api/sudoku_images/puzzle1.jpeg",
            np.array(
                [
                    [1, 3, 2, 9, 7, 8, 5, 4, 6],
                    [7, 9, 8, 6, 4, 5, 2, 1, 3],
                    [4, 6, 5, 3, 1, 2, 8, 7, 9],
                    [3, 5, 6, 4, 2, 1, 9, 8, 7],
                    [2, 4, 1, 7, 8, 9, 6, 3, 5],
                    [8, 7, 9, 5, 3, 6, 1, 2, 4],
                    [5, 1, 3, 8, 9, 7, 4, 6, 2],
                    [6, 2, 4, 1, 5, 3, 7, 9, 8],
                    [9, 8, 7, 2, 6, 4, 3, 5, 1],
                ]
            ),
        ),
        (
            "./sudoku-solver-api/sudoku_images/puzzle2.jpeg",
            np.array(
                [
                    [5, 3, 6, 1, 4, 2, 8, 9, 7],
                    [7, 8, 9, 6, 5, 3, 2, 1, 4],
                    [4, 2, 1, 9, 7, 8, 3, 6, 5],
                    [3, 1, 2, 8, 9, 7, 4, 5, 6],
                    [9, 7, 8, 5, 6, 4, 1, 2, 3],
                    [6, 4, 5, 2, 3, 1, 7, 8, 9],
                    [1, 5, 3, 7, 8, 9, 6, 4, 2],
                    [8, 9, 7, 4, 2, 6, 5, 3, 1],
                    [2, 6, 4, 3, 1, 5, 9, 7, 8],
                ]
            ),
        ),
    ],
)
def test_detectAndSolve(loaded_image, img_path, solution):
    solved = detectAndSolve(loaded_image)
    print(solved)
    print(solution)
    np.testing.assert_array_equal(solved, solution)
