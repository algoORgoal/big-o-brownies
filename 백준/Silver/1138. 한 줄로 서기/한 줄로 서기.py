from itertools import permutations
from functools import cmp_to_key


def comparator(a, b):
    a_ahead, a_value = a
    b_ahead, b_value = b

    if ahead != b_ahead:
        return a_ahead - b_ahead
    else:
        return b_value - a_value


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


# print(10 ** 2 * factorial(10))


def solution(n, aheads):
    line = [0 for i in range(n)]
    for i, ahead in enumerate(aheads):
        height = i + 1

        zero_count = 0
        for j in range(n):
            if line[j] != 0:
                continue
            if zero_count == ahead:
                line[j] = height
                break
            else:
                zero_count += 1

    return line


if __name__ == "__main__":
    n = int(input())
    ahead = [int(string) for string in input().split()]
    answer = solution(n, ahead)
    for index, num in enumerate(answer):
        if index == len(answer) - 1:
            print(num, end="\n")
        else:
            print(num, end=" ")


# 4 2 1 3

# 4 앞에 2개
# 2 앞에 1개
# 1 앞에 2개
# 3 앞에 1개

# n <= 10
# search space => n!
# 각 상태마다, 각 자리에 있는 수보다 더 크게 있는 숫자를 확인 => O(n ** 2)
# O(n ** 2 * n!)

# 362_880_000
# 3억 => 시간초과
# pypy로는 통과함

# 해결책 2
# 빈 공간이 ahead개 나오는 지점에 해당 사람을 넣기
# 이전에 탐색한 건 모두 해당 사람보다 키가 작고, 빈 공간에 나올 사람은 모두 키가 큼
# 따라서 만족
