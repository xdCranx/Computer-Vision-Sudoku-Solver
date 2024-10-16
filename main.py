from fastapi import FastAPI
from app.api.routers import sudoku


app = FastAPI(
    title="The Sudoku Recognizing And Solving API",
    description="This API recognizes the sudoku puzzle from the image and solves it.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)

app.include_router(sudoku.router)


@app.get("/")
async def root():
    return {"message": "Wlecome to sudoku solving API"}
