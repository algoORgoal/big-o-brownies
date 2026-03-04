from re import S


def solution(n, m, r, matrix, commands):

    for command in commands:
        matrix = run_command(len(matrix), len(matrix[0]), matrix, command)

    return matrix


def run_command(n, m, matrix, command):
    if command == 1:
        new_matrix = [[0 for j in range(0, m)]for i in range(0, n)]
        for i in range(0, n):
            for j in range(0, m):
                new_matrix[n - 1 - i][j] = matrix[i][j]
        return new_matrix
    if command == 2:
        new_matrix = [[0 for j in range(0, m)]for i in range(0, n)]
        for i in range(0, n):
            for j in range(0, m):
                new_matrix[i][m - 1 - j] = matrix[i][j]
        return new_matrix
    if command == 3:
        new_matrix = [[0 for j in range(0, n)]for i in range(0, m)]
        for i in range(0, n):
            for j in range(0, m):
                new_matrix[j][n - 1 - i] = matrix[i][j]
        return new_matrix
    if command == 4:
        new_matrix = [[0 for j in range(0, n)]for i in range(0, m)]
        for i in range(0, n):
            for j in range(0, m):
                new_matrix[m - 1 - j][i] = matrix[i][j]
        return new_matrix
    if command == 5:
        new_matrix = [[0 for j in range(0, m)]for i in range(0, n)]
        for i in range(0, n):
            for j in range(0, m):
                area = resolve_area(n, m, i, j)
                if area == 0:
                    new_matrix[i][j + (m // 2)] = matrix[i][j]
                elif area == 1:
                    new_matrix[i + (n // 2)][j] = matrix[i][j]
                elif area == 2:
                    new_matrix[i][j - (m // 2)] = matrix[i][j]
                elif area == 3:
                    new_matrix[i - (n // 2)][j] = matrix[i][j]
        return new_matrix
    else:
        new_matrix = [[0 for j in range(0, m)]for i in range(0, n)]
        for i in range(0, n):
            for j in range(0, m):
                area = resolve_area(n, m, i, j)
                if area == 0:
                    new_matrix[i + (n // 2)][j] = matrix[i][j]
                elif area == 1:
                    new_matrix[i][j - (m // 2)] = matrix[i][j]
                elif area == 2:
                    new_matrix[i - (n // 2)][j] = matrix[i][j]
                elif area == 3:
                    new_matrix[i][j + (m // 2)] = matrix[i][j]
        return new_matrix


def resolve_area(n, m, x, y):
    if 0 <= x < n / 2 and 0 <= y < m / 2:
        return 0
    if 0 <= x < n / 2 and m / 2 <= y < m:
        return 1
    if n / 2 <= x < n and m / 2 <= y < m:
        return 2
    if n / 2 <= x < n and 0 <= y < m / 2:
        return 3


if __name__ == "__main__":
    n, m, r = [int(string) for string in input().split(' ')]

    matrix = [[int(string) for string in input().split(' ')]
              for i in range(0, n)]
    commands = [int(i) for i in input().split(' ')]
    answer = solution(n, m, r, matrix, commands)
    for i in range(0, len(answer)):
        for j in range(0, len(answer[i])):
            if j == len(answer[i]) - 1:
                print(answer[i][j], end="\n")
            else:
                print(answer[i][j], end=" ")


# n * m * r <= 100 * 100 * 1_000 = 10 ** 7
# 한번 연산할 때마다 어차피 n * m => 새로운 matrix 만들어도 시간복잡도는 동일
