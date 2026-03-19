from sys import stdin
from math import inf

input = stdin.readline


def solution(n, s, arr):
    start = 0
    end = 0
    sum = arr[0]
    minimal_length = inf

    while True:

        while start < end:
            if sum - arr[start] >= s:
                sum -= arr[start]
                start += 1
            else:
                break

        if sum >= s:
            minimal_length = min(minimal_length, end - start + 1)

        if end == n - 1:
            break

        end += 1
        sum += arr[end]

    return minimal_length if minimal_length != inf else 0


if __name__ == "__main__":
    while True:
        line = input().strip()
        if not line:
            break
        n, s = [int(string) for string in line.split()]
        arr = [int(string) for string in input().strip().split()]
        answer = solution(n, s, arr)
        print(answer)


# 10 ** 5
# prefix sum 에 대해서 prefix[j] - prefix[i] (0 <= i < j <= n)
# 시간복잡도 O(n ** 2)이므로 비효율적

# 투포인터?
# start = 0, end = 0

# while True:
#   while start < end:
#     if from start + 1 to end > s:
#       start += 1
#   end += 1
