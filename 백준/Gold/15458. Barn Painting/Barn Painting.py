from sys import setrecursionlimit
from sys import stdin

setrecursionlimit(10 ** 5 + 1)

input = stdin.readline


def solution(n, k, edges, colors):
    graph = {}
    for vertex1, vertex2 in edges:
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []

        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    root = 1
    tree = {}
    create_tree(root, None, graph, tree)

    color_table = {vertex: color - 1 for vertex, color in colors}

    return sum(dfs(root, tree, color_table)) % (10 ** 9 + 7)


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


def dfs(current, tree, color_table):
    result = [1, 1, 1]
    if current in color_table:
        for index in {0, 1, 2} - {color_table[current]}:
            result[index] = 0

    if current not in tree:
        return result

    child_results = [dfs(child, tree, color_table) for child in tree[current]]

    count0 = 1
    count1 = 1
    count2 = 1
    for child_result in child_results:
        count0 *= (child_result[0] + child_result[1])
        count1 *= (child_result[1] + child_result[2])
        count2 *= (child_result[2] + child_result[0])

        count0 %= (10 ** 9 + 7)
        count1 %= (10 ** 9 + 7)
        count2 %= (10 ** 9 + 7)

    if result[0] > 0:
        result[0] = count1
    if result[1] > 0:
        result[1] = count2
    if result[2] > 0:
        result[2] = count0

    return result


if __name__ == "__main__":
    n, k = [int(string) for string in input().strip().split()]
    edges = [[int(string) for string in input().strip().split()]
             for i in range(n - 1)]
    colors = [[int(string) for string in input().strip().split()]
              for i in range(k)]
    answer = solution(n, k, edges, colors)
    print(answer)

# undirected acyclic connected graph -> tree로 볼 수 있음
# 1. graph를 tree로 변환하기
# 2. 트리를 순회하면서 subtree의 (a, b, c)를 계산하기
# a: 현재 빨간색을 칠했을 때 경우의 수(자식은 무조건 노랑 or 파랑을 칠해야 함)
# b: '' 파란색 ''
# c: '' 노란색 ''

# 자식이 (a1, b1, c1), (a2, b2, c2), ...일 때 계산법
# c = (a1 + b1)(a2 + b2) + ...
# a = (b1 + c1)(b2 + c2) + ...
# b = (c1 + a1)(c2 + a2) + ...
# 색상이 이미 정해진 경우, 나머지 색상 경우의 수는 0으로 할당하기(해당 색상이 될 수 없음)

# 시간복잡도: O(n)
# 공간복잡도: O(n)
