import heapq
from math import inf


def solution(n, m, r, weights, edges):
    # construct an undirected graph
    # run dijkstra's algorihtm from each node to all nodes and return sum of node weights
    # return maximum sum of node weights

    node_weights = [0] + weights
    graph = construct_graph(edges, n)
    nodes = {node for node in range(1, n + 1)}

    max_sum = -inf

    for node in nodes:
        max_sum = max(max_sum, dijkstra(graph, node, m, node_weights))

    return max_sum


def construct_graph(edges, n):
    graph = {node: [] for node in range(1, n + 1)}
    for start, end, weight in edges:
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    return graph


def dijkstra(graph: dict[int, list[int]], source: int, max_distance: int, node_weights: list[int]):
    n = len(graph.keys())
    pq = []
    visited = {node: inf for node in range(1, n + 1)}
    heapq.heappush(pq, (0, source))
    visited[source] = 0

    weight_sum = 0

    while len(pq) > 0:
        distance, node = heapq.heappop(pq)

        if visited[node] < distance:
            continue

        if distance <= max_distance:
            weight_sum += node_weights[node]

        for adjacent_node, weight in graph[node]:
            next_distance = distance + weight

            if visited[adjacent_node] <= next_distance:
                continue

            visited[adjacent_node] = next_distance
            heapq.heappush(pq, (next_distance, adjacent_node))

    return weight_sum


if __name__ == "__main__":
    n, m, r = [int(string) for string in input().split()]
    weights = [int(string) for string in input().split()]
    edges = [[int(string) for string in input().split()] for i in range(r)]
    answer = solution(n, m, r, weights, edges)
    print(answer)


# 지역 => node
# 양방향 길 => undirected edge(edge with weights)
# undirected graph에서, 최단경로가 m 이하로 도달 가능한 노드의 weights의 합이 최대인 경우
# 각 노드별로 dijkstra's algorithm 실행하여 distance가 m 이하인 노드의 weights 합 구하기
# 시간복잡도: O(n * rlogr) (n <= 100, r <= 100)
# 공간복잡도: O(rlogr)


# 10 1 9
# 1 1 1 1 1 1 1 1 1 1
# 1 2 100
# 2 3 100
# 3 4 100
# 4 5 100
# 5 6 100
# 6 7 100
# 7 8 100
# 8 9 100
# 9 10 100
