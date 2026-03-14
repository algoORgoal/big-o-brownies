from sys import setrecursionlimit
from math import inf

setrecursionlimit(16 * 2 ** 16 + 10)


def solution(n, matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = inf
    cache = {}
    return dfs(0, 1, n, matrix, cache)


def dfs(current, visited, n, matrix, cache):
    if (current, visited) in cache:
        return cache[current, visited]

    if visited ^ ((2 ** n) - 1) == 0:
        cache[current, visited] = matrix[current][0]
        return cache[current, visited]

    min_distance = inf

    for i in range(n):
        if visited & (2 ** i) == 0:
            next_distance = dfs(i, visited | (
                2 ** i), n, matrix, cache)
            min_distance = min(
                next_distance + matrix[current][i], min_distance)

    cache[current, visited] = min_distance
    return cache[current, visited]


if __name__ == "__main__":
    n = int(input())
    matrix = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, matrix)
    print(answer)

# 16! = 20_922_789_888_000
# 모든 상태 공간 탐색이 불가능하다.

# 비트마스킹으로, 방문했던 route 표현 가능
# 동일한 route 상태에 있을 때, (현재 방문 노드, 방문했던 route, 최단거리) 표현 가능
# 총 n * 2 ** n번 탐색

# 시간복잡도: O(n * 2 ** n)
# 공간복잡도: O(n * 2 ** n)

# n = 16 => n * 2 ** n = 1048576

# 상태: current, visited, n, matrix, cache
