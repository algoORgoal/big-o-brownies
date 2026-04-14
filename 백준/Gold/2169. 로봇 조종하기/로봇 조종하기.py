from math import inf


def solution(n, m, matrix):
    dp = [[-inf for j in range(m)] for i in range(n)]

    for i in range(n):
        if i == 0:
            for j in range(m):
                if j == 0:
                    dp[i][j] = matrix[i][j]
                    continue

                dp[i][j] = dp[i][j - 1] + matrix[i][j]

            continue

        left = [-inf for j in range(m)]

        for j in range(m):
            if j == 0:
                left[j] = dp[i - 1][j] + matrix[i][j]
                continue
            left[j] = max(dp[i - 1][j], left[j - 1]) + matrix[i][j]

        right = [-inf for j in range(m)]

        for j in range(m - 1, -1, -1):
            if j == m - 1:
                right[j] = dp[i - 1][j] + matrix[i][j]
                continue
            right[j] = max(dp[i - 1][j], right[j + 1]) + matrix[i][j]

        for j in range(m):
            dp[i][j] = max(left[j], right[j])

    return dp[n - 1][m - 1]


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    matrix = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, m, matrix)
    print(answer)


# 시간복잡도: O(nm)
# 공간복잡도: O(nm)

# 각 줄별로 왼쪽에서 오는 것, 오른쪽에서 오는 것 따로 계산
