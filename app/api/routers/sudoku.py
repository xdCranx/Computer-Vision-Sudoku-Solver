from fastapi import APIRouter


router = APIRouter(prefix="/sudoku", tags=["sudoku"])


@router.get("/")
async def get_placeholder_message():
    return {"message": "This is a placeholder message for sudoku router."}
