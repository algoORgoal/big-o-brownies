import heapq
from math import inf
from sys import stdin

input = stdin.readline


def solution(n, m, x, edges):

    graph = {}
    for start, end, weight in edges:
        if start not in graph:
            graph[start] = []

        graph[start].append((end, weight))

    reversed_graph = {}
    for start, end, weight in edges:
        if end not in reversed_graph:
            reversed_graph[end] = []

        reversed_graph[end].append((start, weight))

    reversed_visited = {}
    # 각자 집에서 x으로 갈 때의 최단거리
    dijkstra(reversed_graph, reversed_visited, x)

    visited = {}
    # x에서 각자 집으로 갈 때의 최단거리
    dijkstra(graph, visited, x)

    max_distance = -inf
    for i in range(1, n + 1):
        distance_from_home_to_n = reversed_visited[i] if i in reversed_visited else inf
        distance_from_n_to_home = visited[i] if i in visited else inf
        max_distance = max(
            max_distance, distance_from_home_to_n + distance_from_n_to_home)

    return max_distance


def dijkstra(graph, visited, root):
    queue = []
    heapq.heappush(queue, (0, root))

    while len(queue) > 0:
        distance, node = heapq.heappop(queue)

        if node in visited:
            continue

        visited[node] = distance

        if node not in graph:
            continue

        for adjacent_node, weight in graph[node]:
            if adjacent_node in visited:
                continue

            heapq.heappush(queue, (distance + weight, adjacent_node))


if __name__ == "__main__":
    n, m, x = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    answer = solution(n, m, x, edges)
    print(answer)


# 1 <= N <= 1000 (the number of vertices)
# 1 <= X <= N (destination)
# 1 <= M <= 100_000 (the number of edges)

# different edge weight => dijkstra's algorithm (mlogn)
# shortest path from each vertex to x
# shortest path from x to each vertex

# graph, visited, root, heapq (edge weight, node)

# 각자 x으로 갈 때의 최단거리: edge를 거꾸로 만들고, x에서 각자 집으로 갈 때의 최단거리
# 각자 집으로 갈 때의 최단거리: edge를 정상으로 만들고, x에서 각자 집으로 갈 때의 최단거리

# 시간복잡도: O(mlog(n))
# 공간복잡도: O(2mlog(n))
