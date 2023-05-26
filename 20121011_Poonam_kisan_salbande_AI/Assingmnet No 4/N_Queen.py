def is_safe(board, row, col, n):
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(n):
    board = [[0 for x in range(n)] for y in range(n)]

    def solve_n_queens_util(col):
        # Base case: If all queens are placed
        if col >= n:
            return True

        # Try placing the queen in each row of the current column
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1

                # Recur to place the remaining queens
                if solve_n_queens_util(col + 1):
                    return True

                # If placing the queen in the current row doesn't lead to a solution,
                # backtrack and try the next row
                board[i][col] = 0

        return False

    if solve_n_queens_util(0) is False:
        print("Solution does not exist")
        return

    # Print the solution
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

