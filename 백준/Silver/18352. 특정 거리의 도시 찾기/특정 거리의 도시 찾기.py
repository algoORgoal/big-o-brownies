from sys import stdin
from sys import stdout
from collections import deque

input = stdin.readline


def print(string, end="\n"):
    stdout.write(f"{string}{end}")


def solution(n, m, k, x, edges):
    graph = construct_graph(edges, n)
    nodes = bfs(x, graph, k)
    if len(nodes) == 0:
        return - 1
    return nodes


def construct_graph(edges, n):
    graph = {node: [] for node in range(1, n + 1)}
    for start, end in edges:
        graph[start].append(end)

    return graph


def bfs(source, graph, target_distance):
    queue = deque()
    visited = set()

    queue.appendleft((0, source))

    target_nodes = []

    while len(queue) > 0:
        distance, node = queue.pop()

        if node in visited:
            continue

        visited.add(node)
        if distance == target_distance:
            target_nodes.append(node)

        for adjacent_node in graph[node]:
            queue.appendleft((distance + 1, adjacent_node))

    return sorted(target_nodes)


if __name__ == "__main__":
    n, m, k, x = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(m)]
    answer = solution(n, m, k, x, edges)
    if answer == -1:
        print(answer)
    else:
        for num in answer:
            print(num)


# 단방향 도로 => directed graph 만들기
# edge weight가 전부 1이면서, 최단거리 k인 곳 찾기 => bfs 활용

# 시간복잡도 O(n + m)
# 공간복잡도 O(n + m)
