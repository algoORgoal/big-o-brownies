from collections import deque
from math import inf


def solution(n, k):
    return bfs(n, set(), k)


def bfs(root, visited, target):
    queue = deque()

    # 거리가 같은 노드를 모두 구함
    node = root
    while node not in visited and 0 <= node <= 200_000:
        visited.add(node)
        queue.appendleft((node, 0))
        node *= 2

    while len(queue) > 0:
        current, distance = queue.pop()

        if current == target:
            return distance

        candidates = [current - 1, current + 1]

        for candidate in candidates:
            while (candidate not in visited) and 0 <= candidate <= 200_000:
                visited.add(candidate)
                queue.appendleft((candidate, distance + 1))
                candidate *= 2

    return inf


if __name__ == "__main__":
    n, k = [int(i) for i in input().split(' ')]
    answer = solution(n, k)
    print(answer)


# bfs를 통해 노드간의 최단경로를 구할 수 있다.
# 근데, 간선간의 거리가 동일하지 않다.
# path 길이가 아니라 weight 합을 구해야하므로 bfs는 적절하지 않다.
# 트릭: 루트 노드를 여러개 사용한다. 2의 배수가 되는 노드들인 전부 루트노드
# 반레: 중간에 - 또는 +를 하다가, * 2를 해서 최적이 되는 경우도 있다
# 해결방법: 각 노드마다 * 2되는 것들도 같이 거리를 기록한다.

# 다익스트라 알고리즘도 비효율적이다. O(v ** 2) v <= 100,000 -> 10억이므로 시간초과한다.

# 다른 해결 방법
# 각 노드마다, * 2 되는 것들도 같이 거리를 기록한다.
# visited되면 stop. 그 이후의 것들도 전부 방문된 것.
# * 2 되는 모든 노드들도 같이 -1, +1되는 노드를 push한다.

# 100 = 2 ** 2 * 5 ** 2
# 98 = 49 * 2
# 1 => 2 =>

# 0 <= candidate <= 100_000
# O(2n) = O(n)
