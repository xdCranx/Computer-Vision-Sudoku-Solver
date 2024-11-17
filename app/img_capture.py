import cv2
import time
from image.preprocess import preprocess
from image.process import (
    findSudokuBox,
    extractSudokuBox,
    applyGridMask,
    splitIntoCells,
    cleanCells,
)
from image.char_detection import recognizeDigitsOCR, measureTime
from image.utils import convertTo2D
import utils
import utils.print_sudoku_board

# resolution = (1920, 1080)
# resolution = (1280, 720)
resolution = (1024, 768)
# resolution = (800, 600)

fps = 5


def videoCapture():
    cap = cv2.VideoCapture(0)
    cap.set(3, resolution[0])
    cap.set(4, resolution[1])

    time_diff = 0

    while True:
        time_curr = time.time() - time_diff
        ret, frame = cap.read()

        if time_curr > 1.0 / fps:
            time_diff = time.time()
            grey = preprocess(frame)

            corners, contour_img = findSudokuBox(grey, frame)
            if corners is not None:
                sudoku = extractSudokuBox(frame, corners)
                sudoku = preprocess(sudoku)
                grid = applyGridMask(sudoku)
                cells = splitIntoCells(grid)
                cleaned_cells = cleanCells(cells)
                recognized_digits = measureTime(cleaned_cells)
                puzzle = convertTo2D(recognized_digits)
                utils.print_sudoku_board.print_sudoku_board(puzzle)

                cv2.imshow("grid", cells[0])

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return "Video Capture Ended"


if __name__ == "__main__":
    videoCapture()
