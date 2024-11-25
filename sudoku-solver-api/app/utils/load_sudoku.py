import numpy as np


def from_csv(file_path: str, num_lines: int = None):
    with open(file_path, "r") as file:
        sudoku_data = []
        for i, line in enumerate(file):
            if num_lines is not None and i >= num_lines:
                break

            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 2:
                print(f"Skipping invalid line: {line}")  # Debugging line
                continue

            puzzle, solution = parts

            # Convert strings to lists of integers
            try:
                puzzle_array = np.array(list(map(int, puzzle.strip()))).reshape(9, 9)
                solution_array = np.array(list(map(int, solution.strip()))).reshape(
                    9, 9
                )
            except ValueError as e:
                print(f"Error converting line: {line}. Error: {e}")
                continue

            sudoku_data.append(
                {
                    "puzzle": puzzle_array,
                    "solution": solution_array,
                }
            )

    # Create numpy arrays for puzzles and solutions
    puzzles = np.array([case["puzzle"] for case in sudoku_data])
    solutions = np.array([case["solution"] for case in sudoku_data])

    return puzzles, solutions


def copy_csv_lines(input_file_path: str, output_file_path: str, num_lines: int):
    with open(input_file_path, "r") as input_file:
        with open(output_file_path, "w") as output_file:
            for i, line in enumerate(input_file):
                if i >= num_lines:
                    break
                output_file.write(line)

    print(f"Copied {num_lines} lines from '{input_file_path}' to '{output_file_path}'.")
