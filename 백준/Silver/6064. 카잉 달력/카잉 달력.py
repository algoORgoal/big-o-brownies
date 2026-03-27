from math import lcm


def solution(m, n, x, y):
    for i in range(x, lcm(m, n) + 1, m):
        if (i - y) % n == 0:
            return i

    return -1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        m, n, x, y = [int(string) for string in input().split()]
        answer = solution(m, n, x, y)
        print(answer)


# 가장 마지막 숫자
# k % m = 0
# k % n = 0


# x:y (1 <= x <= m, 1 <= y <= n)


# 1:1
# 2:2
# 3:3
# 4:4
# 5:5
# 6:6
# 7:7
# 8:8
# 9:9
# 10:10
# 1:11
# 2:12
# 3:1

# m, n, x, y => k such that x:y represents the kth year
# 1 <= m, n <= 40_000, 1 <= x <= m, 1 <= y <= n

# 16 * 10_000 * 10_000 = 16 * 10 ** 8
# 100 000 000
# 16억 => 시간 초과

# 33 % 10 = 3
# 33 % 12 = 9

# 33 % 10 = 3
# 33 % 12 = 9

# (33 - 3) % 10 = 0
# (33 - 9) % 12 = 0

# (k - 3) % 10 = 0
# (k - 9) % 12 = 0

# (k - x) % m = 0
# k = x + mt
# (k - y) % n = 0

# k = 3 + 10t_1
# k = 9 + 12t_2


# 10으로 나누었을 때 3이 되고, 12로 나누었을 때 9가 되는 수는?
# k % 10 = 3
# k % 12 = 9


# 13 % 10(m) = 3
# 13 % 12(n) = 1


# k = a * 10 + 3
# k = b * 12 + 9
