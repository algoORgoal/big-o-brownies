import sys
from math import gcd, lcm

sys.setrecursionlimit(10**7)

# 1. 1인 부분의 공약수이면서, 0인 부분의 공약수가 아님
# 2. 범위는 1 <= x <= L

# 1. 1인 것들을 모아서 최소공배수 찾기 -> L보다 크면 -1
# 2. 0인 것들과 최소공배수가 배수인지 확인 -> 맞으면 최소공배수 반환, 아니면 -1 반환
# 예외 처리
# 1인 것들만 있을 경우: (1)번만 수행하면 됌
# 0인 것들만 있을 경우: 값이 1인 게 있을 경우 -1, 없을 경우 1 반환(1은 모든 수의 배수가 되지 않는다.)

# LCD 찾는 법
# 모든 수의 곱 / GCD


def main(n: int, l: int, numbers: list[int], binaries: list[int]):
    ones = [numbers[index] for index, binary in enumerate(
        binaries) if binary % 2 == 1]
    zeros = [numbers[index] for index, binary in enumerate(
        binaries) if binary % 2 == 0]

    if len(ones) == 0:
        if 1 in zeros: # 모든 자연수는 1의 배수이므로 조건을 만족시키는 자연수가 존재하지 않는다.
            return -1
        else: # 1과 다른 자연수는 최대공약수가 1이므로 조건을 만족시킨다.
            return 1

    a = lcm_list(ones)

    if a == -1:
        return -1
    if a < 1 or a > l:
        return -1
    for i in zeros:
        if a % i == 0:
            return -1
    return a


def lcm_list(list: list[int]):
    acc = list[0]
    for i in list[1:]:
        acc = lcm(acc, i)
        if acc > 10 ** 12: # 최소공배수가 l 이하로 존재하지 않을 수 있음
            return -1
    return acc

if __name__ == "__main__":
    n, l = [int(string) for string in input().split(' ')]
    numbers = [int(string) for string in input().split(' ')]
    binaries = [int(string) for string in input().split(' ')]
    answer = main(n, l, numbers, binaries)
    print(answer)
