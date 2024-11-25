import pytest
import numpy as np
from app.recognize_sudoku import recognizeSudoku
from app.utils.load_photo import loadPhoto


np.set_printoptions(threshold=np.inf)

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
                    [0, 0, 0, 9, 0, 0, 0, 4, 0],
                    [0, 0, 0, 6, 4, 0, 2, 1, 3],
                    [4, 0, 5, 3, 0, 0, 0, 0, 9],
                    [3, 5, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 1, 7, 8, 0, 6, 0, 0],
                    [8, 0, 0, 0, 0, 6, 0, 0, 4],
                    [0, 1, 3, 0, 0, 7, 0, 6, 2],
                    [0, 0, 0, 0, 5, 0, 7, 0, 8],
                    [9, 0, 7, 2, 0, 0, 3, 0, 0]
                ]
            ),
        ),
        (
            "./sudoku_images/puzzle2.jpeg",
            np.array(
                [
                    [5, 0, 6, 0, 0, 2, 0, 9, 0],
                    [0, 8, 9, 0, 0, 0, 0, 1, 4],
                    [4, 0, 0, 9, 7, 0, 0, 0, 5],
                    [0, 1, 0, 0, 0, 0, 4, 0, 0],
                    [0, 7, 0, 5, 6, 4, 0, 0, 0],
                    [0, 4, 0, 2, 3, 0, 0, 8, 9],
                    [0, 0, 3, 7, 8, 9, 0, 0, 0],
                    [8, 0, 0, 0, 0, 0, 5, 0, 1],
                    [2, 0, 4, 3, 0, 5, 9, 0, 0]
                ]
            ),
        ),
    ],
)
def test_recognize_sudoku(loaded_image, img_path, solution):
    solved = recognizeSudoku(loaded_image)
    np.testing.assert_array_equal(solved, solution)
