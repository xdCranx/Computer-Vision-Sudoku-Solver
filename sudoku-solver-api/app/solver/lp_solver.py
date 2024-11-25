import pulp as plp


def defaultSudokuConstraints(problem, grid_vars, rows, cols, grids, vals):
    # 1. Only one value per cell
    for row in rows:
        for col in cols:
            problem.addConstraint(
                plp.LpConstraint(
                    e=plp.lpSum(grid_vars[row][col].values()),
                    sense=plp.LpConstraintEQ,
                    rhs=1,
                    name=f"constraint_1_{row}_{col}",
                )
            )

    # 2. Only one of each value per row
    for row in rows:
        for val in vals:
            problem.addConstraint(
                plp.LpConstraint(
                    e=plp.lpSum([grid_vars[row][col][val] * val for col in cols]),
                    sense=plp.LpConstraintEQ,
                    rhs=val,
                    name=f"constraint_2_{row}_{val}",
                )
            )

    # 3. Only one of each value per column
    for col in cols:
        for val in vals:
            problem.addConstraint(
                plp.LpConstraint(
                    e=plp.lpSum([grid_vars[row][col][val] * val for row in rows]),
                    sense=plp.LpConstraintEQ,
                    rhs=val,
                    name=f"constraint_3_{col}_{val}",
                )
            )

    # 4. Only one of each value per 3x3 grid
    for grid in grids:
        for value in vals:
            problem.addConstraint(
                plp.LpConstraint(
                    e=plp.lpSum(
                        [
                            grid_vars[(grid // 3) * 3 + row][(grid % 3) * 3 + col][
                                value
                            ]
                            * value
                            for col in range(3)
                            for row in range(3)
                        ]
                    ),
                    sense=plp.LpConstraintEQ,
                    rhs=value,
                    name=f"constraint_uniq_grid_{grid}_{value}",
                )
            )


def loadValues(problem, input_sudoku, grid_vars, rows, cols, vals):
    for row in rows:
        for col in cols:
            if input_sudoku[row][col] != 0:
                problem.addConstraint(
                    plp.LpConstraint(
                        e=plp.lpSum(
                            [grid_vars[row][col][value] * value for value in vals]
                        ),
                        sense=plp.LpConstraintEQ,
                        rhs=input_sudoku[row][col],
                        name=f"prefilled_value_constraint_{row}_{col}",
                    )
                )


def returnSolution(grid_vars, rows, cols, vals):
    solution = []
    for row in rows:
        row_values = []
        for col in cols:
            for val in vals:
                if plp.value(grid_vars[row][col][val]) == 1:
                    row_values.append(val)
        solution.append(row_values)
    return solution


def lpSolve(puzzle):
    problem = plp.LpProblem("Sudoku_Solving")

    problem.setObjective(plp.lpSum([]))

    rows = range(0, 9)
    cols = range(0, 9)
    grids = range(0, 9)
    vals = range(1, 10)

    grid_vars = plp.LpVariable.dicts("grid_val", (rows, cols, vals), cat=plp.LpBinary)

    defaultSudokuConstraints(problem, grid_vars, rows, cols, grids, vals)

    loadValues(problem, puzzle, grid_vars, rows, cols, vals)

    problem.solve()

    status = plp.LpStatus[problem.status]
    if status == "Optimal":
        return returnSolution(grid_vars, rows, cols, vals)
