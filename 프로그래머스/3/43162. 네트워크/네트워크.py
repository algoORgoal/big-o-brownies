def solution(n, computers):
    visited = set()
    count = 0
    print(computers)
    for i in range(0, n):
        if i not in visited:
            visited.add(i)
            dfs(i, computers, visited)
            count += 1
    return count
    
def dfs(current, matrix, visited):
    for node, is_adjacent in enumerate(matrix[current]):
        if is_adjacent == 0:
            continue
        if node in visited:
            continue
        visited.add(node)
        dfs(node, matrix, visited)


# 그래프에서 connected component의 개수 세기
# disjoint set을 통해서 connected component끼리 같은 set에 있게 만들 수 있음
# 0부터 n-1까지, find() 연산을 통해 가져오는 root를 집합에 담음
# 집합에 담기는 개수
# 시간복잡도 O(n + m) = O(n + n ** 2) = O(n ** 2)
# 공간복잡도 O(n + m) = O(n + n ** 2) = O(n ** 2)

