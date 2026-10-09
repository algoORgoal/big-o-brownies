from math import inf
import heapq

def solution(n, s, a, b, fares):
    
    matrix = floyd_warshall(n, fares)
    
            
    min_cost = inf
            
    for middle_point in range(1, n + 1):
        min_cost = min(min_cost, matrix[s][middle_point] + matrix[middle_point][a] + matrix[middle_point][b])
            
    return min_cost
    

def construct_graph(n, edges):
    graph = { node: [] for node in range(1, n + 1) }
    for vertex1, vertex2, weight in edges:
        graph[vertex1].append((vertex2, weight))
        graph[vertex2].append((vertex1, weight))
        
    return graph


def floyd_warshall(n, edges):
    matrix = [ [ inf for j in range(n + 1) ] for i in range(n + 1) ]
    
    for vertex1, vertex2, weight in edges:
        matrix[vertex1][vertex2] = weight
        matrix[vertex2][vertex1] = weight
    
    for i in range(1, n + 1):
        matrix[i][i] = 0
        
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    
    return matrix


def dijkstra(start, destination1, destination2, n, graph):
    queue = []
    
    visited = [[ False for j in range(0, n + 1) ] for i in range(0, n + 1) ]
    heapq.heappush(queue, (0, start, start))
    
    while len(queue) > 0:
        cost, node1, node2 = heapq.heappop(queue)
        
        if node1 == destination1 and node2 == destination2:
            return cost
    
        visited[node1][node2] = True
        
        
        # node2 도착한 경우: node1만 이동
        if node2 == destination2:
            for adjacent_node1, weight1 in graph[node1]:
                if visited[adjacent_node1][node2] == True:
                    continue
                    
                next_cost = cost + weight1
                next_state = (next_cost, adjacent_node1, node2)
                
                heapq.heappush(queue, next_state)
            
            continue


        # node1 도착한 경우: node2만 이동
        if node1 == destination1:
            for adjacent_node2, weight2 in graph[node2]:
                if visited[node1][adjacent_node2] == True:
                    continue
                    
                next_cost = cost + weight2
                next_state = (next_cost, node1, adjacent_node2)
                
                heapq.heappush(queue, next_state)
                
            continue
        
        # node1와 node2 동시에 이동
        for adjacent_node1, weight1 in graph[node1]:
            for adjacent_node2, weight2 in graph[node2]:
                if visited[adjacent_node1][adjacent_node2] == True:
                    continue
                
                if node1 != node2 and adjacent_node1 == adjacent_node2:
                    continue
                    
                next_cost = 0
                
                if node1 == node2 and adjacent_node1 == adjacent_node2:
                    next_cost = cost + weight1
                else:
                    next_cost = cost + weight1 + weight2
                    
                next_state = (next_cost, adjacent_node1, adjacent_node2)
                heapq.heappush(queue, next_state)
        
                
    
    return inf
    
    
    # b는 가만히 있고 a만 이동
    
    # a와 b 동시에 이동
    

# 상태
# a, b의 위치(vertex)
# 거리
# 1. a는 가만히 있고 b만 이동
# 2. b는 가만히 있고 a만 이동
# 3. a랑 b 이동
#    (같은 위치이고 이동도 같이 하는 경우 => 이동 비용 그대로)

# 시간복잡도: m logn ()
    


# 합승 - 비합승일 때 sum of minimum cost 구하기
# (합승 구간의 길이는 0이어도 된다.)
# undirected weighted graph 

# 시간복잡도 (m ** 2 log (n ** 2)) (n ** 4 log(n ** 2))
# 1_600_000_000 => 16억 => 시간초과

# 1. floyd warshall's algorithm 실행하여, 모든 정점 사이의 최단거리 구하기 (n ** 3) (n ** 2 log n * n보다 빠름)
# 2. 합승 아예 안 하고 a, b로 가는 경우 / 합승 각 점에서 하고 a,b로 가는 경우 분류, 최소 비용 구하기
# 시간복잡도 O(n ** 3 + n)
# 공간복잡도 O(n ** 2) (n ** 2 <= 40_000)