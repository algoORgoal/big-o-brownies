from collections import deque

def solution(n, path, order):
    graph = construct_graph(n, path)
    precedence = get_precedence(order)
    return bfs(graph, 0, precedence, n)
    
    

def construct_graph(n, path):
    graph = { node: []  for node in range(0, n) }
    for [ vertex1, vertex2 ] in path:
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
    return graph

def get_precedence(order):
    precedence = {}
    for previous, later in order:
        precedence[later] = previous
    
    return precedence
    

def bfs(graph, source, precedence, n):
    queue = deque()
    queue.appendleft(source)
    
    to_be_visited = {}
    
    visited = set()
    
    while len(queue) > 0:
        node = queue.pop()
        
        if node in visited:
            continue
        
        # 우선 방문되야할 노드가 아직 방문되지 않은 경우
        if node in precedence and precedence[node] not in visited:
            to_be_visited[precedence[node]] = node
            continue
        
        # 해당 노드가 어떤 노드에게 우선 방문되어야 했을 노드인 경우
        if node in to_be_visited:
            queue.appendleft(to_be_visited[node])
            to_be_visited.pop(node)
            
        visited.add(node)
        
        for adjacent_node in graph[node]:
            queue.appendleft(adjacent_node)
    
    return len(visited) == n
        
        

# 루트 0, 양방향, 사이클 없음 => 트리
# 경로에 포함되어야 하는 edge (x, y)에서 x가 서로 다르고, y가 서로 다름 + (x, y) (y, z) 와 같이 연속 방문은 존재하지 않음
# 경로: 한 노드 여러번 지나칠 수 있음

# 2 <= n <= 200_000


# BFS를 진행할 경우,
# 세가지 경우로 나뉨.
# 1. 선행 노드를 아직 방문하지 않음
# 2. 선행 노드가 없음
# 3. 선행 노드를 방문함

# 2, 3의 경우 해당 노드를 방문할 수 있다는 뜻이다.
# 1의 경우 기록을 해두었다가, 선행 노드가 방문되었을 때 재탐색을 시작한다.
# 모든 노드를 탐색이 가능한지 확인한다.

# 1. graph 만들기
# 2. bfs 탐색하기 O(n)
# 3. 모든 노드가 전부 방문되었는지 확인하기




