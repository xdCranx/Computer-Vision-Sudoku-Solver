"use client"

import React from "react";

interface SudokuDisplayProps {
  grid: number[][]; // 9x9 grid of numbers, with 0 representing empty cells
}

const SudokuDisplay: React.FC<SudokuDisplayProps> = ({ grid }) => {
  const [sudokuGrid, setSudokuGrid] = React.useState(grid);

  
  return (
    <div className="sudoku-grid">
      {grid.map((row, rowIndex) => {
        return row.map((cell, colIndex) => {
          // Apply thicker borders for cells on the edges of 3x3 subgrids
          const isRightBorder = colIndex % 3 === 2 && colIndex !== 8;
          const isBottomBorder = rowIndex % 3 === 2 && rowIndex !== 8;

          return (
            <div
              key={`${rowIndex}-${colIndex}`}
              className={`sudoku-cell ${isRightBorder ? "right-border" : ""} ${
                isBottomBorder ? "bottom-border" : ""
              }`}
            >
              {cell !== 0 ? cell : ""}
            </div>
          );
        });
      })}
    </div>
  );
};

export default SudokuDisplay;
