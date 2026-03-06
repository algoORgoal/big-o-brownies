from sys import stdin
from sys import stdout

input = stdin.readline


def print(s, end="\n"):
    stdout.write(f"{s}{end}")


def solution(n, m, r, matrix):
    return get_moved_matrix(matrix, r, n, m)


def get_moved_matrix(matrix, r, n, m):
    new_matrix = [[0 for j in range(0, m)] for i in range(0, n)]
    point = [0, 0]
    start_point = [0, 0]
    end_point = [n - 1, m - 1]

    while start_point[0] < end_point[0] and start_point[1] < end_point[1]:
        radius = (end_point[0] - start_point[0] + 1) * (end_point[1] - start_point[1] + 1) - (
            end_point[0] - start_point[0] - 1) * (end_point[1] - start_point[1] - 1)

        moved_point = list(point)
        for i in range(r % radius):
            moved_point = get_next_point(moved_point, start_point, end_point)

        for i in range(0, radius):
            x, y = point
            moved_x, moved_y = moved_point

            new_matrix[moved_x][moved_y] = matrix[x][y]
            point = get_next_point(point, start_point, end_point)
            moved_point = get_next_point(moved_point, start_point, end_point)

        point[0] += 1
        point[1] += 1
        start_point[0] += 1
        start_point[1] += 1
        end_point[0] -= 1
        end_point[1] -= 1
    return new_matrix


def get_next_point(point, start_point, end_point):
    x, y = point
    start_x, start_y = start_point
    end_x, end_y = end_point

    if y == start_y and start_x <= x < end_x:
        x += 1
    elif x == end_x and start_y <= y < end_y:
        y += 1
    elif y == end_y and start_x < x <= end_x:
        x -= 1
    elif x == start_x and start_y < y <= end_y:
        y -= 1

    return [x, y]


def fill(point, start_point, end_point, matrix):
    x, y = point
    start_x, start_y = start_point
    end_x, end_y = end_point
    if not (start_x < end_x and start_y < end_y):
        return

    next_point = []
    if y == start_y and start_x <= x < end_x:
        next_point = x + 1, y
    elif x == end_x and start_y <= y < end_y:
        next_point = x, y + 1
    elif y == end_y and start_x < x <= end_x:
        next_point = x - 1, y
    elif x == start_x and start_y < y <= end_y:
        next_point = x, y - 1

    next_x, next_y = next_point

    value = matrix[x][y]
    if not (x == start_x and y == start_y + 1):
        fill(next_point, start_point, end_point, matrix)
    matrix[next_x][next_y] = value


if __name__ == "__main__":
    n, m, r = [int(string) for string in input().split()]
    matrix = [[int(string) for string in input().split()] for i in range(0, n)]
    answer = solution(n, m, r, matrix)
    for i in range(0, len(answer)):
        for j in range(0, len(answer[i])):
            if j == len(answer[i]) - 1:
                print(answer[i][j], end="\n")
            else:
                print(answer[i][j], end=" ")


# n * m * r
# 1. 연산 r 수행할 때마다,
# 2. 새로운 matrix인 new_matrix 만들기. 회전되는 부분 채워넣기
# 시간복잡도: O(n * m * r)
# 공간복잡도: O(n * m)
# 300 * 300 * 1000 = 90_000 000

# 문제: 시간초과
# 추정 원인: 배열을 너무 많이 생성한 것으로 추청
# 해결 방법: 배열 재사용: value를 기억했다가 재귀 끝났을 때 업데이트

# 시간복잡도: O(n * m * (r % radius))
# 공간복잡도: O(nm)
# radius: worse case에 크기 (300 + 300) * 2 - 4 = 1196 > r
# 시간복잡도를 유의미하게 줄여주지 않는다.
# n <= 300, m <= 300, r <= 1000 => nmr <= 90_000_000
# nmr primitive operation이 리스트 생성, 조건문에 따른 처리라서 시간초과 발생
# 시간복잡도 O(nm)으로 만드는 법
# 시작점의 이동하는 곳을 확정하고, 거기로 할당
#
