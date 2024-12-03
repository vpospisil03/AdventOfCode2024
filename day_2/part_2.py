def read_input_file(file_path):
    with open(file_path, 'r') as file:
        data = [list(map(int, line.split())) for line in file.readlines()]
    return data

def validate_levels(data):
    safe_reports = 0
    for level in data:
        if is_valid_level(level):
            safe_reports += 1
    return safe_reports

def is_valid_level(level):
    def check_increasing(level):
        return all(level[i] < level[i + 1] for i in range(len(level) - 1))

    def check_decreasing(level):
        return all(level[i] > level[i + 1] for i in range(len(level) - 1))

    def check_difference(level):
        return all(1 <= abs(level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))

    if (check_increasing(level) or check_decreasing(level)) and check_difference(level):
        return True

    for i in range(len(level)):
        new_level = level[:i] + level[i + 1:]
        if (check_increasing(new_level) or check_decreasing(new_level)) and check_difference(new_level):
            return True

    return False

file_path = "input.txt"
data = read_input_file(file_path)
safe_reports = validate_levels(data)
print(safe_reports)
