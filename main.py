from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import sudoku


app = FastAPI(
    title="The Sudoku Recognizing And Solving API",
    description="This API recognizes the sudoku puzzle from the image and solves it.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sudoku.router)


@app.get("/")
async def root():
    return {"message": "Wlecome to sudoku solving API"}
