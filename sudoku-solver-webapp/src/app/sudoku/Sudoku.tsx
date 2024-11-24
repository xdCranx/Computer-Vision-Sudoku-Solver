"use client"
import { useState } from "react";
import DropzoneUploader from "./DropzoneUploader";
import SudokuDisplay from "./SudokuDisplay";

const Sudoku: React.FC = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const [uploadMessage, setUploadMessage] = useState<string>("");
  const [sudoku, setSudoku] = useState<number[][]>([]);
  const [isSudokuSolved, setIsSudokuSolved] = useState<boolean>(false);

  if (loading) {
    return <p>Loading...</p>;
  }
  if (uploadMessage) {
    return <p>{uploadMessage}</p>;
  }

  return (
    <div style={{ maxWidth: '50%', padding: '2.5rem', justifyItems: "center" }}>
      <DropzoneUploader
        setSudoku={setSudoku}
        setLoading={setLoading}
        setUploadMessage={setUploadMessage}
      />
      <SudokuDisplay grid={sudoku} />
    </div>
  )
};

export default Sudoku;