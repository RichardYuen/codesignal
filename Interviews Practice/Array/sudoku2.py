def sudoku2(grid):
    for row in range(9):
        d = {}
        for col in range(9):
            val = grid[row][col]
            if val != '.' and val in d:
                return False
            else:
                d[val] = 1
    
    for col in range(9):
        d = {}
        for row in range(9):
            grid[row][col]
            val = grid[row][col]
            if val != '.' and val in d:
                return False
            else:
                d[val] = 1
    
    for box in range(9):
        d = {}
        start_row = (box // 3) * 3
        for row in range(3):
            start_col = (box % 3) * 3
            for col in range(3):
                val = grid[start_row+row][start_col + col]
                if val != '.' and val in d:
                    return False
                else:
                    d[val] = 1

    return True