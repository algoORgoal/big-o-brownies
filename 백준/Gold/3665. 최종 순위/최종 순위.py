from sys import setrecursionlimit

setrecursionlimit(500 ** 2)


def solution(n, previous_rank, m, switched_pairs):
    edges = set()
    for i in range(len(previous_rank)):
        for j in range(i + 1, len(previous_rank)):
            vertex1, vertex2 = previous_rank[i], previous_rank[j]
            edges.add((vertex1, vertex2))

    for vertex1, vertex2 in switched_pairs:
        if (vertex2, vertex1) in edges:
            edges.remove((vertex2, vertex1))
            edges.add((vertex1, vertex2))
        else:
            edges.remove((vertex1, vertex2))
            edges.add((vertex2, vertex1))

    directed_graph = {}
    for start, end in edges:
        if start not in directed_graph:
            directed_graph[start] = []
        directed_graph[start].append(end)

    if has_cycle(directed_graph):
        return "IMPOSSIBLE"

    topo = topological_sort(directed_graph)
    team_to_rank = {}

    for node in topo:
        if node not in directed_graph:
            continue

        if node not in team_to_rank:
            team_to_rank[node] = 1

        for child in directed_graph[node]:
            team_to_rank[child] = team_to_rank[node] + 1

    rank_to_teams = {}
    for team in team_to_rank:
        if team_to_rank[team] not in rank_to_teams:
            rank_to_teams[team_to_rank[team]] = []
        rank_to_teams[team_to_rank[team]].append(team)

    new_rank = []
    for i in range(1, n + 1):
        if i in rank_to_teams:
            if len(rank_to_teams[i]) == 1:
                new_rank.append(rank_to_teams[i][0])
            else:
                for j in range(len(rank_to_teams[i])):
                    new_rank.append('?')

    return new_rank


def has_cycle(directed_graph):
    nodes = set()
    for node in directed_graph:
        nodes.add(node)
        for adjacent_node in directed_graph[node]:
            nodes.add(adjacent_node)

    visited = set()
    for node in nodes:
        if dfs1(node, directed_graph, visited, set()) == True:
            return True

    return False


def topological_sort(directed_graph):
    nodes = set()
    for node in directed_graph:
        nodes.add(node)
        for adjacent_node in directed_graph[node]:
            nodes.add(adjacent_node)

    stack = []
    visited = set()

    for node in nodes:
        dfs2(node, directed_graph, visited, stack)

    return stack[::-1]


def dfs1(node, directed_graph, visited, route):
    if node in route:
        return True

    if node in visited:
        return False

    visited.add(node)
    route.add(node)

    if node in directed_graph:
        for adjacent_node in directed_graph[node]:
            if dfs1(adjacent_node, directed_graph, visited, route) == True:
                return True

    route.remove(node)
    return False


def dfs2(node, directed_graph, visited, stack):
    if node in visited:
        return

    visited.add(node)

    if node in directed_graph:
        for adjacent_node in directed_graph[node]:
            dfs2(adjacent_node, directed_graph, visited, stack)

    stack.append(node)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        previous_rank = [int(string) for string in input().split()]
        m = int(input())
        switched_pairs = [[int(string)
                           for string in input().split()] for i in range(m)]
        answer = solution(n, previous_rank, m, switched_pairs)
        if answer == "IMPOSSIBLE":
            print(answer)
        else:
            print(*answer)


# 1. 가능한 directed edge 정보 모두 수집하기
# 2. connected directed graph 만들기
# 3. cycle 탐지하기 => 있는 경우 impossible 반환하기
# 4. topological sort로 topological order 만들기
# 5. 순위 매기기(부모 + 1)
# 6. 순위 순으로 정렬하기, rank 동일한 것들은 ?로 대체하기

# 시간복잡도: O(m) = O(n ** 2) (n <= 500)
# 공간복잡도: O(n + m) = O(n ** 2)
