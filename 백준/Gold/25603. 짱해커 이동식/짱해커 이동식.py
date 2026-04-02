import heapq
from math import inf
from math import ceil
from sys import stdin

input = stdin.readline


def solution(n, k, requests):

    start = 1
    end = 1_000_000_000

    while start < end:

        mid = (start + end) // 2

        if can_start(requests, k, mid):
            end = mid
        else:
            start = mid + 1

    return start


def can_start(requests, k, m):

    indices = []

    for i in range(len(requests)):
        if requests[i] <= m:
            indices.append(i)

    if len(indices) == 0:
        return False

    left = indices[0]
    right = indices[len(indices) - 1]

    if left > k - 1:
        return False

    if right < len(requests) - 1 - (k - 1):
        return False

    for i in range(len(indices) - 1):
        first, second = indices[i], indices[i + 1]
        if second - first > k:
            return False

    return True


# 0 1 2 3 4

if __name__ == "__main__":
    n, k = [int(string) for string in input().strip().split()]
    requests = [int(string) for string in input().strip().split()]
    answer = solution(n, k, requests)
    print(answer)

# 3 5
# 3 1 5 4 2 => 2 (1, 2)
# 7 1 5 4 2 => 4 (1, 4)

# 최소:

# dp[i][0] i를 포함하지 않을 때 최대값
# dp[i][1] i를 포함할 때 최대값

# dp[i][1] = max(arr[i][1], dp[i - k][1])
# dp[i][0] = max()

# 100_000 ** 2 = 10_000_000_000
#

# 각 요소에서, k - 1 범위 이내에 있는 요소가 선택되면 됌
# k - 1 범위 이내에 있는 요소 중 가장 작은 값
# k - 1 범위 => i - (k - 1)   i + (k - 1)

# 요소 개수가 2 * k - 1개가 되도록 유지
# 가장 작은 값 선택
# maximum = max(가장 작은 값, maximum)


# 시간복잡도 nlogn
# 공간복잡도 n
