class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0 for i in range(4 * n)]
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(node * 2 + 1, start, mid)
            self.build(node * 2 + 2, mid + 1, end)
            self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):

        # 겹치는 부분이 없음
        if end < left or right < start:
            return 0

        # 찾는 구간 안에 현재 커버하는 구간이 들어옴
        if left <= start and end <= right:
            return self.tree[node]

        # 겹치는 부분과 안 겹치는 부분이 공존
        mid = (start + end) // 2

        left_sum = self._query(2 * node + 1, start, mid, left, right)
        right_sum = self._query(2 * node + 2, mid + 1, end, left, right)

        return left_sum + right_sum

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
                self._update(2 * node + 1, start, mid, index)
                self._update(2 * node + 2, mid + 1, end, index)
                self.tree[node] = self.tree[node * 2 + 1] + \
                    self.tree[node * 2 + 2]


def solution(n, m, k, nums, queries):
    segment_tree = SegmentTree(nums)

    results = []
    for query in queries:
        type = query[0]
        if type == 1:
            index, value = query[1:]
            segment_tree.update(index, value)
        else:
            left, right = query[1:]
            sum = segment_tree.query(left, right)
            results.append(sum)

    return results


if __name__ == "__main__":
    n, m, k = [int(string) for string in input().split()]
    nums = [0] + [int(input()) for i in range(n)]
    queries = [[int(string) for string in input().split()]
               for i in range(m + k)]
    answer = solution(n, m, k, nums, queries)
    for num in answer:
        print(num)


# query를 구하는데 걸리는 시간 => O(kn) => 시간초과
# segment tree: update, query를 logn 시간안에 수행
# 시간복잡도 O((m + k)logn)
# 공간복잡도 O(n)
