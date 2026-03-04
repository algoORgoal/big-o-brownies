from itertools import combinations
from math import inf


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# print(combination(20, 10)) => 184756


def solution(n, matrix):
    people = set([i for i in range(0, n)])

    min_difference = inf
    for combination in combinations(people, n // 2):
        team_a = set(combination)
        team_b = people - team_a
        stat_a = 0
        stat_b = 0
        for i in range(0, n):
            for j in range(0, n):
                if i in team_a and j in team_a:
                    stat_a += matrix[i][j]
                elif i in team_b and j in team_b:
                    stat_b += matrix[i][j]
        difference = abs(stat_a - stat_b)
        min_difference = min(min_difference, difference)

    return min_difference


if __name__ == "__main__":
    n = int(input())
    matrix = [[int(string) for string in input().split(' ')]
              for i in range(0, n)]
    answer = solution(n, matrix)
    print(answer)

# 팀 갈라서, 최소가 되는 경우 구하기
# nC(n/2) (4 <= n <= 20, n은 짝수) => 20C10 = 184756

# 팀별 능력치 합 구하기 => O((n / 2) ** 2) (n <= 20)

# 184756 * 100 = 18_475_600
