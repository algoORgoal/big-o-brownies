from math import sqrt
from math import inf
from sys import setrecursionlimit

setrecursionlimit(16 * (2 ** 16))


def solution(n, nodes):
    return dfs(nodes[0], 0 | (2 ** 0), nodes)


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def dfs(current, visited, nodes, cache={}):
    if (current, visited) in cache:
        return cache[current, visited]

    if visited ^ ((2 ** len(nodes)) - 1) == 0:
        backward_distance = euclidean_distance(current, nodes[0])
        cache[current, visited] = backward_distance
        return cache[current, visited]

    min_distance = inf
    for i, node in enumerate(nodes):
        if visited & (2 ** i) > 0:  # 이미 방문함
            continue
        weight = euclidean_distance(current, node)

        min_distance = min(min_distance, weight + dfs(
            node, visited | (2 ** i), nodes, cache))

    cache[current, visited] = min_distance
    return cache[current, visited]


if __name__ == "__main__":
    n = int(input())
    nodes = [tuple([int(string) for string in input().split()])
             for i in range(n)]
    n = solution(n, nodes)
    print(n)

# 완전탐색시 경우의 수: O(n!) (n-1) !
# 15! = 1_307_674_368_000 => TLE

# (현재 방문한 도시, 현재까지 방문한 도시의 리스트)가 동일한 경우, 나머지 도시를 방문하는 최단거리만 구하면 됌.
# n * (2 ** n)
# 15 * 2 ** 15 = 491520 => 가능
