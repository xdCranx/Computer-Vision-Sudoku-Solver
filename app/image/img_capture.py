import time
import cv2

# from image.preprocess import preprocess
from preprocess import preprocess
from process import findSudokuBox

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
        img_with_contours, polygon = findSudokuBox(grey, frame)
        cv2.imshow("frame", img_with_contours)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return "Video Capture Ended"


if __name__ == "__main__":
    videoCapture()
