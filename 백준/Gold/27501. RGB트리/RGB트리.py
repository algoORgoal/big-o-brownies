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

    if max(*result) == result[0]:
        visit_colored_graph(1, 0, colored_tree, color_table)
        print(result[0])
        print(''.join([digit_to_color[color_table[node]] for node in nodes]))
    elif max(*result) == result[1]:
        visit_colored_graph(1, 1, colored_tree, color_table)
        print(result[1])
        print(''.join([digit_to_color[color_table[node]] for node in nodes]))
    else:
        visit_colored_graph(1, 2, colored_tree, color_table)
        print(result[2])
        print(''.join([digit_to_color[color_table[node]] for node in nodes]))


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


def dfs(current, tree, weights, colored_graph):
    result = weights[current][:]
    colored_graph[current] = [[], [], []]

    if current not in tree:
        return result

    if current in tree:
        for child in tree[current]:
            child_result = dfs(child, tree, weights, colored_graph)

            if child_result[1] > child_result[2]:
                result[0] += child_result[1]
                colored_graph[current][0].append((child, 1))
            else:
                result[0] += child_result[2]
                colored_graph[current][0].append((child, 2))

            if child_result[2] > child_result[0]:
                result[1] += child_result[2]
                colored_graph[current][1].append((child, 2))
            else:
                result[1] += child_result[0]
                colored_graph[current][1].append((child, 0))

            if child_result[0] > child_result[1]:
                result[2] += child_result[0]
                colored_graph[current][2].append((child, 0))
            else:
                result[2] += child_result[1]
                colored_graph[current][2].append((child, 1))

    return result


if __name__ == "__main__":
    n = int(input().strip())
    edges = [[int(string) for string in input().strip().split()]
             for i in range(n - 1)]
    weights = [0] + [[int(string) for string in input().strip().split()]
                     for i in range(n)]
    solution(n, edges, weights)


# 시간복잡도: O(n ** 2)
# 공간복잡도: O(n)
