from math import ceil

def solution(distance, rocks, n):
    sorted_rocks = [ 0 ] + sorted(rocks) + [ distance ]
    
    start = 0
    end = 1_000_000_000
    while start < end:
        middle = ceil((start + end) / 2)
        
        target_distance = middle
        
        count = 0
        start_pointer = 0
        end_pointer = 1
        
        while end_pointer < len(sorted_rocks):
            distance = sorted_rocks[end_pointer] - sorted_rocks[start_pointer]
            if distance < target_distance:
                end_pointer += 1
                count += 1
            else:
                end_pointer += 1
                start_pointer = end_pointer - 1
        
        if count <= n:
            start = middle
        else:
            end = middle - 1
        
    return start
            
        
        
        
        
    

# 바위들 n개를 제거한 뒤 지점 사이의 거리의 최솟값 중에 가장 큰 값
# == 바위들 n개를 제거한 뒤 유지 가능한 거리 최댓값

# 바위 n개 제거 모든 경우의 수 => 50_000Cn
# 최댓값 => 50_000
# 시간복잡도 50_000Cn * 50_000 => 너무 큼

# 바위들 n개를 제거한 뒤 유지 가능한 거리 최댓값
# == 유지 거리 d (1 <= d <= 1_000_000_000) 중, 바위 n개 제거로 만들 수 있는 d 중 최대값
# 유지 거리 d에 필요한 바위 제거 횟수 n => 유지 거리 d + 1 에 필요한 바위 제거 횟수 n 이하
# 유지 거리 d를 바위 제거 횟수 n 이하로 만들 수 있음 => 탐색 범위 [d, 1_000_000_000]
# 유지 거리 d가 바위 제거 횟수 n 이하로 만들 수 없음 => 탐색 범위 [1, d - 1]

# distance: n, rocks: m
# 이진탐색 => O(logn)
# 최소 바위 제거 횟수 => O(m)

# O(log n * m) (n <= 1_000_000_000, m <= 50_000)
