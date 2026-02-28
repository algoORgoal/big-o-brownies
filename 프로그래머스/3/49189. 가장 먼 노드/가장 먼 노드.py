from collections import deque 

def solution(n, edges):
    graph = {}
    for vertex1, vertex2 in edges:
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
        
            
    visited_table = {}
    bfs(graph, 1, visited_table)
    
    max_distance = max(*[ visited_table[vertex] for vertex in visited_table ])
    
    count = 0
    for vertex in visited_table:
        if visited_table[vertex] == max_distance:
            count += 1
    return count

def bfs(graph, root, visited_table):
    visited_table[root] = 0
    queue = deque([ (root, 0) ])
    
    
    while len(queue) > 0:
        current, distance = queue.pop()
        
        for adjacent_node in graph[current]:
            if adjacent_node in visited_table:
                continue
            visited_table[adjacent_node] = distance + 1
            queue.appendleft((adjacent_node, distance + 1))


# 최단 경로 -> bfs를 통해 탐색 가능
# 각 노드의 거리를 모두 기억해야하므로 visited_table 유지