def solution(n, m, matrix):
    edges = set([(0, 0), (n - 1, 0), (0, m - 1), (n - 1, m - 1)])
    FLOOR_COUNT = 1
    TOP_COUNT = 1

    sum = 0
    for i in range(n):
        for j in range(m):

            sum += FLOOR_COUNT
            sum += TOP_COUNT

            around = (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
            for around_x, around_y in around:
                if 0 <= around_x < n and 0 <= around_y < m:
                    sum += max(0, matrix[i][j] - matrix[around_x][around_y])
                else:
                    sum += matrix[i][j]

    return sum


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    matrix = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, m, matrix)
    print(answer)


# 바닥면 1, 윗면 1
# 옆면
#   모서리에 있는 경우 => 노출 부분 높이 * 2
#   모서리 아닌 경우 => 노출 부분 높이 * 1
# 접하는 부분 => max((높이 - 이웃한 것 높이), 0)
