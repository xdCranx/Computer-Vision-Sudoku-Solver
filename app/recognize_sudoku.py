import app.image as image


def recognizeSudoku(img):
    grey = image.preprocess(img)
    corners = image.findSudokuBox(grey)
    if corners is not None:
        sudoku_box = image.extractSudokuBox(img, corners)
        sudoku = image.preprocess(sudoku_box)
        grid_lines = image.getGridLines(sudoku)
        mask = image.createGridMask(grid_lines)
        masked_grid = image.applyGridMask(sudoku, mask)
        cells = image.splitIntoCells(masked_grid)
        clean_cells = image.cleanCells(cells)
        recognized_digits = image.recognizeDigits(clean_cells)
        puzzle = image.utils.convertTo2D(recognized_digits)
        return puzzle
