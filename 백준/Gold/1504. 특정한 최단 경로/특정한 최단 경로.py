from sys import stdin
from math import inf
from itertools import permutations
import heapq

input = stdin.readline


def solution(n, e, edges, bypass_nodes):
    graph = {}
    for vertex1, vertex2, weight in edges:
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []

        graph[vertex1].append((vertex2, weight))
        graph[vertex2].append((vertex1, weight))

    min_distance = inf

    for permutation in permutations(bypass_nodes):
        nodes = [1] + list(permutation) + [n]
        distance = 0

        for index in range(1, len(nodes)):
            distance += dijkstra(nodes[index - 1], nodes[index], graph)

        min_distance = min(min_distance, distance)

    return min_distance


def dijkstra(source, destination, graph):
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
    n, e = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(e)]
    bypass_nodes = [int(string) for string in input().strip().split()]
    answer = solution(n, e, edges, bypass_nodes)
    if answer == inf:
        print(-1)
    else:
        print(answer)


# 두가지 경우가 있음
# 1 => vertex1 => vertex2 => n
# 1 => vertex2 => vetex1 => n

# 1. 지나야하는 노드의 permutation을 만들기
# 2. 구간별로 dijkstra를 실행하기 (1, vertex1, vertex2, n), (1, vertex2, vertex1, n)
# 3. 작은 것 반환하기

# 시간복잡도 : 6 * mlog(n) (n <= 800, m <= 200_000)
# 공간복잡도: O(m + n)

# dijkstra 상태: (distance, node)
