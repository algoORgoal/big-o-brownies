import heapq
from math import inf

def solution(alp, cop, problems):
    max_alp = -inf
    max_cop = -inf
    for required_alp, required_cop, added_alp, added_cop, weight in problems:
        max_alp = max(max_alp, required_alp)
        max_cop = max(max_cop, required_cop)
    
    return dijkstra(alp, cop, max_alp, max_cop, problems)

def dijkstra(initial_alp, initial_cop, max_alp, max_cop, problems):
    queue = []
    
    heapq.heappush(queue, (0, initial_alp, initial_cop))    
    visited = {}
    
    while len(queue) > 0:
        cost, alp, cop = heapq.heappop(queue)
        
        if (alp, cop) in visited:
            continue
            
        visited[alp, cop] = cost
        
        if max_alp <= alp and max_cop <= cop:
            return cost
            
        for required_alp, required_cop, added_alp, added_cop, weight in problems:
            if required_alp <= alp and required_cop <= cop:
                next_alp = min(max_alp, alp + added_alp)
                next_cop = min(max_cop, cop + added_cop)
                next_cost = cost + weight
                
                heapq.heappush(queue, (next_cost, next_alp, next_cop))
        
        
        heapq.heappush(queue, (cost + 1, min(max_alp, alp + 1), cop))
        heapq.heappush(queue, (cost + 1, alp, min(max_cop, cop + 1)))            
        
    

# 주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간 구하기

# 1. 알고력 1, 코딩력 1 높이기 (1 cost)
# 2. 현재 풀 수 있는 문제 중 하나 풀어 알고력, 코딩력 높이기


# 가능한 상태: 알고력 < 180, 코딩력 < 180, 180 * 180
# 문제를 풀 때마다 cost가 정해져 있음
# 각 (알고력, 코딩력) 상태 중 가장 최단거리 구하기
# 상태 개수: 180 * 180
# edge 개수: <= 180 * 180
# mlogn => 가능