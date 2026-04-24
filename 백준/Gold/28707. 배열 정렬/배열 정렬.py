

import heapq
from math import inf
from collections import deque
from sys import setrecursionlimit


def solution(n, nums, m, edges):
    graph = construct_graph(edges, n)
    return dijkstra(graph, nums)


def construct_graph(edges, n):
    graph = {node: [] for node in range(0, n)}
    for vertex1, vertex2, weight in edges:
        graph[vertex1 - 1].append((vertex2 - 1, weight))
        graph[vertex2 - 1].append((vertex1 - 1, weight))

    return graph


def dijkstra(graph, nums):
    n = len(graph.keys())

    pq = []
    visited = {}

    root_key = tuple(nums)
    for node in range(0, n):
        heapq.heappush(pq, (0, root_key))
        visited[root_key] = 0

    while len(pq) > 0:
        cost, key = heapq.heappop(pq)

        if visited[key] < cost:
            continue

        for node in range(n):
            for adjacent_node, weight in graph[node]:
                next_cost = cost + weight
                new_nums = list(key)
                new_nums[node], new_nums[adjacent_node] = new_nums[adjacent_node], new_nums[node]
                new_key = tuple(new_nums)

                if new_key in visited and visited[new_key] <= next_cost:
                    continue

                visited[new_key] = next_cost

                heapq.heappush(pq, (next_cost, new_key))

    sorted_key = tuple(sorted(nums))
    if sorted_key in visited:
        return visited[sorted_key]
    else:
        return inf


if __name__ == "__main__":
    n = int(input())
    nums = [int(string) for string in input().split()]

    m = int(input())
    edges = [[int(string) for string in input().split()]for i in range(m)]

    answer = solution(n, nums, m, edges)
    if answer == inf:
        print(-1)
    else:
        print(answer)

# 각각의 위치에서, 다른 위치로 옮길 때 cost 계산
# 각각 옮겨야 하는 위치는, 정렬 후 인덱스가 담겨있는 sorted_table을 통해 계산
# dikstra를 통해 위치를 옮길 때, 숫자의 위치도 서로 바꾼 것 반환하기
# cache: 현재 배치가 동일할 때, 나머지 요소들을 옮겨야 하는 코스트는 동일
# 배치 = n! , 다익스트라 = mlogm
# n! * mlogm
# 8! * 10log(10) = 1339401


# 1 2 3


# node * key
# 8 * 8! 800_000
# node * key가 각각 edge 10개 가지고 있음 8_000_000
# mlogm

# 반례: 현재 노드와 바로 연결되는 edge가 아니더라도 연결할 수 있음
