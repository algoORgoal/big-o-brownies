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

    colored_tree = {}
    result = dfs(1, tree, weights, colored_tree)

    color_table = {}
    digit_to_color = {
        0: 'R',
        1: 'G',
        2: 'B',
    }

    for color, count in enumerate(result):
        if count == max(*result):
            visit_colored_graph(1, color, colored_tree, color_table)
            print(count)
            print(''.join([digit_to_color[color_table[node]]
                  for node in sorted(nodes)]))
            break


def visit_colored_graph(current, color, colored_tree, color_table):
    if current not in colored_tree:
        return

    color_table[current] = color

    for child, child_color in colored_tree[current][color]:
        visit_colored_graph(child, child_color, colored_tree, color_table)


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


def dfs(current, tree, weights, colored_tree):
    sums = weights[current][:]
    colored_tree[current] = [[], [], []]

    if current not in tree:
        return sums

    for child in tree[current]:
        child_result = dfs(child, tree, weights, colored_tree)

        colors = set([0, 1, 2])

        for color in colors:
            different_color1, different_color2 = list(colors - {color})
            if child_result[different_color1] >= child_result[different_color2]:
                sums[color] += child_result[different_color1]
                colored_tree[current][color].append((child, different_color1))
            else:
                sums[color] += child_result[different_color2]
                colored_tree[current][color].append((child, different_color2))

    return sums


if __name__ == "__main__":
    n = int(input().strip())
    edges = [[int(string) for string in input().strip().split()]
             for i in range(n - 1)]
    weights = [0] + [[int(string) for string in input().strip().split()]
                     for i in range(n)]
    solution(n, edges, weights)


# 시간복잡도: O(n)
# 공간복잡도: O(n)
