"use client";

import { useDropzone } from "react-dropzone";


interface DropzoneUploaderProps {
  setSudoku: (sudoku: number[][]) => void;
  setLoading: (loading: boolean) => void;
  setUploadMessage: (message: string) => void;
}

const DropzoneUploader: React.FC<DropzoneUploaderProps> = ({
  setSudoku,
  setUploadMessage,
  setLoading,
}) => {
  const onDrop = async (acceptedFiles: File[]) => {
    if (acceptedFiles.length === 0) return;

    const file = acceptedFiles[0];
    const reader = new FileReader();

    reader.onload = async () => {
      const base64Data = (reader.result as string).split(",")[1];
      setLoading(true);
      try {
        const response = await fetch("http://localhost:8000/sudoku", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name: file.name,
            data: base64Data,
          }),
        });

        const result = await response.json();
        setSudoku(result);
        setUploadMessage(result.message || undefined);
      } catch {
        setUploadMessage("Failed to upload the file.");
      } finally {
        setLoading(false);
      }
    };

    reader.readAsDataURL(file);
  };

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    accept: { "image/*": [".jpg"] },
    maxFiles: 1,
  });

  return (
    <div
      {...getRootProps()}
      className="dropzone"
    >
      <input {...getInputProps()} />
      <h2>Drag and drop your picture here</h2>
      <p>or click to browse</p>
    </div>
  );
};

export default DropzoneUploader;
