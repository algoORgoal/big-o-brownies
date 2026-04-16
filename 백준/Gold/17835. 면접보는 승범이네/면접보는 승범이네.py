from sys import stdin
import heapq
from math import inf

input = stdin.readline


def solution(n, m, k, edges, destinations):
    graph = {}
    for start, end, weight in edges:
        if end not in graph:
            graph[end] = []

        graph[end].append((start, weight))

    max_distance, farthest_nodes = dijkstra(graph, destinations)
    return sorted(farthest_nodes)[0], max_distance


def dijkstra(graph, sources):
    queue = []
    visited = set()
    for source in sources:
        heapq.heappush(queue, (0, source))

    farthest_nodes = []
    max_distance = -inf

    while len(queue) > 0:
        distance, node = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        if max_distance == distance:
            farthest_nodes.append(node)
        elif max_distance < distance:
            max_distance = distance
            farthest_nodes = [node]

        if node not in graph:
            continue

        for adjacent_node, weight in graph[node]:
            heapq.heappush(queue, (distance + weight, adjacent_node))

    return max_distance, farthest_nodes


if __name__ == "__main__":
    n, m, k = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    destinations = [int(string) for string in input().strip().split()]
    answer = solution(n, m, k, edges, destinations)
    for num in answer:
        print(num)


# directed graph, 두 노드 사이에 edge 여러개 존재할 수 있음
# 목적지: destinations로 여러곳이 존재할 수 있음

#
# if node in destinations: return distance

# edge 방향 뒤집고, 면접장에서 다른 노드로 가는 최단거리 구하기
# 문제점: k * mlogn 인데 1 <= k <= n이다.
# 거리가 0인 노드가 여러개이다.
# 따라서 queue에 거리가 0인 루트 노드를 여러개 집어넣는다.
# 가장 거리가 먼 노드의 리스트 및 거리 기록하기
# 거리 반환하기


# 시간복잡도: O(m logn)
# 공간복잡도: O(m + n)


