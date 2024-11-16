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


