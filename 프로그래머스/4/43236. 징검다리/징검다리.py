from math import ceil

def solution(distance, rocks, n):
    rocks.sort()
    
    in_between_distances = []
    for i, rock in enumerate(rocks):
        if i == 0: 
            in_between_distances.append(rock)
        else:
            in_between_distances.append(rocks[i] - rocks[i - 1])
    in_between_distances.append(distance - rocks[len(rocks) - 1])
    
    
    
    start = 0
    end = 1_000_000_000
        
    while start < end:
        middle = ceil((start + end) / 2)
        
        
        minimum_distance = middle
        current_distance = in_between_distances[0]
        destroy_count = 0

        for i, in_between_distance in enumerate(in_between_distances):
            if i == 0:
                continue
            elif current_distance < minimum_distance:
                destroy_count += 1
                current_distance += in_between_distance
            else:
                current_distance = in_between_distance
        if current_distance < minimum_distance:
            destroy_count += 1
                        
        # 거리 i 유지하려면 바위 n개 제거로 가능 => 거리 0 ~ (i - 1) 거리 유지하려면 바위 n개 제거로 가능
        # 거리 i 유지하려면 바위 n개 제거로 불가능 => 거리 (i + 1) ~ n 거리 유지하려면 바위 n개 제거로 불가능
        if destroy_count <= n:
            start = middle
        else:
            end = middle - 1
    return start
    

            
    
        
    
    
    answer = 0
    return answer


# 0 2 11 14 17 21 25
#  2 9  3 3  4  4

# 현재 값 2
# 9 들어올 때 2 <= d => destory => 2 + 9 = 11
# 11 들어올 때 11 >= d => replace => 현재값 9
# 14 들어올 때 9 >= d => replace => 현재값 3
# 17 들어올 때 3 < d => destroy => 3 + 3 = 6
# 21 들어올 때 4 >= d => replace => 현재값 4
# 25 들어올 때 4 >= d => replace => 현재값 4


# 질문: 특정 거리가 들어왔을 때, 왼쪽에서 destroy해야될까 아니면 오른쪽에서 destroy해야될까?

# 거리 d를 유지하기 위해 제거해야되는 요소들의 최소 개수를 어떻게 구하지?
# 가장 작은 것부터 순차적으로 배열 탐색하면서 제거: O(n ** 2) 2_500_000_000 => 시간초과

