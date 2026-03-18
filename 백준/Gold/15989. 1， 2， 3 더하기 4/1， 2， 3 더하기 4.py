from sys import stdin
from sys import stdout
from sys import setrecursionlimit

setrecursionlimit(10 ** 5)

input = stdin.readline


def print(string, end="\n"):
    stdout.write(f"{string}{end}")


def solution(n, arr):
    cache = {}
    return [count(i, 1, cache) for i in arr]


def count(n, k, cache):
    if (n, k) in cache:
        return cache[n, k]
    if k > 3:
        cache[n, k] = 0
        return cache[n, k]
    if n < k:
        cache[n, k] = 0
        return cache[n, k]
    if n == k:
        cache[n, k] = 1
        return cache[n, k]
    if n > k:
        cache[n, k] = count(n - k, k, cache) + count(n, k + 1, cache)
        return cache[n, k]


if __name__ == "__main__":
    n = int(input())
    arr = [int(input().strip()) for i in range(n)]
    answer = solution(n, arr)
    for i in answer:
        print(i)


# 순서대로 사용하기
# k >= 1
# k > 3 => f(n, k) = 0
# n > k => f(n, k) = f(n - k, k) + f(n, k + 1)
# n == k => f(n, k) = 1
# n < k => f(n, k) = 0

# 1 <= n <= 200, 1 <= k <= 4
# 시간복잡도: 2 ** n => O(nk)
# 공간복잡도: O(nk)


# k를 한번 사용 / k를 사용하지 않고 다음으로 넘어감
# f(n, k): n을 k 이상의 수로 나타낼 수 있는 경우의 수
#
