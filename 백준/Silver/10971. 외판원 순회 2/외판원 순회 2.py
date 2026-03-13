from math import inf


def solution(n, matrix):
    return dfs(0, set([0]), n, matrix)


def dfs(current, visited, n, matrix):
    if len(visited) == n:
        if matrix[current][0] != 0:
            return matrix[current][0]
        else:
            return inf

    minimal_distance = inf
    for i in range(n):
        if i not in visited and matrix[current][i] != 0:
            visited.add(i)
            minimal_distance = min(
                matrix[current][i] + dfs(i, visited, n, matrix), minimal_distance)
            visited.remove(i)

    return minimal_distance


if __name__ == "__main__":
    n = int(input())
    matrix = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, matrix)
    print(answer)
