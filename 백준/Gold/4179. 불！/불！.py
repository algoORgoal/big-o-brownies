from collections import deque


def solution(r, c, matrix):
    return bfs(r, c, matrix)


def bfs(r, c, matrix):

    root_fire_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "F":
                root_fire_points.append((i, j))
            elif matrix[i][j] == "J":
                root_player_point = (i, j)

    player_queue = deque()
    fire_queue = deque()

    player_queue.appendleft((root_player_point, 0))
    for root_fire_point in root_fire_points:
        fire_queue.appendleft((root_fire_point, 0))

    target_distance = 0

    while len(player_queue) > 0 or len(fire_queue) > 0:

        while len(fire_queue) > 0 and fire_queue[len(fire_queue) - 1][1] == target_distance:
            fire_point, fire_distance = fire_queue.pop()
            fire_x, fire_y = fire_point

            candidates = [(fire_x - 1, fire_y), (fire_x + 1, fire_y),
                          (fire_x, fire_y - 1), (fire_x, fire_y + 1)]

            for candidate in candidates:
                candidate_x, candidate_y = candidate
                if 0 <= candidate_x < r and 0 <= candidate_y < c:
                    if matrix[candidate_x][candidate_y] == "." or matrix[candidate_x][candidate_y] == "J":
                        matrix[candidate_x][candidate_y] = "F"
                        fire_queue.appendleft((candidate, fire_distance + 1))

        while len(player_queue) > 0 and player_queue[len(player_queue) - 1][1] == target_distance:
            player_point, player_distance = player_queue.pop()
            player_x, player_y = player_point

            if player_x == 0 or player_x == r - 1 or player_y == 0 or player_y == c - 1:
                return player_distance + 1

            candidates = [(player_x - 1, player_y), (player_x + 1, player_y),
                          (player_x, player_y - 1), (player_x, player_y + 1)]

            for candidate in candidates:
                candidate_x, candidate_y = candidate
                if 0 <= candidate_x < r and 0 <= candidate_y < c:
                    if matrix[candidate_x][candidate_y] == ".":
                        matrix[candidate_x][candidate_y] = "J"
                        player_queue.appendleft(
                            (candidate, player_distance + 1))

        target_distance += 1

    return "IMPOSSIBLE"


if __name__ == "__main__":
    r, c = [int(string) for string in input().split()]
    matrix = [[char for char in input()]for i in range(r)]
    answer = solution(r, c, matrix)
    print(answer)


# matrix edge node까지의 shortest path의 길이를 구해야 함
# 그와 동시에 해당 shortest path에 도착하는 순간 fire가 있지 않아야 함

# 각 cell에 누가 먼저 도달하는지 경쟁하는 bfs.
# 한 cell에 먼저 도달하는 순간, 절대 따라잡을 수 없음

# distance = 1일 동안:
# fire queue에서 모두 처리
# distance = 1일 동안:
# player queue에서 모두 처리
# distance = 2일 동안:
# fire queue에서 모두 처리

# 각 반복마다:
# 방문되지 않은 곳 방문 처리(. => F, . => J)
# 특히, player queue에서 edge에 도달했다면 distance 반환하기
# bfs가 모두 끝났다면 IMPOSSIBLE 반환하기


# 일종의 시뮬레이션
# 시간 n에서, 불이 n번만큼 덮쳤을 때 n번만큼 움직인 플레이어의 상태가 어디로 갈 수 있는지 계산
