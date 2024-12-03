import re

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def get_multiplication_sum(data):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, data)
    
    total_sum = 0
    for x, y in matches:
        result = int(x) * int(y)
        total_sum += result
    
    return total_sum

file_path = 'input.txt'
data = read_input_file(file_path)
total_sum = get_multiplication_sum(data)
print(total_sum)
    