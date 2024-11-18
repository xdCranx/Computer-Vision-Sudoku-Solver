import cv2
import numpy as np


def draw_points(image, points, color=(0, 0, 255), radius=4):
    for point in points:
        cv2.circle(image, (int(point[0]), int(point[1])), radius, color, -1)
    return image


def sort_corners(corners):
    if corners.shape != (4, 1, 2):
        raise ValueError("Corners must be a (4, 1, 2) shaped array.")

    reshaped_corners = corners.reshape(4, 2)

    s = reshaped_corners.sum(axis=1)
    diff = np.diff(reshaped_corners, axis=1)

    tl = reshaped_corners[np.argmin(s)]
    br = reshaped_corners[np.argmax(s)]
    tr = reshaped_corners[np.argmin(diff)]
    bl = reshaped_corners[np.argmax(diff)]

    return np.array([tl, tr, br, bl], dtype="float32")


def drawLines(img, lines, colored=False):
    if colored:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        __color = (0, 0, 255)
    else:
        __color = 255

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv2.line(img, pt1, pt2, __color, 6, cv2.LINE_AA)

        return img


def convertTo2D(cells):
    return [cells[i : i + 9] for i in range(0, 81, 9)]

def sudokuFromCells(cells):
    if len(cells) != 81:
        raise ValueError("The list must contain exactly 81 image cells.")
        
    rows = []
    for i in range(9):
        row = np.hstack(cells[i * 9:(i + 1) * 9])
        rows.append(row)
    
    sudoku_grid = np.vstack(rows)
    
    return sudoku_grid
