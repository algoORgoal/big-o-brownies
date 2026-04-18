from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(1000 * 1001 // 2)

input = stdin.readline


def solution(n: int, nodes: set[str], m: int, edges: list[list[str]]):
    graph = {}

    for parent, child in edges:
        if parent not in graph:
            graph[parent] = []
        graph[parent].append(child)

    stack = []
    visited = set()
    for node in nodes:
        dfs(node, graph, visited, stack)

    topo = stack[::-1]

    dp = {node: set() for node in nodes}

    end_nodes = set()
    for node in topo:
        if node not in graph:
            end_nodes.add(node)
            continue

        for child in graph[node]:
            dp[child] -= dp[node]
            dp[child].add(node)

    print(len(end_nodes))
    print(*sorted(end_nodes))

    for node in sorted(topo):
        print(node, end=" ")
        print(len(dp[node]), end=" ")
        print(*dp[node])


def dfs(node, graph, visited, stack):
    if node in visited:
        return

    visited.add(node)

    if node in graph:
        for child in graph[node]:
            dfs(child, graph, visited, stack)

    stack.append(node)


if __name__ == "__main__":
    n = int(input().strip())
    nodes = set(input().strip().split())
    m = int(input().strip())
    edges = [input().strip().split() for i in range(m)]
    solution(n, nodes, m, edges)

# 조상을 완벽하게 기억하고 있다 => a가 b의 조상이면서 b가 a의 조상인 경우는 없다.
# 한 node가 여러 부모를 가질 수 있음 => DAG

# 각 노드의 조상이 주어짐

# 사람 이름 / 자식의 수 / 자식들의 이름


# 각 인물이 조상으로서 등장한 횟수 세기
# 서로 조상으로서 등장한 횟수 차이가 1인 경우,
# 부모 - 자식 관계
# 반례 => 부모가 여러 자식을 가지는 경우 횟수 차이가 1보다 더 클 수 있음


# 자손 - 조상 관계로 DAG 생성하기
# topologically ordered list로 변환한다면, 항상 자식(자손)가 부모(조상) 앞에 나옴
# dp = { node: set() for node in topo }
# for current in topo:
#   if current not in graph:
#     roots.add(current)
#   for parent in graph[current]
#     dp[parent] &= dp[current]
#     dp[parent].add(current)
# print(*sorted(roots)) # 시조들의 이름
# for node in topo:
#   print(node)
#   print(len(dp[node]))
#   print(sorted(dp[node]))


# 500_000_000.0
