from sys import stdin
from math import inf

input = stdin.readline


def solution(n, k, arr):
    table = {i: 0 for i in range(1, 100_001)}
    table[arr[0]] = 1
    end = 0

    max_length = -inf
    for start in range(n):
        if start > 0:
            table[arr[start - 1]] -= 1
        while True:
            if end + 1 < n and table[arr[end + 1]] + 1 <= k:
                table[arr[end + 1]] += 1
                end += 1
            else:
                break
        max_length = max(max_length, end - start + 1)

    return max_length


if __name__ == "__main__":
    n, k = [int(string) for string in input().split()]
    arr = [int(string) for string in input().split()]
    answer = solution(n, k, arr)
    print(answer)

# 같은 정수를 k개 이하로 포함
# 최장 연속 부분 수열의 길이 구하기
# arr[i]에서 시작하는 같은 정수가 K개 이하인 최장 연속 부분 수열을 각각 구하기
#  초기 값:
#    i == 0 => table = {}
#    i != 0 => table[arr[current - 1]] -= 1
# 계속 진행하다가, table[arr[current]] == k인 경우 break
#

# 시간복잡도: O(n)
