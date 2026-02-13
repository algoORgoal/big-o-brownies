def solution(array, commands):
    adjusted_commands = [ [ index - 1 for index in command ] for command in commands ]
    
    result = []
    for start, end, target_index in adjusted_commands:
        sliced_sorted_array = sorted(array[start:end + 1])
        result.append(sliced_sorted_array[target_index])
    return result


# 각 커맨드에 대해서 정렬 수행하고, i - 1번째 인덱스 반환
# len(commands) * len(array) * log(len(array))