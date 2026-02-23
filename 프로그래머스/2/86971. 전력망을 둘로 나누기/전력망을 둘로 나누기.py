from math import inf

def solution(n, wires):
    graph = {}

    for vertex1, vertex2 in wires:
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []
            
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
        
    
    subtree_size_table = {}
    
    visited = set()

    dfs(graph, 1, subtree_size_table, visited)
    min_difference = inf
    total_node_count = subtree_size_table[1]
    
    for node in subtree_size_table:
        subtree_size = subtree_size_table[node]
        rest = total_node_count - subtree_size
        min_difference = min(min_difference, abs(subtree_size - rest))
        
    return min_difference

def dfs(graph, current, subtree_size_table, visited):    
    visited.add(current)
    
    
    children = graph[current]

    sum = 0
    for child in children:
        if child in visited:
            continue
        dfs(graph, child, subtree_size_table, visited)
        sum += subtree_size_table[child]
    subtree_size_table[current] = sum + 1
        

# 현재 노드 - 부모 사이의 edge를 제거했을 때
# 현재 노드를 포함하는 컴포넌트의 노드 개수
# = 자식 노드 - 현재 노드를 포함하는 컴포넌트의 노드 개수 합
# 현재 노드를 포함하지 않는 컴포넌트의 노드 개수 = 전체 노드 개수 - 현재 노드를 포함하는 컴포넌트의 노드 개수
# 
