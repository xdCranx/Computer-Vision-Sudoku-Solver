import pytesseract
import time
import numpy as np
import cv2
from tensorflow.keras.models import load_model


def recognizeDigitOCR(cell):
    digit = None
    cell = cv2.resize(cell, (35, 35))
    char = pytesseract.image_to_string(
        cell, config="--psm 10 --oem 3 -c tessedit_char_whitelist=123456789"
    )
    char = char.strip()
    if char.isdigit() and 1 <= int(char) <= 9:
        digit = int(char)
    else:
        raise ValueError("Invalid digit detected")

    return digit


def recognizeDigitNN(cell):
    model = load_model("./app/neural_network/digit_recognizer_model.keras")
    cell = cv2.resize(cell, (28, 28))
    # cv2.imshow("cell", cell)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cell = cell / 255.0
    cell = cell.reshape(1, 28, 28, 1)
    digit = model.predict(cell)
    digit = np.argmax(digit)

    return digit


def recognizeDigits(cells, isOcr=False):
    digits = []
    for cell in cells:
        if np.isclose(cell, 0).sum() / (cell.shape[0] * cell.shape[1]) >= 0.97:
            digits.append(0)
        else:
            if isOcr:
                digit = recognizeDigitOCR(cell)
                digits.append(digit)
            else:
                digit = recognizeDigitNN(cell)
                digits.append(digit)

    return digits


def measureTime(cells):
    start = time.time()
    print("Start")
    digits = recognizeDigits(cells)
    end = time.time()
    print("End, Time taken: ", end - start)
    return digits
