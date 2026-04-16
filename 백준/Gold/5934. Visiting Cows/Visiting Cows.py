def solution(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for vertex1, vertex2 in edges:
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    return max(dfs(1, graph, set([1])))


def dfs(current, graph, visited):

    count_included, count_excluded = 1, 0

    if current not in graph:
        return count_included, count_excluded

    for adjacent_node in graph[current]:
        if adjacent_node in visited:
            continue

        visited.add(adjacent_node)
        count_child_included, count_child_excluded = dfs(
            adjacent_node, graph, visited)
        count_included += count_child_excluded
        count_excluded += max(count_child_included, count_child_excluded)

    return count_included, count_excluded


if __name__ == "__main__":
    n = int(input())
    edges = [[int(string) for string in input().split()] for i in range(n - 1)]
    answer = solution(n, edges)
    print(answer)

# 노드 n개, edge n - 1개가 서로 연결 => 트리
# dfs 수행
# 각각마다 계산해야할 것: 자신을 포함하지 않을 때 서브트리 최대 노드 개수, 자신을 포함할 때 서브트리 최대 노드 개수
# 시간복잡도: O(n)

# 틀린 부분: 자신을 포함하지 않을 때는, 자식을 포함하지 않거나 포함한 경우 둘 다 가능함

# dfs 상태
# 현재 노드, graph, visited
