from collections import deque
from math import inf


def solution(n, m, edge_table):
    graph = create_graph(edge_table, 1)
    backward_weights = {(start, end): edge_table[start, end] for start, end,
                        in edge_table if end == 1}

    roots = set()
    for parent in graph:
        roots.add(parent)

    for parent in graph:
        for child, weight in graph[parent]:
            roots.discard(child)

    topo = topological_sort(roots, graph)

    dp = {i: 0 for i in range(1, n + 1)}

    parent_table = {}

    for node in topo:
        if node in graph:
            for child, weight in graph[node]:
                if weight + dp[node] > dp[child]:
                    dp[child] = weight + dp[node]
                    parent_table[child] = node

    max_sum = -inf
    max_leaf = -1

    for start, source in backward_weights:
        dp[start] += backward_weights[start, source]
        if dp[start] > max_sum:
            max_sum = dp[start]
            max_leaf = start

    path = deque()
    current = max_leaf
    while current is not None:
        path.appendleft(current)
        current = parent_table.get(current)
    path.append(1)

    print(max_sum)
    print(*path)


def create_graph(edge_table, excluded_node):
    graph = {}
    for start, end in edge_table:
        weight = edge_table[start, end]
        if end == excluded_node:
            continue
        if start not in graph:
            graph[start] = []
        graph[start].append((end, weight))

    return graph


def topological_sort(roots, graph):
    queue = deque()
    in_degree = {}

    for parent in graph:
        for child, weight in graph[parent]:
            if child not in in_degree:
                in_degree[child] = 0
            in_degree[child] += 1

    for root in roots:
        queue.appendleft(root)

    topo = []

    while len(queue) > 0:
        node = queue.pop()

        topo.append(node)

        if node in graph:
            for child, weight in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.appendleft(child)

    return topo


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    edge_list = [[int(string) for string in input().split()] for i in range(m)]
    edge_table = {}
    for start, end, weight in edge_list:
        if (start, end) not in edge_table:
            edge_table[start, end] = weight
        else:
            edge_table[start, end] = max(edge_table[start, end], weight)

    solution(n, m, edge_table)


# 1을 제외한 상태에서는 cycle이 없음 => 2부터 n까지 directed acyclic graph
# 1에서 모든 노드 reachable => 2부터 n까지 모두 방문할 수 있음, 그러나 서로 모두 방문가능하다는 뜻은 아님
# dp를 통해 최장 weight 구하기
# dp = { node: 0 for node in nodes}
# for node in topo:
#   if node in graph:
#     for child in graph[node]:
#       dp[child] = max(dp[child], weights[child] + dp[node])
# 여러 경로가 존재할 수 있을까? 순서가 바뀐다는 것인데, 위상정렬시 [a, b, c]에서 a와 b, b와 c는 연결되어 있다. 순서가 바뀌는 순간 사이클 존재한다는 것 의미 => 불가능
# 위상정렬 각 edge 사이의 가중치 합 계산하기


# 1에서 모든 노드 reachable
# 1을 제외한 incoming edge가 없다 => 1하고 연결되어 있음
# 모든노드에서 1 reachable
# 1을 제외한 outgoing edge가 없다 => 1하고 연결되어 있음

# 반례: edge가 1 2, 2 1만 있는 경우 그래프가 생성되지 않음
# 해결 방법: 1부터 시작하도록 포함

# 반례: 동일한 start, end를 가진 edge weight가 존재할 수 있음
# 해결 방법: max값만 저장

# 반례: leaf가 아니더라도 1로 되돌아갈 수 있음
# 예를 들어, 문제에서 주어진 예시에 6 -> 1 추가되어도 문제가 없음
