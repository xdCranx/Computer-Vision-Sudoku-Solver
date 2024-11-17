from ortools.sat.python import cp_model


def cpSolve(puzzle):
    model = cp_model.CpModel()

    line = list(range(9))
    box = list(range(3))

    vars_grid = {}

    for i in line:
        for j in line:
            vars_grid[i, j] = model.NewIntVar(1, 9, f"cell_{i}_{j}")

    for i in line:
        model.AddAllDifferent([vars_grid[i, j] for j in line])
        model.AddAllDifferent([vars_grid[j, i] for j in line])

    for i in box:
        for j in box:
            model.AddAllDifferent(
                [vars_grid[i * 3 + k, j * 3 + l] for k in box for l in box]
            )

    for i in line:
        for j in line:
            if puzzle[i][j] != 0:
                model.Add(vars_grid[i, j] == puzzle[i][j])

    solver = cp_model.CpSolver()

    # multithreading
    # solver.parameters.num_search_workers = 4

    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        for i in line:
            for j in line:
                puzzle[i][j] = solver.Value(vars_grid[i, j])
    return puzzle
