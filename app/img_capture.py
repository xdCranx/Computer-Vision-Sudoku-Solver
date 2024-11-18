import cv2
import time
import image
import image.utils
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
            grey = image.preprocess(frame)

            corners = image.findSudokuBox(grey)
            if corners is not None:
                sudoku = image.extractSudokuBox(frame, corners)
                sudoku = image.preprocess(sudoku)
                grid = image.applyGridMask(sudoku)
                cells = image.splitIntoCells(grid)
                cleaned_cells = image.cleanCells(cells)

                recognized_digits = image.measureTime(cleaned_cells)
                puzzle = image.utils.convertTo2D(recognized_digits)
                utils.print_sudoku_board.print_sudoku_board(puzzle)

                cv2.imshow("grid", sudoku)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return "Video Capture Ended"


if __name__ == "__main__":
    videoCapture()
