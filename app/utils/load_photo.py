import os
import cv2

desired_resolution = (1280, 960)


def crop_to_target_resolution(
    img, landscape_resolution=(2880, 2160), portrait_resolution=(2160, 2880)
):
    height, width = img.shape[:2]

    if width >= height:
        target_width, target_height = landscape_resolution  # Landscape
    else:
        target_width, target_height = portrait_resolution  # Portrait

    if target_width > width or target_height > height:
        raise ValueError("Target resolution exceeds the original image dimensions.")

    x_margin = (width - target_width) // 2
    y_margin = (height - target_height) // 2

    cropped_img = img[
        y_margin : y_margin + target_height, x_margin : x_margin + target_width
    ]
    # cv2.imwrite("cropped.jpg", cropped_img)

    return cropped_img


def loadPhoto(path):
    if not os.path.exists(path):
        raise FileNotFoundError("The file does not exist.")
    puzzle_image = cv2.imread(path)
    if puzzle_image is None:
        raise ValueError("The file is not an image.")
    puzzle_image = crop_to_target_resolution(puzzle_image)
    if puzzle_image.size // 3 > 1280 * 720:
        if puzzle_image.shape[0] > puzzle_image.shape[1]:
            puzzle_image = cv2.resize(
                puzzle_image, (desired_resolution[1], desired_resolution[0])
            )
        else:
            puzzle_image = cv2.resize(
                puzzle_image, (desired_resolution[0], desired_resolution[1])
            )
    return puzzle_image
