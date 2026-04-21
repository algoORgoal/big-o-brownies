from sys import setrecursionlimit

setrecursionlimit(1_000 ** 2)


def solution(n, m, sequences):
    edges = set()
    for sequence in sequences:
        for i in range(len(sequence)):
            for j in range(i + 1, len(sequence)):
                start, end = sequence[i], sequence[j]
                edges.add((start, end))

    nodes = {i for i in range(1, n + 1)}
    graph = {node: [] for node in nodes}
    for start, end in edges:
        graph[start].append(end)

    visited = set()

    if any([has_cycle(node, graph, visited, set()) for node in nodes]):
        return 0

    visited = set()
    stack = []

    for node in nodes:
        topological_sort(node, graph, visited, stack)

    topo = stack[::-1]

    return topo


def has_cycle(current, graph, visited, route):
    if current in route:
        return True

    if current in visited:
        return False

    route.add(current)
    visited.add(current)

    if current in graph:
        for adjacent_node in graph[current]:
            if has_cycle(adjacent_node, graph, visited, route) == True:
                return True

    route.remove(current)

    return False


def topological_sort(current, graph, visited, stack):
    if current in visited:
        return

    visited.add(current)

    if current in graph:
        for adjacent_node in graph[current]:
            topological_sort(adjacent_node, graph, visited, stack)

    stack.append(current)


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    sequences = [[int(string) for string in input().split()][1:]
                 for i in range(m)]
    answer = solution(n, m, sequences)
    if answer == 0:
        print(answer)
    else:
        for num in answer:
            print(num)

# 노드간에 선후 관계가 있음
# 위상정렬로 해결 가능
# 1. sequences 분해해서 edge로 만들기
# 1. directed graph 생성하기
# 2. directed graph에 사이클 있는지 확인하기
# 3. 사이클 있으면 0 반환, 없으면 topological order 반환

# 시간복잡도 O(n + m) (m <= n(n-1)/2)
# 공간복잡도 O(n + m) (m <= n(n-1)/2)


# 4,3 / 3,2 / 2,4 => 사이클 생성되므로 줄세우기 불가능 => 0 출력
