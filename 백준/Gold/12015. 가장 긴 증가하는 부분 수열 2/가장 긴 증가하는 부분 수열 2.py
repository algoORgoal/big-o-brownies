from sys import stdin
from math import inf
from bisect import bisect_left


input = stdin.readline


def solution(n, nums):
    tails = []
    for num in nums:
        index = bisect_left(tails, num)

        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num
    return len(tails)


if __name__ == "__main__":
    n = int(input().strip())
    nums = [int(string) for string in input().strip().split()]
    answer = solution(n, nums)
    print(answer)

# 9
# 10 20 10 15 16 11 12 13 14
# 1  2  1  2  3  2  3  4  5

# 16 15

# 14 13 12 11

# 10

#    10
#       20
#      15
#     11 16
#      12
#       13
#        14
# 10 20
# 10
# 10 15 16
# 10 11 12 13 14

# 30

# (10, 0) (20, 1) (10, 2), (15, 3), (16, 4), (11, 5), (12, 6), (13, 7), (14, 8)
# 10: [0, 2]
# 11: [5]
# 12: [6]
# 13: [7]
# 14: [8]
# 15: [3]
# 16: [4]
# 20: [1]

# [10, 11, 12, 13, 14, 15, 16, 20]


# (10, 1)
# (10, 1), (20, 2)
# (10, 1), (20, 2)
# (10, 1), (15, 2), (20, 2)
# (10, 1), (15, 2), (16, 3), (20, 2)
# (10, 1), (11, 2), (20, 2)
# (10, 1), (11, 2), (12, 3), (20, 2)
# (10, 1), (11, 2), (12, 3), (13, 4), (20, 2)
# (10, 1), (11, 2), (12, 3), (13, 4), (14, 5), (20, 2)

# 같은 값일 경우 => 더 많이쌓인 놈만 기억하면 됌
# 8 9 10 5 6 7 8 9 10

# 10 11 12 13 14

# stack 활용
# (10, 1)
# 10 < 20 => (20, 2)
# 10


# 10 20 10 11 12 13
# 10 20 10 30 20 50

# 10 20 최대 길이 2, 가장 큰 숫자 20
# 10 11 12 13

# 10 20 최대 길이 2, 가장 큰 숫자 20
# 10 30 20 50 뭘까?


# 1. 배열 뒤집기
# 2. 배열 순회, stack top > num일 경우 유지, stack top <= num인 경우 pop
# 3. stack.append(current)
# 4. 길이 체크
