from sys import stdin
from bisect import bisect_left
from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10 ** 6 + 10)

input = stdin.readline


def solution(n, nums):
    tails = []
    num_indices = []
    graph = {}
    parent_table = {}

    for num_index, num in enumerate(nums):
        index = bisect_left(tails, num)

        if index > 0:
            previous_index = num_indices[index - 1]

            if previous_index not in graph:
                graph[previous_index] = []

            graph[previous_index].append(num_index)

            parent_table[num_index] = previous_index

        if index == len(tails):
            tails.append(num)
            num_indices.append(num_index)
        else:
            tails[index] = num
            num_indices[index] = num_index

    # child - parent 관계가 성립
    # 모든 노드가 connected되어 있진 않음
    # tree의 집합으로 볼 수 있음

    nodes = set()
    for parent in graph:
        nodes.add(parent)
        for child in graph[parent]:
            nodes.add(child)

    visited = {}
    for node in nodes:
        if node not in visited:
            dfs(node, graph, visited, 0)

    # 모든 노드의 child-parent 연결 관계가 없는 경우
    if len(nodes) == 0:
        print(1)
        print(nums[0])
        return

    max_node = list(nodes)[0]
    for node in visited:
        if visited[node] > visited[max_node]:
            max_node = node

    index_path = deque()
    current = max_node

    while current is not None:
        index_path.appendleft(current)
        current = parent_table.get(current)

    print(visited[max_node] + 1)
    print(*[nums[index] for index in index_path])


def dfs(current, graph, visited, depth):
    if current in visited:
        return

    visited[current] = depth

    if current in graph:
        for adjacent_node in graph[current]:
            dfs(adjacent_node, graph, visited, depth + 1)


if __name__ == "__main__":
    n = int(input().strip())
    nums = [int(string) for string in input().strip().split()]
    solution(n, nums)


# 시간복잡도 O(nlogn) + O(n)
# 공간복잡도 O(n)

# 인덱스로 안 할 경우 문제점
# 2 3 1 2
# {2: [3], 1: [2]} -> 1, 2, 3
# 앞에 나오는 2와 뒤에 나오는 2가 구별되지 않아서, 원래 안 되는 경로 생성 가능
# 따라서 {[부모 인덱스]: [자식 인덱스]} 관계로 설정해야 함

# 시간복잡도: O(n)
