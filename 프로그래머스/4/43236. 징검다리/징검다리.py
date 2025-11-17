# 바위 위치를 오름차순으로 정렬
# prev의 초기값: 0
# i보다 작으면서, 제거되지 않은 바위의 위치 prev
# i - prev < distance => i 제거 => 제거된 바위의 개수 1 증가
# i - prev >= distance => prev = i

# 제거해야하는 바위의 최소 개수가 n개 이하인 것 중 가장 distance가 가장 큰 것을 찾는다.

# k 거리를 확보하기 위해 제거해야하는 바위의 최소 개수 <= k + 1 거리를 확보하기 위해 제거해야하는 바위의 최소 개수
# 거리 k에 대해서 이진 탐색을 시도해본다. 
# 제거해야하는 바위 개수가 n 이하 => 다음 이진탐색의 range는 (mid, end) => 이 속에 만족하는 정답 항상 있음
# 제거해야하는 바위의 개수가 n 초과 => 다음 이진탐색의 range는 (start, mid - 1) => 이 속에 만족하는 정답 항상 있음

# 도착 지점을 넣어서 바위 - 도착 지점 사이 거리도 만족하는지 확인
# 0 - 도착 지점 확인 => 어차피 모든 바위 제거하였음, count + 1 = num(rocks) + 1 되면 정답이 아님 (1 <= n <= num(rocks))
# 바위 - 도착 지점 확인 => 바위를 제거 => 이전 바위 - 바위 거리는 target_distance 이상이였을 것이므로 만족함

from math import ceil

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start = 0
    end = distance
    while start < end:
        mid = ceil((start + end) / 2)
        count = count_minimum_rocks_to_remove(mid, rocks)
        if count <= n:
            start = mid
        else:
            end = mid - 1
    return start
    
        
    

# n 거리를 확보하기 위해 제거해야하는 바위의 최소 개수
# the minimum number of rocks so that they are n-distant
def count_minimum_rocks_to_remove(target_distance, rocks):
    prev = 0
    count = 0
    for rock in rocks:
        if rock - prev < target_distance:
            count += 1
        else:
            prev = rock
    return count