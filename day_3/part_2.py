import re

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def get_multiplication_sum(data):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'
    matches = re.finditer(pattern, data)
    
    total_sum = 0
    multiplication_enabled = True

    for match in matches:
        if match.group(1) and match.group(2):
            if multiplication_enabled:
                x, y = match.group(1), match.group(2)
                result = int(x) * int(y)
                total_sum += result
        elif match.group(0) == 'do()':
            multiplication_enabled = True
        elif match.group(0) == "don't()":
            multiplication_enabled = False
    
    return total_sum

file_path = 'input.txt'
data = read_input_file(file_path)
total_sum = get_multiplication_sum(data)
print(total_sum)
    