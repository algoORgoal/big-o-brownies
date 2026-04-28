class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0 for i in range(self.n * 4)]
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(node * 2 + 1, start, mid)
            self.build(node * 2 + 2, mid + 1, end)
            self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if end < left or right < start:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self._query(node * 2 + 1, start, mid, left, right)
        right_sum = self._query(node * 2 + 2, mid + 1, end, left, right)

        return left_sum + right_sum

    def update(self, index, value):
        self.arr[index] = value
        self._update(0, 0, self.n - 1, index)

    def _update(self, node, start, end, index):
        if start == end:
            if start == index:
                self.tree[node] = self.arr[index]
        else:
            if start <= index <= end:
                mid = (start + end) // 2
                self._update(node * 2 + 1, start, mid, index)
                self._update(node * 2 + 2, mid + 1, end, index)
                self.tree[node] = self.tree[node * 2 + 1] + \
                    self.tree[node * 2 + 2]


def solution(n, q, arr, queries):
    segment_tree = SegmentTree(arr)
    results = []

    for query in queries:
        x, y, a, b = query[0] - 1, query[1] - 1, query[2] - 1, query[3]
        if x < y:
            result = segment_tree.query(x, y)
        else:
            result = segment_tree.query(y, x)
        results.append(result)

        segment_tree.update(a, b)

    return results


if __name__ == "__main__":
    n, q = [int(string) for string in input().split()]
    arr = [int(string) for string in input().split()]
    queries = [[int(string) for string in input().split()] for i in range(q)]
    answer = solution(n, q, arr, queries)
    for num in answer:
        print(num)


# 특정 구간의 합 => O(n * q) => 10 ** 5 * 10 ** 5 = 10 ** 10 => 시간초과
# segment tree를 사용시 시간복잡도 => O(q * logn)
# 구간합 구하기 => query
# 숫자 바꾸기 => update
