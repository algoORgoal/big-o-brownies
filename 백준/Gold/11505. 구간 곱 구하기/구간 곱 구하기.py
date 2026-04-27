
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0 for i in range(4 * n)]
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(node * 2 + 1, start, mid)
            self.build(node * 2 + 2, mid + 1, end)
            self.tree[node] = (self.tree[node * 2 + 1] *
                               self.tree[node * 2 + 2]) % 1_000_000_007

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        # 범위 밖
        if end < left or right < start:
            return 1  # 1은 무슨 수를 곱하더라도 자기 자신이 된다.

        # 범위 안
        if left <= start and end <= right:
            return self.tree[node]

        # 겹치는 범위도 있고, 안 겹치는 범위도 있음
        mid = (start + end) // 2
        left_result = self._query(node * 2 + 1, start, mid, left, right)
        right_result = self._query(node * 2 + 2, mid + 1, end, left, right)
        return (left_result * right_result) % 1_000_000_007

    def update(self, index, value):
        self.arr[index] = value
        self._update(0, 0, self.n - 1, index)

    def _update(self, node, start, end, index):
        if start == end:
            if start == index:
                self.tree[node] = self.arr[start]
        else:
            if start <= index <= end:
                mid = (start + end) // 2
                self._update(node * 2 + 1, start, mid, index)
                self._update(node * 2 + 2, mid + 1, end, index)
                self.tree[node] = (self.tree[node * 2 + 1] *
                                   self.tree[node * 2 + 2]) % 1_000_000_007


def solution(n, m, k, nums, queries):
    segment_tree = SegmentTree(nums)

    results = []
    for query in queries:
        type = query[0]
        if type == 1:
            index, value = query[1] - 1, query[2]
            segment_tree.update(index, value)
        else:
            left, right = query[1] - 1, query[2] - 1
            result = segment_tree.query(left, right)
            results.append(result)

    return results


if __name__ == "__main__":
    n, m, k = [int(string) for string in input().strip().split()]
    nums = [int(input().strip()) for i in range(n)]
    queries = [[int(string) for string in input().strip().split()]
               for i in range(m + k)]
    answer = solution(n, m, k, nums, queries)
    for num in answer:
        print(num)


# 수의 변경이 일어날 때마다 곱 결과가 바뀜
# brute force시 O(m + nk) n <= 1_000_000 , k <= 10_000 => nk <= 10 ** 10 => TLE
# segment tree에 구간곱 결과 저장 => 시간복잡도 O((m + k) log n) 20_000 * log 1_000_000 =>
# 공간복잡도 O(m + n + k)
