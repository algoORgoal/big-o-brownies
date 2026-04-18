def solution(n, m, edges):
    graph = {}
    for child, parent, weight in edges:
        if parent not in graph:
            graph[parent] = []
        graph[parent].append((child, weight))

    stack = []

    nodes = set()
    root_nodes = set()

    for parent in graph:
        root_nodes.add(parent)

    for parent in graph:
        nodes.add(parent)
        for child, weight in graph[parent]:
            nodes.add(child)
            root_nodes.discard(child)

    visited = set()
    for node in nodes:
        dfs(node, graph, visited, stack)

    topo = stack[::-1]

    dp = {node: {} for node in topo}

    for root_node in root_nodes:
        dp[root_node][root_node] = 1

    for node in topo:
        if node not in graph:
            continue

        for child, weight in graph[node]:
            for root_node in dp[node]:
                if root_node not in dp[child]:
                    dp[child][root_node] = 0
                dp[child][root_node] += dp[node][root_node] * weight

    return sorted([(root_node, dp[n][root_node])for root_node in dp[n]])


def dfs(current, graph, visited, stack):
    if current in visited:
        return

    visited.add(current)

    if current in graph:
        for child, weight in graph[current]:
            dfs(child, graph, visited, stack)

    stack.append(current)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    edges = [[int(string) for string in input().split()]for i in range(m)]
    answer = solution(n, m, edges)
    for row in answer:
        print(*row)

# x, y, z
# [y]: [(x, z)]

# 기본 부품: indegree가 0인 노드
# 중간 부붐: indegree가 1 이상인 노드
# 최종 부품: outdegree가 0인 노드

# 두 중간 부품이 서로를 필요로 하는 경우 없음 => 사이클 없음
# DAG로 모델링 가능

# 1. 위상정렬를 통해 topology 구하기
#    dp = { node: {} for node in nodes}
# 2. for node in topo:
#      if node not in graph:
#        continue
#      for child in graph[node]:
#        for grandparent in dp[node]:
#          dp[child][grandparent] = dp[node][grandparent] * weight
#
# m의 개수: 100개
# n의 개수: 100개

# 시간복잡도: O(nm)
# 공간복잡도: O(nm)
