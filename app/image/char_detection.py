import pytesseract
import time
import cv2


def celanupCells(cells):
    cleaned_cells = []
    for cell in cells:
        cell = cv2.bitwise_not(cell)

        cv2.imshow("cell", cell)

        cleaned_cells.append(cell)
    return cleaned_cells


def recognizeDigits(cells):
    digits = []
    cells = celanupCells(cells)
    for cell in cells:
        digit = pytesseract.image_to_string(
            cell, config="--psm 10 --oem 3 -c tessedit_char_whitelist=123456789"
        )
        digits.append(digit)
    return digits


def measureTime(cells):
    start = time.time()
    print("Start")
    digits = recognizeDigits(cells)
    end = time.time()
    print("End, Time taken: ", end - start)
    return digits
