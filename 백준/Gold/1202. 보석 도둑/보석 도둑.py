from functools import cmp_to_key
from sys import stdin
from collections import deque
import heapq


def comparator(a, b):
    mass1, value1 = a
    mass2, value2 = b
    return mass1 - mass2


input = stdin.readline


def solution(n, k, jewelry_pieces, bags):
    sorted_mass_and_value = deque(sorted(
        [(mass, value) for mass, value in jewelry_pieces], key=cmp_to_key(comparator)))
    queue = []

    value_sum = 0

    for bag in sorted(bags):
        while len(sorted_mass_and_value) > 0 and sorted_mass_and_value[0][0] <= bag:
            mass, value = sorted_mass_and_value.popleft()
            heapq.heappush(queue, (-value, mass))

        if len(queue) > 0:
            negative_value, mass = heapq.heappop(queue)
            value_sum += (-negative_value)
    return value_sum


if __name__ == "__main__":
    n, k = [int(string) for string in input().split()]
    jewelry_pieces = [[int(string) for string in input().split()]
                      for i in range(n)]
    bags = [int(input()) for i in range(k)]
    answer = solution(n, k, jewelry_pieces, bags)
    print(answer)


# 입력: O(n + k) (1 <= n, k, <= 300_000)
# readline을 통해 입력을 받아야 함

# 현재 가방이 소화할 수 있는 보석까지 push하고, 그 중에서 가치가 가장 큰 것을 pop하기
# 보석은 mass 기준으로 오름차순
# 가치가 가장 큰 것 => heapq에 부호 음수 붙이기 (negative_value, mass)
