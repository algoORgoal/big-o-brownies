import heapq
from sys import stdin

input = stdin.readline


def solution(n, l, nums):
    queue = []
    d = []
    for index_to_push, num in enumerate(nums):
        index_to_pop = index_to_push - l
        while len(queue) > 0 and queue[0][1] <= index_to_pop:
            heapq.heappop(queue)

        heapq.heappush(queue, (num, index_to_push))
        d.append(queue[0][0])

    print(*d)


if __name__ == "__main__":
    n, l = [int(string) for string in input().strip().split()]
    nums = [int(string) for string in input().strip().split()]
    solution(n, l, nums)


# (5_000_000 * log2(5_000_000) = 111_267_483.32105768
# 시간제한 2.4초 => 가능

# 모든 range에서 최소값 찾기 => O(ln) = O(n ** 2) 시간초과
# 3 6 2 4
# queue(3, 6, 2) => i - l번째 값 빼기
# for index_to_push, num in enumerate(nums):
#   while queue[0].index <= i - l:
#     heapq.heappop(queue)
#   heapq.heappush(queue, (num, index_to_push))
#
#   num = queue[0]
#   d.append(num)
