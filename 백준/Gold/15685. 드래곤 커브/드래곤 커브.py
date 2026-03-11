

def solution(n, curves):
    matrix = [[False for j in range(101)] for i in range(101)]

    for x, y, d, g in curves:
        point = x, y
        matrix[x][y] = True
        path = create_path(x, y, d, g)
        for direction in path:
            x, y = move(point, direction)
            matrix[x][y] = True

            point = x, y

    count = 0
    for i in range(100):
        for j in range(100):
            if matrix[i][j] == True and matrix[i + 1][j] == True and matrix[i][j + 1] == True and matrix[i + 1][j + 1] == True:
                count += 1

    return count


def create_path(x, y, d, g):
    right_table = create_table([0], {})
    up_table = create_table([1], {})
    left_table = create_table([2], {})
    down_table = create_table([3], {})

    if d == 0:
        path = right_table[g]
    elif d == 1:
        path = up_table[g]
    elif d == 2:
        path = left_table[g]
    else:
        path = down_table[g]

    return path


def move(point, direction):
    x,  y = point
    if direction == 0:
        return x + 1, y
    if direction == 1:
        return x, y - 1
    if direction == 2:
        return x - 1, y
    else:
        return x, y + 1


def create_table(initial_path, table):
    table[0] = initial_path
    for i in range(1, 11):
        table[i] = table[i - 1] + [spin(i) for i in reversed(table[i - 1])]

    return table


def spin(direction):
    if direction == 3:
        return 0
    return direction + 1


if __name__ == "__main__":
    n = int(input())
    curves = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, curves)
    print(answer)


# n 세대를 만드는 경우,
# 1. n - 1 세대의 경로를 뒤집음
# 2. 반시계 방향으로 회전시킨 경로를 n - 1 세대에 추가함

# 시작점을 기준으로, 경로에 적힌 방향으로 이동하면서 fill

# 시작 방향에 따라 경로 각각 캐싱

# 100 * 100에서 filled된 square 구하기
