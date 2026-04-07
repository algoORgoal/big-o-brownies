from sys import setrecursionlimit

setrecursionlimit(50 * 50)


def solution(n, l, r, matrix):
    should_stop = True
    round_count = 0

    while True:
        # 각 round마다 방문되는 좌표 모음
        round_visited = set()
        for i in range(n):
            for j in range(n):
                if (i, j) in round_visited:
                    continue

                round_visited.add((i, j))

                path = []

                sum, node_count = dfs(
                    (i, j), matrix, round_visited, l, r, path)

                average = sum // node_count

                for x, y in path:
                    matrix[x][y] = average

                if len(path) > 1:
                    should_stop = False

        if should_stop == True:
            break
        else:
            round_count += 1
            should_stop = True

    return round_count


def dfs(current, matrix, visited, lower_bound, upper_bound, path):
    n = len(matrix)
    x, y = current

    path.append((x, y))

    candidates = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

    sum, node_count = matrix[x][y], 1

    for candidate in candidates:
        candidate_x, candidate_y = candidate
        if not (0 <= candidate_x < n and 0 <= candidate_y < n):
            continue
        if candidate in visited:
            continue
        difference = abs(
            matrix[x][y] - matrix[candidate_x][candidate_y])
        if not (lower_bound <= difference <= upper_bound):
            continue

        visited.add(candidate)
        partial_sum, partial_node_count = dfs(
            candidate, matrix, visited, lower_bound, upper_bound, path)

        sum += partial_sum
        node_count += partial_node_count

    return sum, node_count


if __name__ == "__main__":
    n, l, r = [int(string) for string in input().split()]
    matrix = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, l, r, matrix)
    print(answer)


# 2차원 배열에 대해:

# dfs를 두번 실행하기
# 1번: dfs를 돌려서 방문하는 노드의 개수, node value의 합 구하기
# (node value 합) // 노드의 개수 구하기
# 2번: dfs를 돌려서 평균 값으로 할당하기


# 인구이동 일 수 2000번 이하 =>
# 2000 * n ** 2
# 2000 * 2500 = 5_000_000
