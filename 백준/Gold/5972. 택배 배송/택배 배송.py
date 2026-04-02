import heapq
from sys import stdin

input = stdin.readline


def solution(n, m, edges):
    graph = {}
    for vertex1, vertex2, weight in edges:
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []
        graph[vertex1].append((vertex2, weight))
        graph[vertex2].append((vertex1, weight))
    return dijkstra(1, n, graph, set())


def dijkstra(start, end, graph, visited):
    queue = []
    heapq.heappush(queue, (0, start))

    while len(queue) > 0:
        distance, current = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            return distance

        if current not in graph:
            continue

        for adjacent_node, weight in graph[current]:
            heapq.heappush(queue, (distance + weight, adjacent_node))


if __name__ == "__main__":
    n, m = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    answer = solution(n, m, edges)
    print(answer)


# edge weight가 다르고, bidirectional
# 1부터 n까지 가기 위한 shortest path
# dijkstra's algorithm
# 시간복잡도 O(mlogn) (n <= 50_000) (m <= 50_000)
# 공간복잡도 O(n + m)

# queue, start, end, edges, visited
