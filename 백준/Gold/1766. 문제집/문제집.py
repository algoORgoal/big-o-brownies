from sys import stdin
from sys import setrecursionlimit
from collections import deque
import heapq

setrecursionlimit(100_000)

input = stdin.readline


def solution(n, m, edges):
    nodes = {i for i in range(1, n + 1)}
    graph = {node: [] for node in nodes}

    for start, end in edges:
        graph[start].append(end)

    visited = set()

    queues = []

    roots = set()
    for parent in graph:
        roots.add(parent)

    for parent in graph:
        for child in graph[parent]:
            roots.discard(child)

    topo = topological_sort_iterative(roots, graph)

    return topo


def topological_sort(current, graph, visited, stack):
    if current in visited:
        return

    visited.add(current)

    if current in graph:
        for adjacent_node in graph[current]:
            topological_sort(adjacent_node, graph, visited, stack)

    stack.append(current)


def topological_sort_iterative(roots, graph):
    queue = []

    in_degree = {}
    for parent in graph:
        for child in graph[parent]:
            if child not in in_degree:
                in_degree[child] = 0
            in_degree[child] += 1

    for root in roots:
        heapq.heappush(queue, root)

    topo = []

    while len(queue) > 0:
        node = heapq.heappop(queue)
        topo.append(node)

        if node in graph:
            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    heapq.heappush(queue, child)

    return topo


if __name__ == "__main__":
    n, m = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    answer = solution(n, m, edges)
    print(*answer)


# topological order를 통해, 왼쪽 - 오른쪽 관계 정렬 가능
# topological sort하기
# 끝에 있는 것부터 탐색, 이웃 노드 탐색시 숫자가 높은 것부터 담기

# 시간복잡도: O(n + m + nlogn)
# 공간복잡도: O(n + m)


# 8 4
# 5 3
# 3 2
# 8 4
# 4 2
