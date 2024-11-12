import cv2


def findSudokuBox(img, org):
    __epsilon = 0.02

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
            polygon = contour
            break

    x, y, w, h = cv2.boundingRect(polygon)
    img_with_contours = cv2.drawContours(org, [polygon], -1, (0, 255, 0), 3)

    corners = (
        (x, y),
        (x + w, y),
        (x, y + h),
        (x + w, y + h),
    )

    return img_with_contours, corners
