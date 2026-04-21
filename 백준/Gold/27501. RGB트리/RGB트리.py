from sys import setrecursionlimit
from sys import stdin

setrecursionlimit(500_000)

input = stdin.readline


def solution(n, edges, weights):
    nodes = {i for i in range(1, n + 1)}
    graph = {node: [] for node in nodes}
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)

    tree = {}
    create_tree(None, 1, graph, tree, set())

    dp = {}
    dfs(1, tree, weights, dp)

    digit_to_color = {
        0: 'R',
        1: 'G',
        2: 'B',
    }

    answer = {}
    reconstruct(1, -1, tree, dp, answer)

    print(max(*dp[1]))
    print(''.join([digit_to_color[answer[node]]
                  for node in sorted(nodes)]))


def reconstruct(current, parent_color, tree, dp, answer):
    if parent_color == -1:
        color = max(range(3), key=lambda c: dp[current][c])
    else:
        candidates = [c for c in range(3) if c != parent_color]
        if dp[current][candidates[0]] >= dp[current][candidates[1]]:
            color = candidates[0]
        else:
            color = candidates[1]

    answer[current] = color

    if current in tree:
        for child in tree[current]:
            reconstruct(child, color, tree, dp, answer)


def create_tree(parent, current, graph, tree, visited):
    if current in visited:
        return

    visited.add(current)

    if parent is not None:
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(current)

    if current in graph:
        for adjacent_node in graph[current]:
            create_tree(current, adjacent_node, graph, tree, visited)


def dfs(current, tree, weights, dp):
    dp[current] = weights[current][:]

    if current not in tree:
        return

    for child in tree[current]:
        dfs(child, tree, weights, dp)

        colors = set([0, 1, 2])

        for color in colors:
            different_color1, different_color2 = list(colors - {color})
            if dp[child][different_color1] >= dp[child][different_color2]:
                dp[current][color] += dp[child][different_color1]
            else:
                dp[current][color] += dp[child][different_color2]


if __name__ == "__main__":
    n = int(input().strip())
    edges = [[int(string) for string in input().strip().split()]
             for i in range(n - 1)]
    weights = [0] + [[int(string) for string in input().strip().split()]
                     for i in range(n)]
    solution(n, edges, weights)


# 시간복잡도: O(n)
# 공간복잡도: O(n)
