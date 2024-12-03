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
    increasing = all(level[i] < level[i + 1] for i in range(len(level) - 1))
    decreasing = all(level[i] > level[i + 1] for i in range(len(level) - 1))
    
    difference_valid = all(1 <= abs(level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))
    
    return (increasing or decreasing) and difference_valid

file_path = "input.txt"
data = read_input_file(file_path)
safe_reports = validate_levels(data)
print(safe_reports)
