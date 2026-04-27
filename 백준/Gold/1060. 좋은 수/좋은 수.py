import heapq
from bisect import bisect_right
from math import inf

# [2, 5, 10, 15]
# 20


def solution(l, nums, n):
    sorted_nums = sorted(nums)
    numbers = [0] + sorted_nums

    pq = []

    for num in numbers:
        heapq.heappush(pq, (0, num))

    visited = set()
    stack = []

    while len(pq) > 0 and len(stack) <= n:
        count, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        stack.append(node)

        visited.add(node)

        next_nodes = [node - 1, node + 1]

        for next_node in next_nodes:
            if next_node <= 0:
                continue

            # next_node보다 큰 수 중에서 최솟값을 찾는다.
            upper_bound = bisect_right(numbers, next_node)
            if upper_bound >= len(numbers):
                heapq.heappush(pq, (inf, next_node))
            else:
                lower_bound = upper_bound - 1

                next_count = (next_node - numbers[lower_bound]) * \
                    (numbers[upper_bound] - next_node) - 1

                heapq.heappush(pq, (next_count, next_node))

    return [num for num in stack if num != 0]


if __name__ == "__main__":
    l = int(input())
    nums = [int(string) for string in input().split()]
    n = int(input())
    answer = solution(l, nums, n)
    print(*answer)


# bisect_right: num 중에 크거나 같은 최솟값. 같은 값이 있을 경우 가장 왼쪽 인덱스
# bisect_left: num 중에 크거나 같은 최솟값. 같은 값이 있을 경우 가장 오른쪽 인덱스 + 1

# 각 숫자 별 집합 개수 세기 (n - lower_bound) * (upper_bound - n) - 1
# a + b = c인데 c가 고정일 때 a * b 최대값 => a == b일 때(짝수) a = b - 1일 때(홀수)
# 따라서 뽑아낸 숫자 기준으로 양옆 탐색하기
# bisect_right => logc
# nlogn * logc
