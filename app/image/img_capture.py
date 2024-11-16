import cv2

# from image.preprocess import preprocess
from preprocess import preprocess
from process import findSudokuBox, extractSudokuBox, splitIntoCells

# resolution = (1920, 1080)
resolution = (1280, 720)
# resolution = (1024, 768)
# resolution = (800, 600)


def videoCapture():
    cap = cv2.VideoCapture(0)
    cap.set(3, resolution[0])
    cap.set(4, resolution[1])

    while True:
        ret, frame = cap.read()
        grey = preprocess(frame)
        corners, contour_img = findSudokuBox(grey, frame)
        if corners is not None:
            sudoku = extractSudokuBox(contour_img, corners)
            cell = splitIntoCells(sudoku)
            cv2.imshow("frame", cell[1])
        else:
            cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return "Video Capture Ended"


if __name__ == "__main__":
    videoCapture()
