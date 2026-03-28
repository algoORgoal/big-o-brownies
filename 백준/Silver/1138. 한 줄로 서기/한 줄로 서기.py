from itertools import permutations


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


# print(10 ** 2 * factorial(10))


def solution(n, ahead):
    people = [i for i in range(1, n + 1)]
    for permutation in permutations(people, n):
        table = {}

        for i in range(len(permutation)):
            for j in range(i):
                if permutation[j] > permutation[i]:
                    if permutation[i] not in table:
                        table[permutation[i]] = 0

                    table[permutation[i]] += 1

        arr = [table[i] if i in table else 0 for i in range(1, n + 1)]

        if arr == ahead:
            return permutation

    return n


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
