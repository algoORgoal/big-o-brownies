# 일단 모든 경우의 수를 계산하는 경우
# 한번 때릴 때마다 6번의 경우의 수가 나온다
# 60 60 60을 까기 위해서 최소한 9 3 1
# 180 / 13 = 13.8 = 13.8
# 6 ** 14 = 78_364_164_096

# 특정 체력에 도달하기 위해서, 공격하는 순서가 중요하지 않다
# 9 3 1 => 1 3 9로 때리나, 1 3 9 => 9 3 1로 때리나 남은 체력은 동일함
# 때리는 순서가 상태에서 중요한 게 아님, 왜냐하면 공격 횟수가 동일하기 때문

# 현재 상태: a b c => 목표 상태: 0 0 0(0 이하로 떨어지는 경우 전부 0으로 침)
# 여러 갈래를 통해서 a b c => 0 0 0으로 갈 수 있는데, 두 노드간의 최단거리를 구하는 것이 목표이다. (그래프)
# 최단거리를 구하기 위해서 무슨 전략을 쓸 수 있는가? 엣지의 weight가 같으면 BFS / 다르면 다익스트라
# 근데, 현재 상황에서는 각 상태로 갈 때 공격 한번만 쓰기 때문에 엣지 weight가 같다고 볼 수 있다.
# 따라서, bfs를 통해서 정답을 찾을 수 있다.
# 다만, 이미 방문한 상태 같은 경우 (1체력, 2체력, 3체력) 이전에 방문한 거리가 최단거리이기 때문에, 다시 방문했을 때 바로 버릴 수 있다는 것을 알 수 있다.
# 따라서 visited로 관리 가능

from itertools import permutations
from collections import deque


def solution(health_points):
    return bfs(health_points)


def bfs(initial_health_points, visited={}):
    queue = deque()
    queue.append(initial_health_points)
    visited[tuple(initial_health_points)] = 0
    attack_points = [9, 3, 1][0:len(initial_health_points)]
    while len(queue) > 0:
        current_health_points = queue.popleft()
        perms = permutations(attack_points, len(initial_health_points))
        for perm in perms:
            minus_health_points = [
                current_health_points[i] - perm[i] for i in range(0, len(perm))]
            left_health_points = [health_point if health_point >
                                  0 else 0 for health_point in minus_health_points]
            if tuple(left_health_points) in visited:
                continue
            visited[tuple(left_health_points)] = visited[tuple(
                current_health_points)] + 1
            queue.append(left_health_points)
    return visited[tuple([0 for i in initial_health_points])]


if __name__ == "__main__":
    count = int(input())
    health_points = [int(i) for i in input().split()]
    answer = solution(health_points)
    print(answer)
