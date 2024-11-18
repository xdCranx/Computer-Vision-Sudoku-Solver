import pytest
import numpy as np
from app.recognize_sudoku import recognizeSudoku
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
                    [0, 0, 0, 0, 0, 6, 0, 7, 0],
                    [8, 1, 0, 9, 7, 0, 0, 0, 0],
                    [9, 0, 0, 0, 4, 5, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 6, 7],
                    [0, 3, 0, 0, 6, 7, 2, 5, 0],
                    [0, 0, 0, 3, 5, 0, 0, 0, 0],
                    [0, 0, 4, 0, 0, 1, 0, 0, 3],
                    [0, 0, 0, 0, 0, 2, 0, 1, 4],
                    [0, 2, 0, 0, 0, 4, 7, 9, 0]
                ]
            ),
        ),
        (
            "./sudoku_images/puzzle2.jpeg",
            np.array(
                [
                    [0, 6, 7, 0, 4, 9, 0, 3, 0],
                    [1, 2, 0, 5, 3, 0, 0, 0, 4],
                    [0, 9, 0, 7, 0, 0, 6, 0, 0],
                    [8, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 4, 9, 0, 8, 0, 5, 0, 0],
                    [2, 0, 0, 6, 1, 0, 3, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 3],
                    [0, 0, 0, 0, 0, 0, 9, 0, 6],
                    [4, 0, 0, 0, 0, 3, 0, 7, 0]
                ]
            ),
        ),
    ],
)
def test_recognize_sudoku(loaded_image, img_path, solution):
    solved = recognizeSudoku(loaded_image)
    np.testing.assert_array_equal(solved, solution)
