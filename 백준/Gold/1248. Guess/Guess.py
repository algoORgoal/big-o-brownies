from sys import setrecursionlimit

setrecursionlimit(10 ** 8)


def solution(n, table):
    prefix = [0 for i in range(n)]
    return dfs([], prefix, table, n)


def dfs(stack, prefix, table, n):
    current = len(stack)

    if len(stack) == n:
        return stack

    sign = table[current][current]
    if sign == "+":
        candidates = range(1, 11)
    elif sign == "-":
        candidates = range(-10, 0)
    else:
        candidates = range(0, 1)

    for candidate in candidates:
        if all(range_sum(prefix, i, current - 1) + candidate > 0 and table[i][current] == "+"
               or range_sum(prefix, i, current - 1) + candidate < 0 and table[i][current] == "-"
               or range_sum(prefix, i, current - 1) + candidate == 0 and table[i][current] == "0" for i in range(0, current)):
            if current > 0:
                prefix[current] = candidate + prefix[current - 1]
            else:
                prefix[current] = candidate

            stack.append(candidate)
            result = dfs(stack, prefix, table, n)
            if result != None:
                return result

            stack.pop()

    return None


def range_sum(prefix, start, end):
    if end < 0:
        return 0
    if start <= 0:
        return prefix[end]
    return prefix[end] - prefix[start - 1]


if __name__ == "__main__":
    n = int(input())
    sequence = [char for char in input()]
    table = []

    i = n
    while len(sequence) > 0:
        table.append(['' for i in range(0, n - i)] + sequence[0:i])
        sequence = sequence[i:]
        i -= 1

    answer = solution(n, table)
    for i, num in enumerate(answer):
        if i == len(answer) - 1:
            print(num, end="")
        else:
            print(num, end=" ")


# 20 ** 10 = 10_240_000_000_000
# search space의 모든 경우의 수 탐색시 시간초과

#  - => + => -prefix[i - 1] < a[i]
#  + => - => prefix[i - 1] < -a[i]


# a[0] > 0 => prefix[0] = 1
# a[0] == 0 => prefix[0] = 0
# a[0] > 0 => prefix[0] = -1

# - and + => a[i] = abs(prefix[i - 1]) + 1
# + and + => a[i] = 0
# 0 and + => a[i] = 1

# - and 0 => a[i] = abs(prefix[i - 1])
# + and 0 => a[i] = -prefix[i - 1]
# 0 and 0 => a[i] = 0

# - and - => a[i] = 0
# + and - => a[i] = -(abs(prefix[i - 1]) + 1)
# 0 and - => a[i] = -1

# a[i] 최대값: 10
# +-+-+-+-+-
# 12345678910 (진동하는 경우,)
# 생성되는 수열의 요소 abs(a[i]) <= 10


# 필요한 상태
# 1. 지금까지의 선택지 순서 (stack)
# 2. prefix sum
# 3. n
# 4. table

# candidate from -10 to 10:
# current = len(stack)
# for i from 0 to current - 1:
#   range_sum(i, current - 1) + candidate > 0 and table[current][current] == "+"
#   or range_sum(i, current - 1) + candidate < 0 and table[current][current] == "-"
#   or range_sum(i, current - 1) + candidate == 0 and table[current][current] == "0"
#     prefix_sum[current] = candidate + prefix_sum[current - 1]
#     stack.append(candidate)
#     dfs()
#     prefix_sum.pop(current)
#     stack.pop()

# range_sum(prefix, i, j):
#   if j < 0 return 0
#   if i <= 0 return prefix[j]
#   return prefix[j] - prefix[i - 1]


# ++0+-
#  +-+-
#   -+-
#    +-
#     -
