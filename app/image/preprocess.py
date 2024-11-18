import cv2


def preprocess(img):
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(grayscale, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2
    )

    invert = cv2.bitwise_not(thresh)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    morph = cv2.morphologyEx(invert, cv2.MORPH_OPEN, kernel)

    result = cv2.dilate(morph, kernel, iterations=1)

    return result
