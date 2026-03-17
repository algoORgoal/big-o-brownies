from functools import cmp_to_key
from sys import stdin
import bisect


def comparator(a, b):
    value1, mass1 = a
    value2, mass2 = b
    if value1 != value2:
        return value2 - value1
    return mass1 - mass2


input = stdin.readline


def solution(n, k, jewelry_pieces, bags):
    sorted_value_and_mass = sorted(
        [(value, mass) for mass, value in jewelry_pieces], key=cmp_to_key(comparator))

    fw = Fenwick(len(bags))

    sorted_bags = sorted(bags)

    for bag in sorted_bags:
        fw.add(bag, sorted_bags)

    count = 0
    for value, mass in sorted_value_and_mass:
        result = fw.remove_geq(mass, sorted_bags)
        if result != None:
            count += value

    return count


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, diff):
        while i <= self.n:
            self.tree[i] += diff
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def find_kth(self, k):
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)  # 수정!!

        while bit_mask:
            next_idx = idx + bit_mask
            if next_idx <= self.n and self.tree[next_idx] < k:
                k -= self.tree[next_idx]
                idx = next_idx
            bit_mask >>= 1

        return idx + 1

    def add(self, x, values):
        idx = bisect.bisect_left(values, x) + 1  # 1-based
        self.update(idx, 1)

    def remove_geq(self, x, values):
        # x 이상 시작 위치 (0-based)
        pos = bisect.bisect_left(values, x)

        # x보다 작은 개수
        before = self.query(pos)

        total = self.query(self.n)

        if before == total:
            return None  # x 이상 없음

        # x 이상 중 최소값 = (before + 1)번째
        idx = self.find_kth(before + 1)

        self.update(idx, -1)

        return values[idx - 1]


if __name__ == "__main__":
    n, k = [int(string) for string in input().split()]
    jewelry_pieces = [[int(string) for string in input().split()]
                      for i in range(n)]
    bags = [int(input()) for i in range(k)]
    answer = solution(n, k, jewelry_pieces, bags)
    print(answer)


# 입력: O(n + k) (1 <= n, k, <= 300_000)
# readline을 통해 입력을 받아야 함

# 경우의 수 O(n!) (n <= 300_000), 모두 담을 수 있는 경우, 시간초과

# 가장 maximum mass가 가장 작은 가방 순서대로 정렬
# 작은 가방부터 순회:
#   질량이 maximum mass보다 작거나 같으면서, 현재 남아있는 것 중 가치가 가장 큰 것 담기
# O(k * n) = 300_000 * 300_000 = 9 * 10 ** 10 시간초과

# 짐을 가치 순으로 내림차순 정렬
# 들어갈 수 있는 가방 중 가장 maximum mass가 작은 가방에 넣어버림

# 이진 탐색을 통해 찾기 => O(n * logc) (c <= 100_000_000)
# maximum mass보다 작거나 같은 짐 찾기

# 가방 제거에 O(k)이 들어버림 => 시간 초과
