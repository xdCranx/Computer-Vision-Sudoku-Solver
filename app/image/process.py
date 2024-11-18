import cv2
import numpy as np
import image.utils as utils


def findSudokuBox(img):
    __epsilon = 0.1

    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    polygon = None

    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, __epsilon * perimeter, True)

        if (
            len(approx) == 4
            and cv2.contourArea(contour) > 300000
            and cv2.isContourConvex(approx)
        ):
            polygon = approx
            break

    return polygon


def extractSudokuBox(img, corners):
    sorted_corners = utils.sort_corners(corners)

    tl, tr, br, bl = sorted_corners

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array(
        [
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1],
        ],
        dtype="float32",
    )

    M = cv2.getPerspectiveTransform(sorted_corners, dst)
    warp = cv2.warpPerspective(img, M, (maxWidth, maxHeight))

    return warp


def getGridLines(img):
    tmp = img.copy()

    row_len = img.shape[0]
    col_len = img.shape[1]

    row_size = row_len // 13
    col_size = col_len // 13

    row_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (row_size, 1))
    col_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, col_size))

    horizontal = cv2.erode(tmp, row_kernel)
    horizontal = cv2.dilate(horizontal, row_kernel)

    vertical = cv2.erode(tmp, col_kernel)
    vertical = cv2.dilate(vertical, col_kernel)

    grid = cv2.add(horizontal, vertical)

    cv2.imshow("grid", grid)

    return grid


def createGridMask(grid):
    grid = cv2.dilate(
        grid, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=2
    )

    full_lines = cv2.HoughLines(grid, 0.3, np.pi / 90, 250)
    grid_mask = utils.drawLines(grid, full_lines)

    return grid_mask


def applyGridMask(img, mask):
    mask = cv2.bitwise_not(mask)
    masked_img = cv2.bitwise_and(img, mask)

    return masked_img


def splitIntoCells(top_view_img):
    cell_h = top_view_img.shape[0] // 9
    cell_w = top_view_img.shape[1] // 9

    cells = []
    for i in range(9):
        for j in range(9):
            cell = top_view_img[
                i * cell_h : (i + 1) * cell_h,
                j * cell_w : (j + 1) * cell_w,
            ]
            cells.append(cell)
    return cells


def cleanCells(cells):
    cleaned_cells = []
    for cell in cells:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
        cell = cv2.morphologyEx(cell, cv2.MORPH_OPEN, kernel)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        cell = cv2.erode(cell, kernel, iterations=1)
        cell = cv2.resize(cell, (35, 35))
        cleaned_cells.append(cell)
    return cleaned_cells
