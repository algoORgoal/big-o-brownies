from sys import stdin
from math import inf

input = stdin.readline


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.num_to_index_list = [(num, index)
                                  for index, num in enumerate(arr)]
        self.num_to_index_list.sort(reverse=True)
        self.arr = arr
        self.tree = [-inf for i in range(4 * n)]
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            if self.arr[start] == -inf:
                self.tree[node] = 0
            else:
                self.tree[node] = 1
        else:
            mid = (start + end) // 2
            self.build(node * 2 + 1, start, mid)
            self.build(node * 2 + 2, mid + 1, end)
            self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def update(self, index, value):
        self.arr[index] = value
        self._update(0, 0, self.n - 1, index)

    def _update(self, node, start, end, index):
        if start == end:
            if start == index:
                if self.arr[index] == -inf:
                    self.tree[node] = 0
                else:
                    self.tree[node] = 1
        else:
            if start <= index <= end:
                mid = (start + end) // 2
                self._update(node * 2 + 1, start, mid, index)
                self._update(node * 2 + 2, mid + 1, end, index)
                self.tree[node] = self.tree[node * 2 + 1] + \
                    self.tree[node * 2 + 2]

    def popall(self):
        sum = 0
        for num, index in self.num_to_index_list:
            if index + 1 <= self.n - 1:
                sum += self.query(index + 1, self.n - 1)
            self.update(index, -inf)

        return sum

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if end < left or right < start:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_count = self._query(node * 2 + 1, start, mid, left, right)
        right_count = self._query(node * 2 + 2, mid + 1, end, left, right)
        return left_count + right_count


def solution(n, nums):
    segment_tree = SegmentTree(nums)
    return segment_tree.popall()


if __name__ == "__main__":
    n = int(input().strip())
    nums = [int(string) for string in input().strip().split()]
    answer = solution(n, nums)
    print(answer)


# 3 2 1
# 2 3 1
# 2 1 3
# 1 2 3

# 버블소트
# n = k일 때, k번째 큰 수 arr[0:n - k]에서 찾기
# k 번째 큰 수 = k + 1번째 큰 수보다 작은 수
# _query(0, 0, self.n - 1, left, right, upper_bound)
# _query(self, node, start, end, left, right, upper_bound):
#   if start == end:
#     if arr[start] <= upper_bound:
#       return arr[start]
#     else:
#       return -inf
#   else:
#     mid = (start + end) // 2
#     left_max = self._query(node * 2 + 1, start, mid, left, right, upper_bound)
#     right_max = self._query(node * 2 + 2, mid + 1, end, left, right, upper_bound)
#
# k번째 큰 수를 arr[n - k] 로 옮기기 (swap 횟수 k번)


# 5 1 3 2 4
# 1 3 2 4 5
# 1 3 2 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# 4번 (1 3 2 4)
# 0번
# 1번
# 5번


# (1, 1), (2, 3), (3, 2), (4, 4), (5, 0)
# _query(0, 0, self.n - 1, 0, upper_bound
# _query(self, node, start, end, left, right):
#   if end < left or start < right
#     return


# 인덱스가 중요한 게 아님: 뒤의 요소가 빠질 수 있기 때문
# 자기 뒤로 요소가 몇개가 있는지 셀 수 있는 게 중요함

# 3 1 5 2 4
# 특정 구간의 가장 큰 값 구하기
# 5가 크다 => 제거
# 4가 크다 => 제거

# 1 2 3 4 5
# 가장 큰 것: 5
# 5를 inf

# 트리 유지하기: positive_tree
# 1. 현재 가장 큰 요소 찾고, 가장 큰 요소가 arr의 어떤 인덱스에 있는지 연결하기
#    [(요소, 인덱스)]
# 2. positive tree에서, 해당 요소에서 끝까지 양수의 개수 찾아서 더하기
# 3. 해당 요소가 들어있는 인덱스 -inf로 만들기

# 시간복잡도: O(nlogn + nlogn)
