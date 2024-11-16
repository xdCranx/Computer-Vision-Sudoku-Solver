import cv2
import numpy as np
import utils


def findSudokuBox(img, org):
    __epsilon = 0.1

    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    polygon = None

    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, __epsilon * perimeter, True)

        if (
            len(approx) == 4
            and cv2.contourArea(contour) > 3000
            and cv2.isContourConvex(approx)
        ):
            polygon = approx
            break

    img_with_contours = cv2.drawContours(org, [polygon], -1, (0, 255, 0), 3)

    return polygon, img_with_contours

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

def splitIntoCells(top_view_img):
    cell_h = top_view_img.shape[0] // 9
    cell_w= top_view_img.shape[1] // 9

    cells = []
    for i in range(9):
        for j in range(9):
            cell = top_view_img[
                i * cell_h : (i + 1) * cell_h,
                j * cell_w : (j + 1) * cell_w,
            ]
            cells.append(cell)
    return cells


