from collections import deque

def solution(n, computers):
    visited = set()
    count = 0
    for i in range(0, n):
        if i not in visited:
            visited.add(i)
            bfs(computers, i, visited)
            count += 1

    return count

def bfs(matrix, root, visited):
    queue = deque([ root ])
    
    while len(queue) > 0:
        current = queue.popleft()
        for node, is_adjacent in enumerate(matrix[current]):
            if is_adjacent == 0:
                continue
            if node in visited:
                continue
            visited.add(node)
            queue.append(node)

    
    
    

    



# 그래프에서 connected component의 개수 세기
# disjoint set을 통해서 connected component끼리 같은 set에 있게 만들 수 있음
# 0부터 n-1까지, find() 연산을 통해 가져오는 root를 집합에 담음
# 집합에 담기는 개수
# 시간복잡도 O(n + m) = O(n + n ** 2) = O(n ** 2)
# 공간복잡도 O(n + m) = O(n + n ** 2) = O(n ** 2)

