"use client"
import { useState } from "react";
import DropzoneUploader from "./DropzoneUploader";
import SudokuDisplay from "./SudokuDisplay";
import LoadingCircle from "./LoadingCircle";

const Sudoku: React.FC = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const [uploadMessage, setUploadMessage] = useState<string>("");
  const [sudoku, setSudoku] = useState<number[][] | null>(null);
  if (loading) {
    return (
      <div style={{ width: "50%", padding: "2.5rem", justifyItems: "center" }}>
      <LoadingCircle />
      </div>
    );
  }
  if (uploadMessage) {
    return (
      <div style={{ width: "50%", padding: "2.5rem", justifyItems: "center" }}>
        <p>{uploadMessage}</p>
      </div>
    );  }

  return (
    <div style={{ width:'50%', padding: '2.5rem', justifyItems: "center" }}>
      {sudoku 
      ? (
        <SudokuDisplay grid={sudoku!} />
      ) 
      : (
        <DropzoneUploader
          setSudoku={setSudoku}
          setLoading={setLoading}
          setUploadMessage={setUploadMessage}
        />)}
    </div>
  )
};

export default Sudoku;