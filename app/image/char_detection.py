import pytesseract
import time


def recognizeDigitsOCR(cells):
    digits = []
    for cell in cells:
        char = pytesseract.image_to_string(
            cell, config="--psm 10 --oem 3 -c tessedit_char_whitelist=123456789"
        )
        char = char.strip()
        if char == "":
            digit = 0
        elif char.isdigit() and 1 <= int(char) <= 9:
            digit = int(char)
        else:
            raise ValueError("Invalid digit detected: ", char)
        digits.append(digit)
    return digits


def measureTime(cells):
    start = time.time()
    print("Start")
    digits = recognizeDigitsOCR(cells)
    end = time.time()
    print("End, Time taken: ", end - start)
    return digits
