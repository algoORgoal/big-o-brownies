import heapq
from math import inf
from sys import stdin

input = stdin.readline


def solution(n, k, requests):
    queue = []

    maximum = -inf

    for index, request in enumerate(requests):
        heapq.heappush(queue, (request, index))

        while len(queue) > 0 and queue[0][1] <= index - k:
            heapq.heappop(queue)

        if len(queue) >= k - 1:
            maximum = max(maximum, queue[0][0])

    return maximum


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
