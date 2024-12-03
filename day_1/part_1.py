def get_sorted_lists_from_file(file_path: str) -> tuple[list[int], list[int]]:
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
    return sorted(left_list), sorted(right_list)


def get_total_distance(left_list: list[int], right_list: list[int]) -> int:
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    return total_distance


file_path = "input.txt"
left_list, right_list = get_sorted_lists_from_file(file_path)
total_distance = get_total_distance(left_list, right_list)
print(total_distance)
