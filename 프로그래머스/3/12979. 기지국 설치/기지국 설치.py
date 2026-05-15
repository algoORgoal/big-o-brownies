from math import ceil

# 문제: station - w로 건설되는 건설 지점이 0보다 작을 수도 있다.
# 해결방법: station - w로 커버되는 시작지점의 최소값을 1로 지정한다.

# 문제: 본래 기지국 건설 지점이 1이었을 경우, 커버 가능한 지점은 2 * w가 아니라 w까지만 커버가 가능하다. 그런데 동일하게 2 * w까지 커버된다고 표시했다. 범위 문제
# 해결방법: 기지국 별로 유효한 범위 따로 저장한다.
# 예) station 위치가 2였고 w가 5 => 3 4 5 6 7 범위 덮을 수 있다.
def solution(n, stations, w):
    boundaries = [ (max(station - w, 1), min(station + w, n)) for station in stations ]
    
    total = 0
    
    
    for index, (start, end) in enumerate(boundaries):
        if index == 0:
            prev_end = 0
        else:
            prev_end = boundaries[index - 1][1]
            
        if prev_end + 1 <= start - 1:
            empty_area_count = (start - 1) - (prev_end + 1) + 1
            required_tower_count = ceil(empty_area_count / (2 * w + 1))
            total += required_tower_count
        
        if index == len(boundaries) - 1:
            if end + 1 <= n:
                empty_area_count = n - (end + 1) + 1
                required_tower_count = ceil(empty_area_count / (2 * w + 1))
                total += required_tower_count
                
    
    return total
                
            
                
    
    

# 아파트 개수 200_000_000
# len(stations) <= 10_000
# 모든 아파트를 돌아다니면서, 최소 개수 파악하기
# stations 개수 10_000번, 한번 연산할 때 (2 * w + 1) 요소 순회 => n * len(stations) 

# 기지국을 설치해서 모든 아파트에 전파가 전달될 수 있어야 할 때, 설치되는 기지국의 최소값
# 기지국 n개로 최대한 많은 아파트에 설치하는 방법
# 왼쪽에서 오른쪽으로 가면서 처음으로 설치가 안 된 기지국부터 (2 * w + 1)번 커버하기
# 시간복잡도 O(n)

# 해결방법 투포인터
# start에 전파 안 터진다 => count += 1
# start로 세우고 다시 2 * w + 1만큼 뻗어나감, 중간에 전파 터지는 시작점 발견시 거기를 start로 세움

# 1. distance = 2 * w + 1
# 2. station_starts = set([ station - w for station in stations ])

# 시간복잡도 O(n)
# 공간복잡도 O(len(stations))

# start = 1
# end = 1
# count += 1
# while start < n and end < n:
#   end = start
#   if start not in station_starts:
#     count += 1
#   while (end - start) <= 2 * w + 1:
#     end += 1
#     if end in station_starts:
#       break

# 문제점: station - w가 1보다 크거나 같아야 함

# 문제점: station 커버 시작 지점이 1이라도, station 커버 종료 지점은 1 + 2w가 아닐 수 있다. 기지국의 위치가 항상 w + 1에 있지 않을 것이기 때문이다.
# 해결방법: 시작점 별로 끝값을 별도로 처리하는 station_table을 구한다. 

# 문제점: n <= 200_000_000임에도 O(n) 시간 풀이가 통과하지 않는다.
# 해결방법: 각 station 사이에 얼마나 많은 빈공간이 있는지 확인한다.
# 빈공간의 개수 구하는 법?
# 1. station을 바탕으로 [start, end] 만들기
# index가 0인 경우 => [0, start - 1]가 연속된 빈 공간의 개수
# 아닐 경우 [prev.end+1, start - 1]가 연속된 빈 공간의 개수
# ceil((빈공간 개수) / (2 * w + 1))이 필요한 기지국의 개수
# 시간복잡도 O(len(stations))

