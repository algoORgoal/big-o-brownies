from sys import setrecursionlimit

setrecursionlimit(10 ** 8)


def solution(s, t):

    return dfs(s, t)


def dfs(current, target):
    if len(current) == len(target):
        return current == target

    if current not in target and current[::-1] not in target:
        return False

    return dfs(current + "A", target) or dfs((current + "B")[::-1], target)


if __name__ == "__main__":
    s = input()
    t = input()
    answer = solution(s, t)
    if answer == True:
        print(1)
    else:
        print(0)


# 상태공간 모두 탐색
# A 추가 / B 추가하고 문자열 뒤집기
# 두 연산 모두 문자열 길이가 길어짐
# 길이 1에서 50 => 2 ** 50 불가능

# 중간에 불가능한 경우 탐색 중단: s의 A 개수 > T의 A 개수 or s의 B 개수 > T의 B 개수
# s의 길이 > t의 길이
#


# f(n) = f(뒤집기) or f(A추가)
# A개수 25 B개수 25


# A
# ABABABABABABABABABABABABABABABABABABABABABABABABAB

# A
# ABABABABABABABABABABABABAB
