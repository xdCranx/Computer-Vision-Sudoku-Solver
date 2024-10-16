def validCheck(board, row, col, val):
    # Check row
    if val in board[row]:
        return False

    # Check column
    if val in board[:, col]:
        return False

    # Check box
    boxRow = row // 3 * 3
    boxCol = col // 3 * 3
    if val in board[boxRow : boxRow + 3, boxCol : boxCol + 3]:
        return False

    return True


def constraintUpdate(board):
    possibleVals = [
        [set(range(1, 10)) if board[i][j] == 0 else set() for j in range(9)]
        for i in range(9)
    ]

    changed = True
    while changed:
        changed = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    currentPossibleVals = possibleVals[i][j]

                    # Row check
                    currentPossibleVals -= {
                        board[i][k] for k in range(9) if board[i][k] != 0
                    }

                    # Column check
                    currentPossibleVals -= {
                        board[k][j] for k in range(9) if board[k][j] != 0
                    }

                    # Box check
                    boxRow = i // 3 * 3
                    boxCol = j // 3 * 3
                    currentPossibleVals -= {
                        board[k][l]
                        for k in range(boxRow, boxRow + 3)
                        for l in range(boxCol, boxCol + 3)
                        if board[k][l] != 0
                    }

                    if len(currentPossibleVals) < len(possibleVals[i][j]):
                        changed = True
                        possibleVals[i][j] = currentPossibleVals
    return possibleVals


def getEmptyCell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve(board):
    emptyCell = getEmptyCell(board)
    if emptyCell is None:
        return True

    row, col = emptyCell
    possibleVals = constraintUpdate(board)[row][col]
    for val in possibleVals:
        if validCheck(board, row, col, val):
            board[row][col] = val
            if solve(board):
                return True
            board[row][col] = 0
    return False
