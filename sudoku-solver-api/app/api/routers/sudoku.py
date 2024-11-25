from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
import cv2

router = APIRouter(prefix="/sudoku", tags=["sudoku"])


class SudokuUploadRequest(BaseModel):
    name: str
    data: str


@router.get("/")
async def get_placeholder_message():
    return {"message": "This is a placeholder message for sudoku router."}


@router.post("/")
async def solve_from_array(sudoku: SudokuUploadRequest):
    from app.detect_and_solve import detectAndSolve
    import base64

    decoded_image = base64.b64decode(sudoku.data)

    np_image = np.frombuffer(decoded_image, dtype=np.uint8)
    sudoku_image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    solved = detectAndSolve(sudoku_image)

    return solved.tolist()
