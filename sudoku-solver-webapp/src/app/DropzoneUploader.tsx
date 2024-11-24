"use client";

import { useState } from "react";
import { useDropzone } from "react-dropzone";

const DropzoneUploader = () => {
  const [uploadMessage, setUploadMessage] = useState("");

  const onDrop = async (acceptedFiles: File[]) => {
    if (acceptedFiles.length === 0) return;

    const file = acceptedFiles[0];
    const reader = new FileReader();

    reader.onload = async () => {
      const base64Data = (reader.result as string).split(",")[1];
      try {
        const response = await fetch("/api/upload", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name: file.name,
            data: base64Data,
          }),
        });

        const result = await response.json();
        setUploadMessage(result.message || "Upload failed.");
      } catch {
        setUploadMessage("Failed to upload the file.");
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
      {uploadMessage && <p>{uploadMessage}</p>}
    </div>
  );
};

export default DropzoneUploader;
