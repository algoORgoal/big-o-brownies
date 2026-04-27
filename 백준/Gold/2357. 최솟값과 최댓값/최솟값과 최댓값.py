from math import inf
from sys import setrecursionlimit

setrecursionlimit(100_000)


class MinSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0 for i in range(self.n * 4)]
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            self.build(left, start, mid)
            self.build(right, mid + 1, end)
            self.tree[node] = min(self.tree[left], self.tree[right])

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        # 현재 node가 담당하는 구간: [start, end]
        # 내가 알고 싶은 구간: [left, right]

        # 1. 아예 안 겹침
        if end < left or right < start:
            return inf

        # 2. 현재 node 구간이 내가 원하는 구간에 완전히 포함됨
        if left <= start and end <= right:
            return self.tree[node]

        # 3. 일부만 겹침 -> 자식으로 내려감
        mid = (start + end) // 2

        left_min = self._query(node * 2 + 1, start, mid, left, right)
        right_min = self._query(node * 2 + 2, mid + 1, end, left, right)

        return min(left_min, right_min)


class MaxSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0 for i in range(self.n * 4)]
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            self.build(left, start, mid)
            self.build(right, mid + 1, end)
            self.tree[node] = max(self.tree[left], self.tree[right])

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        # 현재 node가 담당하는 구간: [start, end]
        # 내가 알고 싶은 구간: [left, right]

        # 1. 아예 안 겹침
        if end < left or right < start:
            return -inf

        # 2. 현재 node 구간이 내가 원하는 구간에 완전히 포함됨
        if left <= start and end <= right:
            return self.tree[node]

        # 3. 일부만 겹침 -> 자식으로 내려감
        mid = (start + end) // 2

        left_max = self._query(node * 2 + 1, start, mid, left, right)
        right_max = self._query(node * 2 + 2, mid + 1, end, left, right)

        return max(left_max, right_max)


def solution(n, m, nums, queries):
    min_segment_tree = MinSegmentTree(nums)
    max_segment_tree = MaxSegmentTree(nums)

    results = []

    for start, end in queries:
        min_value = min_segment_tree.query(start, end)
        max_value = max_segment_tree.query(start, end)
        results.append([min_value, max_value])

    return results


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    nums = [0] + [int(input()) for i in range(n)]
    queries = [[int(string) for string in input().split()]for i in range(m)]
    answer = solution(n, m, nums, queries)
    for result in answer:
        print(*result)


# 완전탐색 시간복잡도: O(nm) => 시간초과
# segment tree를 통해 특정 구간의 최소값 및 최대값 구할 수 있음
# 시간복잡도: O(m * log n)
# 공간복잡도: O(n)
