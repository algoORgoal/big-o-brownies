from sys import stdin
from math import inf

input = stdin.readline


def solution(n, s, arr):
    start = 0
    end = 0
    sum = 0
    minimal_length = inf

    for end in range(n):
        sum += arr[end]
        while start < end:
            if sum - arr[start] >= s:
                sum -= arr[start]
                start += 1
            else:
                break

        if sum >= s:
            minimal_length = min(minimal_length, end - start + 1)

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


# 알고리즘은  0 <= end <= n - 1에 대하여 sum(end ~ start) >= s인 최댓값 start를 찾는다.
# 못찾는다고 해보자.(proof by induction)
# 1. base case end = 0에 대해서, 최댓값 start_0 찾는다.
# 2. induction step: end = k까지 최댓값 start_k를 찾았다고 가정
#    sum(start_k ~ end_k) >= s 이므로 sum(start_k ~ end_k+1) >= s
#    루프 invaraint에 따라 sum(start_k+1 + 1, end_k+1) < s이므로 start_k+1은 최대한 큰 값을 찾는다.

# 항상 end += 1 or start += 1만 발생하므로 O(n)
