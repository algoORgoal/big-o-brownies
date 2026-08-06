from collections import deque


def solution(n, computers):
    count = 0
    visited = set()
    for node in range(0, n):
        if node not in visited:
            dfs(node, computers, visited)
            count += 1
    return count
        
    
    
def dfs(node, matrix, visited):
    if node in visited:
        return
    
    visited.add(node)
    
    for adjacent_node, has_edge in enumerate(matrix[node]):
        if has_edge == 1:
            dfs(adjacent_node, matrix, visited)
    
    
    

    



# 그래프에서 connected component의 개수 세기
# disjoint set을 통해서 connected component끼리 같은 set에 있게 만들 수 있음
# 0부터 n-1까지, find() 연산을 통해 가져오는 root를 집합에 담음
# 집합에 담기는 개수
# 시간복잡도 O(n + m) = O(n + n ** 2) = O(n ** 2)
# 공간복잡도 O(n + m) = O(n + n ** 2) = O(n ** 2)

