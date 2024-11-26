"use client"
import { Button } from "@mui/material";

const ResetButton = () => {

  return (
    <Button variant="contained" className="button" size='large'
      onClick={() => typeof window !== "undefined" && window.location.reload()}
    >RESET</Button>
  );
}

export default ResetButton;