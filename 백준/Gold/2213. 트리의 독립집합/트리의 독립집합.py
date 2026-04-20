from math import inf
from sys import setrecursionlimit

setrecursionlimit(10 ** 5)


def solution(n, weights, edges):
    graph = {}
    for vertex1, vertex2 in sorted(edges):
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []

        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    tree = {}
    root = 1
    create_tree(root, None, graph, tree)

    weights = [0] + weights

    result = dfs(1, tree, weights)

    if result[0] >= result[1]:
        print(result[0])
        print(*sorted(result[2]))
    else:
        print(result[1])
        print(*sorted(result[3]))


def create_tree(current, parent, graph, tree, visited=set()):
    if current in visited:
        return

    visited.add(current)

    if parent is not None:
        if parent not in tree:
            tree[parent] = []

        tree[parent].append(current)

    if current not in graph:
        return

    for adjacent_node in graph[current]:
        create_tree(adjacent_node, current, graph, tree, visited)


def dfs(current, tree, weights):
    # dp[0], nodes[0]: 현재 노드 포함
    # dp[1], nodes[1]: 현재 노드 비포함

    # dp[0] = dp[1] + weight
    # nodes[0] = nodes[1] + set([ current ])

    # dp[1] = max(dp[0], dp[1])
    # nodes[1] = nodes[0] if dp[0] >= dp[1] else nodes[1]

    # if current == root:
    #     dp[0] += weights[root]
    #     nodes[0].add(current)
    # else:
    #     dp[0], dp[1], nodes[0], nodes[1] = (dp[1] + weights[current],
    #                                         max(dp[0], dp[1]),
    #                                         nodes[1] | {current},
    #                                         nodes[0] if dp[0] >= dp[1] else nodes[1])

    result = [weights[current], 0, {current}, set()]
    if current not in tree:
        return result

    for child in tree[current]:
        child_result = dfs(child, tree, weights)
        result[0] += child_result[1]
        result[2] |= child_result[3]
        if child_result[0] >= child_result[1]:
            result[1] += child_result[0]
            result[3] |= child_result[2]
        else:
            result[1] += child_result[1]
            result[3] |= child_result[3]

    return result


if __name__ == "__main__":
    n = int(input())
    weights = [int(string) for string in input().split()]
    edges = [[int(string) for string in input().split()] for i in range(n - 1)]
    solution(n, weights, edges)


# 해당 정점을 포함하는 경우 + max(자식을 포함하지 않는 경우)
# 해당 정점을 포함하지 않는 경우 + max(자식을 포함하는 경우, 자식을 포함하지 않는 경우)

# dp[0]:


# tree로 일단 변환하기
# 트리 특징: 어느 노드를 루트로 잡아서 만들어도 상관 없음

# 시간복잡도: 탐색 O(n), 각 탐색마다 set 생성 최대 O(n) => O(n ** 2) (n <= 10_000, n ** 2 <= 100_000_000)
# 공간복잡도: O(n)


# 100_000_000
