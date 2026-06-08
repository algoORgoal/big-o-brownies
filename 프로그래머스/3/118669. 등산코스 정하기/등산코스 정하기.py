import heapq

def solution(n, paths, gates, summits):
    nodes = set([ node for node in range(1, n + 1) ])
    graph = construct_graph(paths, nodes)
    shortest_weight, shortest_summit = dijkstra(graph, summits, gates)
    return [ shortest_summit, shortest_weight ]
    
    


def construct_graph(edges, nodes):
    graph = { node: [] for node in nodes }
    
    for vertex1, vertex2, weight in edges:
        graph[vertex1].append((vertex2, weight))
        graph[vertex2].append((vertex1, weight))
        
    return graph

def dijkstra(graph, sources, destinations):
    queue = []
    visited = {}
    
    for source in sources:
        heapq.heappush(queue, (0, source, source))
        
    while len(queue) > 0:
        max_weight, source, node = heapq.heappop(queue)
        
        
        
        if node in visited:
            continue
            
        visited[node] = max_weight, source
        
        
        
        for adjacent_node, weight in graph[node]:
            next_weight = max(max_weight, weight)
            heapq.heappush(queue, (next_weight, source, adjacent_node))
            
    shortest_weight, shortest_source = sorted([ visited[destination] for destination in destinations])[0]
    
    return shortest_weight, shortest_source
    
    
    


# 출입구 - 쉼터 - 산봉우리 - 쉼터 - 출입구 경로 중 지나치는 최대 edge weight가 최소 몇까지는 될까?
# 산봉우리에서 출입구로 dijkstra's algorithm을 돌려 지나치는 최대 edge weight의 최소 값 찾기
# 양방향이므로 산봉우리 - 출입구 최소 edge weight가 출입구 - 산봉우리 edge weight가 도니다.
# (node, 최대 edge weight)

# queue = []
# heapify.push(queue, ())
# while len(queue) > 0:
#   
# for adjacent_node in graph[node]:
#   
# 시작 출입구와 끝 출입구는 동일해야 함

# 모든 선봉우리를 시작으로 넣고, dijkstra's algorithm 실행
# 기억해야될 상태: 현재 방문 노드, max weight, 시작 산봉우리
# 힙에다가 넣어야 하므로 max weight, 현재 방문 노드, 시작 산봉우리 순으로 넣기
# (intensity, 시작 산봉우리) tuple로 리스트에 넣고 정렬 후 첫번째 요소 반환
# 시간복잡도: nlog(n)

# ㄷ