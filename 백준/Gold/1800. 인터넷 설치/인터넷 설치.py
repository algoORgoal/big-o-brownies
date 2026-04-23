import heapq
from math import inf


def solution(n, p, k, edges):
    graph = construct_graph(edges, n)
    result = binary_search(0, 1_000_001, graph, k)
    return -1 if result == 1_000_001 else result


def construct_graph(edges, n):
    graph = {i: [] for i in range(1, n + 1)}
    for start, end, weight in edges:
        graph[start].append((end, weight))
        graph[end].append((start, weight))
    return graph


def binary_search(start, end, graph, k):
    if start == end:
        return start

    mid = (start + end) // 2

    n = len(graph.keys())

    # max_weight이 mid일 때, 경로 중에 넘치는 weight k개로 커버 가능하다
    if dijkstra(graph, 1, n, mid) <= k:
        return binary_search(start, mid, graph, k)  # [start, mid]
    else:
        return binary_search(mid + 1, end, graph, k)  # (mid, end]


def dijkstra(graph, source, destination, max_weight):
    node_count = len(graph.keys())
    pq = []
    visited = {node: inf for node in range(1, node_count + 1)}
    heapq.heappush(pq, (0, source))
    visited[source] = 0

    while len(pq) > 0:
        weight_count, node = heapq.heappop(pq)

        if visited[node] < weight_count:
            continue

        for adjacent_node, weight in graph[node]:
            if weight > max_weight:
                next_weight_count = weight_count + 1
            else:
                next_weight_count = weight_count

            if visited[adjacent_node] <= next_weight_count:
                continue

            visited[adjacent_node] = next_weight_count
            heapq.heappush(pq, (next_weight_count, adjacent_node))

    return visited[destination]


if __name__ == "__main__":
    n, p, k = [int(string) for string in input().split()]
    edges = [[int(string) for string in input().split()] for i in range(p)]
    answer = solution(n, p, k, edges)
    print(answer)


# 2648449.5042244755
# nlogn * log(l)
# 10_000 * log(10_000) * log(1_000_000) = 2_648_449

# path에서 longest edge weight k개 제외하고서  1_000_000 이하가 가능한가?
# path에서 longest edge weight k개를 제외하고서 500_000 이하가 가능한가?
# => path에서, edge weight이 500_000을 초과하는 것이 k개가 넘는가?
# edge weight이 500_000을 초과하는 것의 개수 => cost
# cost가 가장 작은 path 찾기 => dijkstra's algorithm
# 상태: (edge weight이 target을 초과하는 것의 개수, node)

# longest edge weight k개 제외하고서 500_000 이하 가능 => longest edge weight k개 제외하고서 1_000_000 이하 가능
# 이진탐색 돌릴 수 있음
# 시간복잡도: nlogn * log(l)

# 반례: 비용을 아예 안 내도 되는 경우도 존재 가능.
#      허용되는 max_weight가 0일 때 k개로 전부 다 면제되는 경우

# 3 2 100
# 1 2 1
# 2 3 2

# 반례: n까지 도달하는게 불가능한 경우 존재 가능 (n까지 비용이 항상 inf)
#      1_000_001로 설정하고, 1_000_001인 경우 -1 반환


# 4 2 1
# 1 2 10
# 2 3 20
