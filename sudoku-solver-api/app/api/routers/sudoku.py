from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/sudoku", tags=["sudoku"])

class SudokuUploadRequest(BaseModel):
    name: str
    data: str

@router.get("/")
async def get_placeholder_message():
    return {"message": "This is a placeholder message for sudoku router."}


@router.post("/")
async def solve_from_array(sudoku: SudokuUploadRequest):
    from app.solve_from_image import solveFromImage
    import base64
    decoded_sudoku = base64.b64decode(sudoku.data)

    sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    return sudoku
