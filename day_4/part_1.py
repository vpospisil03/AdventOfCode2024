def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def is_valid_position(x, y, max_x, max_y):
    return 0 <= x < max_x and 0 <= y < max_y

def count_xmas_occurrences(grid):
    directions = [
        (0, 1),  # right
        (0, -1), # left
        (1, 0),  # down
        (-1, 0), # up
        (1, 1),  # down-right
        (1, -1), # down-left
        (-1, 1), # up-right
        (-1, -1) # up-left
    ]

    word = "XMAS"
    word_length = len(word)
    count = 0
    max_x = len(grid)
    max_y = len(grid[0]) if max_x > 0 else 0

    for r in range(max_x):
        for c in range(max_y):
            for dx, dy in directions:
                if all(is_valid_position(r + ch * dx, c + ch * dy, max_x, max_y) and
                       grid[r + ch * dx][c + ch * dy] == word[ch] for ch in range(word_length)):
                    count += 1
    return count

file_path = 'input.txt'
grid = read_input_file(file_path)
xmas_count = count_xmas_occurrences(grid)
print(xmas_count)
