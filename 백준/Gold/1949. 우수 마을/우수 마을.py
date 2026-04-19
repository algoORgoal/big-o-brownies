from math import inf
from sys import setrecursionlimit

setrecursionlimit(10 ** 5)


def solution(n, populations, edges):
    populations = [0] + populations

    graph = {}
    for vertex1, vertex2 in edges:
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []

        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    visited = set()

    max_result = -inf

    for i in range(1, n + 1):
        if i in visited:
            continue
        visited.add(i)
        result = dfs(i, graph, populations, visited)

        max_result = max(max_result, result[1], result[2])

    return max_result


def dfs(current, graph, populations, visited):
    result = [0, 0, populations[current]]

    if current not in graph:
        return result

    child_results = []

    for adjacent_node in graph[current]:
        if adjacent_node in visited:
            continue

        visited.add(adjacent_node)

        child_result = dfs(adjacent_node, graph, populations, visited)
        child_results.append(child_result)

    if len(child_results) == 0:
        result[1] = -inf  # 자식이 없어서 주변에 우수마을이 없음
        return result

    max_index = 0
    max_diff = child_results[0][2] - child_results[0][1]

    for index, child_result in enumerate(child_results):
        diff = child_result[2] - child_result[1]
        if max_diff < diff:
            max_diff = diff
            max_index = index

    for index, child_result in enumerate(child_results):
        result[0] += child_result[1]
        result[2] += max(child_result[0], child_result[1])

        if index == max_index:
            result[1] += child_result[2]
        else:
            result[1] += max(child_result[1], child_result[2])

    return result


if __name__ == "__main__":
    n = int(input())
    populations = [int(string) for string in input().split()]
    edges = [[int(string) for string in input().split()] for i in range(n - 1)]
    answer = solution(n, populations, edges)
    print(answer)

# undirected graph
# 모든 마을 연결, edge 개수 n - 1
# tree

# max(sum of populations)
# 현재 우수, 자식 비우수
# 현재 비우수, 자식 우수
#
# 현재 비우수 ->
#   자식 우수 손자 비우수
#   자식 비우수 손자 우수
# 우수 - 우수 불가능
# 우수 - 비우수 - 비우수 또는 비우수 - 비우수 - 우수 또는 우수 - 비우수 - 우수 또는 비우수 - 우수 - 비우수 가능

# 1. 현재 비우수, 자식 전부 다 비우수
# 2. 현재 비우수, 자식 중 한명 이상 우수
# 3. 현재 우수, 자식 모두 비우수

# 부모 입장에서
# 1. 현재 비우수: 자식 전부 2
# 2. 현재 비우수: 자식 하나 이상 3, 나머지 2
# 3. 현재 우수, 자식 전부 1 또는 2

# 가장 낮은 노드
# 1. 0
# 2. 0
# 3. arr[node]

# 정답: arr[0][2] + arr[0][3]

# 시간복잡도: O(n)
