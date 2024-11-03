from fastapi import APIRouter


router = APIRouter(prefix="/sudoku", tags=["sudoku"])


@router.get("/")
async def get_placeholder_message():
    return {"message": "This is a placeholder message for sudoku router."}


@router.post("/solve-from-array")
async def solve_from_array(sudoku_puzzle):
    from solver.solver import solve

    return solve(sudoku_puzzle)
