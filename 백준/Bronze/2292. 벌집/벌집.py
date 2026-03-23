from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


def solution(n):
    return count(n, 1, 1)


def count(n, current, distance):
    if n <= current:
        return distance
    else:
        return count(n - current, current + 6 if current != 1 else 6, distance + 1)


if __name__ == "__main__":
    n = int(input())
    answer = solution(n)
    print(answer)


# 1
# 7 - 2 + 1 = 6
# 19 - 8 + 1 = 12
# 37 - 20 + 1 = 18
# 61 - 38 + 1 = 24


# 1겹에서 도달 못하면
# 1 빼고, 5 더함, 거리 1 더함
# 2겹에서 도달 못하면
# 6 빼고, 6 더함, 거리 1 더함
# 3겹에서 도달 못하면
# 12 빼고, 6 더함, 거리 1 더함
#
# 13
# n(겹 이동할 때마다 줄어듬) (현재 겹에 있는 개수) (거리))
