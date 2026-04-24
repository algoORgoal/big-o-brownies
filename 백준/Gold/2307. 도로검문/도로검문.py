from sys import stdin
from math import inf
import heapq
from collections import deque

input = stdin.readline


def solution(n, m, edges):
    graph = construct_graph(edges, n)
    min_cost, path = dijkstra(graph, 1, n, None, output_path=True)

    if min_cost == inf:
        return 0

    max_cost = -inf
    for i in range(len(path) - 1):
        start, end = path[i], path[i + 1]
        cost = dijkstra(graph, 1, n, (start, end))
        max_cost = max(max_cost, cost)

    diff = max_cost - min_cost

    if diff == inf:
        return -1

    return diff


def construct_graph(edges, n):
    graph = {node: [] for node in range(1, n + 1)}
    for start, end, weight in edges:
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    return graph


def dijkstra(graph, source, destination, excluded_edge, output_path=False):
    n = len(graph.keys())
    pq = []
    visited = {node: inf for node in range(1, n + 1)}
    parent_table = {}

    heapq.heappush(pq, (0, source, None))
    visited[source] = 0

    while len(pq) > 0:
        cost, node, parent = heapq.heappop(pq)

        if visited[node] < cost:
            continue

        if output_path == True and parent is not None:
            parent_table[node] = parent

        for adjacent_node, weight in graph[node]:
            if (node, adjacent_node) == excluded_edge:
                continue

            next_cost = cost + weight
            if visited[adjacent_node] <= next_cost:
                continue

            visited[adjacent_node] = next_cost

            heapq.heappush(pq, (next_cost, adjacent_node, node))

    if output_path == True:
        path = deque()
        current = destination
        while current is not None:
            path.appendleft(current)
            current = parent_table.get(current)

        return visited[destination], path

    return visited[destination]


if __name__ == "__main__":
    n, m = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    answer = solution(n, m, edges)
    print(answer)


# 양방향 => undirected graph
# edge weight 있음
# 1부터 n까지 도착하는 최소시간 구하기
# 다익스트라 사용하여 최단거리 및 경로를 구할 수 있음

# 최단경로 안에 있는 edge를 하나씩 제거해보기
# 각각의 edge 제거했을 때 최단거리 dijkstra's algorithm 돌려서 확인하기
# diff = max(edge 제거한 최단거리 집합) - (edge 제거 안 했을 때 최단거리)
# diff = inf => -1 반환
# inf - inf => 0 반환(지연효과가 없음)

# 시간복잡도 O(mlogm * n) (m <= 5_000, n <= 1_000)
# 61_438_561
# 시도해볼만한 가치 있음


# 5 4
# 1 2 1
# 2 5 1
# 1 3 1
# 3 5 1

# 5 4
# 1 2 1
# 2 3 1
# 3 4 1
# 4 5 1

# 5 4
# 1 2 1
# 2 5 1
# 1 3 100
# 3 5 200

# 5 3
# 1 2 1
# 2 3 1
# 3 4 1
