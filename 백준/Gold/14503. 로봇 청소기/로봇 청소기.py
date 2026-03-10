
def solution(size, initial_point, d, matrix):
    n, m = size
    point = initial_point
    direction = d

    count = 0
    while True:
        x, y = point
        if matrix[x][y] == 0:
            count += 1
            matrix[x][y] = 2

        candidates = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

        if any([0 <= candidate_x < n and 0 <= candidate_y < m and matrix[candidate_x][candidate_y] == 0 for candidate_x, candidate_y in candidates]):
            direction = (direction - 1) if direction > 0 else 3
            next_x, next_y = resolve_next_point(point, direction)

            if 0 <= next_x < n and 0 <= next_y < m and matrix[next_x][next_y] == 0:
                point = next_x, next_y
        else:
            back_x, back_y = resolve_back_point(point, direction)
            if 0 <= back_x < n and 0 <= back_y < m and matrix[back_x][back_y] != 1:
                point = back_x, back_y
            else:
                break

    return count


def resolve_next_point(point, direction):
    x, y = point
    # 북 동 남 서
    if direction == 0:
        return x - 1, y
    if direction == 1:
        return x, y + 1
    if direction == 2:
        return x + 1, y
    else:
        return x, y - 1


def resolve_back_point(point, direction):
    x, y = point
    # 북 동 남 서
    if direction == 0:
        return x + 1, y
    if direction == 1:
        return x, y - 1
    if direction == 2:
        return x - 1, y
    else:
        return x, y + 1


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    r, c, d = [int(string) for string in input().split()]
    matrix = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution((n, m), (r, c), d, matrix)
    print(answer)


# 상태
# 현재 청소기의 좌표 (x, y)
# 현재 청소기의 방향 d
