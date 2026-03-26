from collections import deque
from math import inf


def solution(w, k):
    table = {}
    shortest = inf
    longest = -inf
    for i, char in enumerate(w):
        if char not in table:
            table[char] = deque()

        if len(table[char]) < k:
            table[char].append(i)
            if len(table[char]) == k:
                start, end = table[char][0], table[char][len(table[char]) - 1]
                shortest = min(shortest, end - start + 1)
                longest = max(longest, end - start + 1)
        elif len(table[char]) == k:
            table[char].popleft()
            table[char].append(i)

            start, end = table[char][0], table[char][len(table[char]) - 1]
            shortest = min(shortest, end - start + 1)
            longest = max(longest, end - start + 1)

    if shortest == inf:
        return -1

    return shortest, longest


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        w = input()
        k = int(input())
        answer = solution(w, k)
        if answer == -1:
            print(answer)
        else:
            shortest, longest = answer
            print(f"{shortest} {longest}")

# 완전 탐색: 각 인덱스별로 문자열 k개를 포함하는 가장 짧은 문자열 구하기 O(n), 다음 문자 포함했을 떄 해당 문자 개수 k개 되면 stop
#          각 인덱스별 문자열 중 가장 짧은 문자열의 길이, 가장 긴 문자열의 길이 구하기
# O(100 * n ** 2) (n <= 10_000 ** 2)
# 100_000_000 * 100 => 100억 시간초과

# 1. k개를 포함하는 가장 짧은 문자열 구하기
# start = 0, end = 0
# table = { string[i]: 1 }

# shortest = inf

# while True:
#   end += 1
#   table[string[end]] += 1
#   if table[string[end]] == k:
#     while string[start] != string[end]:
#       table[string[start]] -= 1
#       start += 1
#
#   shortest = min(shortest, (end - start) + 1)

# 투포인터로 shortest는 찾을 수 있을 듯
# 현재 찾은 놈이 (start, end)이면, 다음 놈의 start는 무조건 현재 찾은 놈의 start보다 오른쪽에 있어야 함
# 그래야 길이가 더 짧아짐

# shortest = inf

# while True:
#   end += 1
#   table[string[end]] += 1
#   if table[string[end]] == k:
#     while string[start] != string[end]:
#       table[string[start]] -= 1
#       start += 1
#
#   shortest = min(shortest, (end - start) + 1)


# r: [4, 11]
# 현재 접근하는 요소에 < k개 들어있을 때
#   - 인덱스 넣기
#   - 만약 k개가 되었다면 => (end - start + 1) 계산
# 현개 접근하는 요소가 k개 들어있을 때
#   - 첫번째 인덱스 빼기
#   - 인덱스 넣기
#   - (end - start + 1) 계산
# shortest, longest 모두 계산 가능
# 시간복잡도: O(n) (문자열의 길이)
