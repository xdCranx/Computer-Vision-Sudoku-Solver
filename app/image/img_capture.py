import cv2
import time
from preprocess import preprocess
from process import (
    findSudokuBox,
    extractSudokuBox,
    applyGridMask,
)

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
                cv2.imshow("lines", grid)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return "Video Capture Ended"


if __name__ == "__main__":
    videoCapture()
