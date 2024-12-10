"use client"

import React from "react";

interface SudokuDisplayProps {
  grid: number[][];
}

const SudokuDisplay: React.FC<SudokuDisplayProps> = ({ grid }) => {
  return (
    <div className="sudoku-grid">
      {grid.map((row, rowIndex) => {
        return row.map((cell, colIndex) => {
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
