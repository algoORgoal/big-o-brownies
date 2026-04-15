from sys import stdin
import heapq
from math import inf

input = stdin.readline


def solution(n, m, edges, source, destination):
    graph = {}
    for start, end, weight in edges:
        if start not in graph:
            graph[start] = []

        graph[start].append((end, weight))

    return dijkstra(graph, source, destination)


def dijkstra(graph, source, destination):
    queue = []
    visited = set()

    heapq.heappush(queue, (0, source))

    while len(queue) > 0:
        distance, node = heapq.heappop(queue)

        if node in visited:
            continue

        if node == destination:
            return distance

        visited.add(node)

        if node not in graph:
            continue

        for adjacent_node, weight in graph[node]:
            heapq.heappush(queue, (distance + weight, adjacent_node))

    return inf


if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    source, destination = [int(string) for string in input().strip().split()]
    answer = solution(n, m, edges, source, destination)
    print(answer)


# 최소 비용
# edge weight가 서로 다름

# 완전탐색시 O(n!) 또는 O(n * 2 ** n)(현재 상태 / 경로) 복잡도 => 시간초과
# 다익스트라 알고리즘 활용
# 단방향 그래프

# (거리, 현재 노드)
