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
            "./sudoku_images/puzzle1.jpeg",
            np.array(
                [
                    [3, 4, 5, 8, 1, 6, 9, 7, 2],
                    [8, 1, 2, 9, 7, 3, 6, 4, 5],
                    [9, 6, 7, 2, 4, 5, 1, 3, 8],
                    [5, 9, 1, 4, 2, 8, 3, 6, 7],
                    [4, 3, 8, 1, 6, 7, 2, 5, 9],
                    [2, 7, 6, 3, 5, 9, 4, 8, 1],
                    [6, 8, 4, 7, 9, 1, 5, 2, 3],
                    [7, 5, 9, 6, 3, 2, 8, 1, 4],
                    [1, 2, 3, 5, 8, 4, 7, 9, 6],
                ]
            ),
        ),
        (
            "./sudoku_images/puzzle2.jpeg",
            np.array(
                [
                    [5, 6, 7, 8, 4, 9, 2, 3, 1],
                    [1, 2, 8, 5, 3, 6, 7, 9, 4],
                    [3, 9, 4, 7, 2, 1, 6, 5, 8],
                    [8, 3, 1, 2, 9, 5, 4, 6, 7],
                    [6, 4, 9, 3, 8, 7, 5, 1, 2],
                    [2, 7, 5, 6, 1, 4, 3, 8, 9],
                    [9, 5, 6, 1, 7, 2, 8, 4, 3],
                    [7, 1, 3, 4, 5, 8, 9, 2, 6],
                    [4, 8, 2, 9, 6, 3, 1, 7, 5],
                ]
            ),
        ),
    ],
)
def test_detectAndSolve(loaded_image, img_path, solution):
    solved = detectAndSolve(loaded_image)
    np.testing.assert_array_equal(solved, solution)
