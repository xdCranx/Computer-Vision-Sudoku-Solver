import DropzoneUploader from "./DropzoneUploader";
import SudokuDisplay from "./SudokuDisplay";

export default function Home() {
const sudokuGrid: number[][] = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9],
];

  return (
    <main
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
      }}
    >
      <div style={{ maxWidth: '50%', padding: '2.5rem' }}>
        <h1 style={{ fontSize: '3.5rem', marginBottom: '10px' }}>Sudoku Solver</h1>
        <p style={{ fontSize: '1.25rem', }}>Upload picture of your sudoku puzzle</p>
      </div>
      <div style={{ maxWidth: '50%', padding: '2.5rem' }}>
      <DropzoneUploader />
      <SudokuDisplay grid={sudokuGrid} />
      </div>
    </main>
  );
}
