def read_inputfile(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
    return grid

def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 'A':
                continue

            if not (r - 1 >= 0 and c - 1 >= 0 and r + 1 < rows and c + 1 < cols) and not \
               (r - 1 >= 0 and c + 1 < cols and r + 1 < rows and c - 1 >= 0):
                continue

            tl = grid[r-1][c-1]  # top-left
            br = grid[r+1][c+1]  # bottom-right
            tr = grid[r-1][c+1]  # top-right
            bl = grid[r+1][c-1]  # bottom-left

            valid_diag1 = (tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')
            valid_diag2 = (tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M')

            if valid_diag1 and valid_diag2:
                count += 1

    return count

file_path = 'input.txt'
grid = read_inputfile(file_path)
result = count_x_mas(grid)
print(result)