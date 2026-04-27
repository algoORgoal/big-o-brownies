from math import inf


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0 for i in range(4 * self.n)]
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(node * 2 + 1, start, mid)
            self.build(node * 2 + 2, mid + 1, end)
            self.tree[node] = min(self.tree[node * 2 + 1],
                                  self.tree[node * 2 + 2])

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if end < left or right < start:
            return inf

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_min = self._query(node * 2 + 1, start, mid, left, right)
        right_min = self._query(node * 2 + 2, mid + 1, end, left, right)
        return min(left_min, right_min)


def solution(n, m, nums, queries):
    segment_tree = SegmentTree(nums)

    results = []

    for query in queries:
        start, end = [num - 1 for num in query]
        result = segment_tree.query(start, end)
        results.append(result)

    return results


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    nums = [int(input()) for i in range(n)]
    queries = [[int(string) for string in input().split()] for i in range(m)]
    answer = solution(n, m, nums, queries)
    for num in answer:
        print(num)

# query마다 구간 규칙이 없을 때 제일 작은 정수 =>
# brute force: O(nm) => TLE
# segment tree => O(m logn)
# build, query만 필요
