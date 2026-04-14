from sys import stdin
from collections import deque

input = stdin.readline


def solution(n, x, visitor_counts):
    queue = deque()

    partial_sum = 0
    for i in range(x):
        partial_sum += visitor_counts[i]
        queue.append(visitor_counts[i])

    max_sum = partial_sum
    count = 1

    for i in range(x, len(visitor_counts)):
        partial_sum -= queue.popleft()
        partial_sum += visitor_counts[i]
        queue.append(visitor_counts[i])

        if partial_sum == max_sum:
            count += 1
        elif partial_sum > max_sum:
            max_sum = partial_sum
            count = 1

    return max_sum, count


if __name__ == "__main__":
    n, x = [int(string) for string in input().strip().split()]
    visitor_counts = [int(string) for string in input().strip().split()]
    max_sum, count = solution(n, x, visitor_counts)
    if max_sum == 0:
        print("SAD")
    else:
        print(max_sum)
        print(count)


# deque 사용하기
# 매번 append 시키고 popleft
# partial_sum 업데이트

# 현재 부분합이 더 크다 => max_sum 업데이트하고 count 0으로 만들기
# 현재 부분합이 같다 => count 증가시키기
# 현재 부분합이 max_sum보다 작다 => 아무것도 안 하기


# 시간복잡도 O(n)
# 공간복잡도 O(n)
