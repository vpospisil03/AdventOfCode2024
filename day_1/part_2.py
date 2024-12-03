def get_lists_from_file(file_path: str) -> tuple[list[int], list[int]]:
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list


def get_similarity_score(left_list: list[int], right_list: list[int]) -> int:
    similarity_score = 0
    for left in left_list:
        count = right_list.count(left)
        similarity_score += left * count
    return similarity_score


file_path = "input.txt"
left_list, right_list = get_lists_from_file(file_path)
similarity_score = get_similarity_score(left_list, right_list)
print(similarity_score)
