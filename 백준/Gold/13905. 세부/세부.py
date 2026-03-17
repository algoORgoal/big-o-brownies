from sys import setrecursionlimit

setrecursionlimit(10 ** 5 + 10)


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return

        self.parent[root1] = root2


def solution(n, m, source, destination, edges):
    disjointSet = DisjointSet(n + 1)
    sorted_edges = sorted([(weight, start, end)
                          for start, end, weight in edges], reverse=True)
    for weight, start, end in sorted_edges:
        if disjointSet.find(start) != disjointSet.find(end):
            disjointSet.union(start, end)
            if disjointSet.find(source) == disjointSet.find(destination):
                return weight

    return 0


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    source, destination = [int(string) for string in input().split()]
    edges = [[int(string) for string in input().split()] for i in range(m)]
    answer = solution(n, m, source, destination, edges)
    print(answer)


# source부터 destination까지의 경로 중 최소 weight의 최댓값

# 1. edge를 weight 순으로 정렬
# 2. 정렬된 순서대로 순회: 현재 edge가 cycle을 만들지 않는다면(같은 connected component 안에 없다면)
#      연결
#      만약 source와 destination이 같은 connected component 안에 있게 된다면
#        해당 값 반환

# 증명
#  방금 연결된 edge가 없는 경우 =>
#    1. 기존 컴포넌트로의 edge로만 연결되는 방법: 없음
#    2. 다른 edge 추가 => 무조건 해당 edge <= 현재 선택한 edge
#  따라서 현재가 최선


# 5 5
# 1 5
# 2 3 1
# 2 4 2
# 2 5 3
# 3 4 4
# 3 5 5


# 시간복잡도 O(m + mlogm)
# 공간복잡도 O(n + m)
