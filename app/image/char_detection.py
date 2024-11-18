import pytesseract
import time
import cv2
import numpy as np


def recognizeDigitOCR(cell):
    digit = None
    char = pytesseract.image_to_string(
        cell, config="--psm 10 --oem 3 -c tessedit_char_whitelist=123456789"
    )
    char = char.strip()
    if char.isdigit() and 1 <= int(char) <= 9:
        digit = int(char)
    else:
        cv2.imshow(char, cell)
        raise ValueError("Invalid digit detected: ", char)

    return digit


def recognizeDigits(cells, isOcr=True):
    digits = []
    for cell in cells:
        if np.isclose(cell, 0).sum() / (cell.shape[0] * cell.shape[1]) >= 0.97:
            digits.append(0)
        else:
            if isOcr:
                digit = recognizeDigitOCR(cell)
                digits.append(digit)
            else:
                print("Not implemented yet")
    return digits


def measureTime(cells):
    start = time.time()
    print("Start")
    digits = recognizeDigits(cells)
    end = time.time()
    print("End, Time taken: ", end - start)
    return digits
