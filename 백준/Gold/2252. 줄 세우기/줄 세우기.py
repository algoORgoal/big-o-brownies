from sys import setrecursionlimit

setrecursionlimit(10 ** 5)


def solution(n, m, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for start, end in edges:
        graph[start].append(end)

    nodes = {i for i in range(1, n + 1)}
    visited = set()
    stack = []
    for node in nodes:
        topological_sort(node, graph, visited, stack)

    topo = stack[::-1]
    return topo


def topological_sort(current, graph, visited, stack):
    if current in visited:
        return

    visited.add(current)

    if current in graph:
        for adjacent_node in graph[current]:
            topological_sort(adjacent_node, graph, visited, stack)

    stack.append(current)


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    edges = [[int(string) for string in input().split()] for i in range(m)]
    answer = solution(n, m, edges)
    print(*answer)

# 두 노드간 왼쪽 / 오른쪽 관계가 정해짐
# 위상정렬 후 topological order 그대로 반환

# 시간복잡도 O(n + m)
# 공간복잡도 O(n + m)
