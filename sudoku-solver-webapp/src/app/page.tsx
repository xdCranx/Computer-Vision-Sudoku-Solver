import Sudoku from "./sudoku/Sudoku";
import Button from "@mui/material/Button";

export default function Home() {


  return (
    <main>
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
      }}>
        <div style={{ maxWidth: '50%', padding: '2.5rem' }}>
          <h1 style={{ fontSize: '3.5rem', marginBottom: '10px' }}>Sudoku Solver</h1>
          <p style={{ fontSize: '1.25rem', }}>Upload picture of your sudoku puzzle</p>
          <Button variant="outlined" className="button">SOLVE</Button>
        </div>

        <Sudoku/>
      </div>
    </main>
  );
}
