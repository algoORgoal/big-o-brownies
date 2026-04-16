from sys import stdin
import heapq
from collections import deque


input = stdin.readline


def solution(n, m, edges, source, destination):
    graph = {}
    for start, end, weight in edges:
        if start not in graph:
            graph[start] = []

        graph[start].append((end, weight))

    cost, path = dijkstra(graph, source, destination)
    return [cost, len(path), list(path)]


def dijkstra(graph, source, destination):
    queue = []
    visited = {}

    heapq.heappush(queue, (0, source, source))

    while len(queue) > 0:
        cost, node, parent = heapq.heappop(queue)

        if node in visited:
            continue

        visited[node] = parent

        if node == destination:
            path = deque()
            path.appendleft(destination)

            current = destination
            while current != visited[current]:
                current = visited[current]
                path.appendleft(current)

            return cost, path

        if node not in graph:
            continue

        for adjacent_node, weight in graph[node]:
            heapq.heappush(queue, (cost + weight, adjacent_node, node))

    return graph


if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    source, destination = [int(string) for string in input().strip().split()]
    minimum_cost, city_count, path = solution(n, m, edges, source, destination)
    print(minimum_cost)
    print(city_count)
    print(*path)


# 완전탐색시 비용: n!
# edge weight이 다른 graph에서 최소비용 구하기 => 다익스트라 활용
# visited에 부모를 기록하기, 출발 노드는 자기 자신을 부모로 기록하기
# directed graph
# 항상 시작점에서 도착점 까지의 경로가 존재

# (비용, 노드, 부모 노드)

# 시간복잡도 O(mlogn) (n <= 1000, m <= 100_000)
# 공간복잡도 O(m + n) (graph)


