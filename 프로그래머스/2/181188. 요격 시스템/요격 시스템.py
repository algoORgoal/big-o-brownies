from functools import cmp_to_key

def compare(a, b):
    start1, end1 = a
    start2, end2 = b
    return end1 - end2

def solution(targets):
    last_shot_position = -1 # 이 좌표 바로 왼쪽에 요격
    shot_count = 0
    
    targets.sort(key=cmp_to_key(compare))
    for start, end in targets:
        if start < last_shot_position:
            continue
        else:
            shot_count += 1
            last_shot_position = end
    
    return shot_count
    
    


# [1, 4], [3, 8]