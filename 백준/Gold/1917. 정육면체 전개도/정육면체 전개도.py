models = [
    [
        [0, 0, 1, 0],
        [1, 1, 1, 1,],
        [0, 0, 1, 0],
    ],
    [
        [0, 1, 0, 0],
        [1, 1, 1, 1,],
        [0, 0, 1, 0],
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 1],
    ],
    [
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
    ],
    [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 1],
        [1, 0, 0],
    ],
    [
        [0, 0, 1, 0],
        [0, 1, 1, 1],
        [1, 1, 0, 0],
    ],
    [
        [0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
    ],
    [
        [0, 0, 1, 1],
        [1, 1, 1, 0],
        [1, 0, 0, 0]
    ],
    [
        [0, 0, 1, 1],
        [0, 1, 1, 0],
        [1, 1, 0, 0],
    ]
]


def solution(matrix):
    n, m = len(matrix), len(matrix[0])

    shapes = []

    for model in models:
        model1 = model
        model2 = rotate(model1)
        model3 = rotate(model2)
        model4 = rotate(model3)

        flipped_model1 = flip(model)
        flipped_model2 = rotate(flipped_model1)
        flipped_model3 = rotate(flipped_model2)
        flipped_model4 = rotate(flipped_model3)

        for new_model in [model1, model2, model3, model4, flipped_model1, flipped_model2, flipped_model3, flipped_model4]:
            points = convert_to_points(new_model)
            shapes.append(points)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                for points in shapes:
                    if all([True if 0 <= i + point_x < n and 0 <= j + point_y < m and matrix[i + point_x][j + point_y] == 1 else False for point_x, point_y in points]):
                        return True

    return False


def rotate(model):
    n, m = len(model), len(model[0])

    new_model = [[0 for j in range(n)] for i in range(m)]
    # j 끝에 있는게 첫번째 i가 됌
    # i 끝에 있는게 마지막 j가 됌
    for i in range(n):
        for j in range(m):
            new_model[m - j - 1][i] = model[i][j]

    return new_model


def flip(model):
    n, m = len(model), len(model[0])

    new_model = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            new_model[n - i - 1][j] = model[i][j]
    return new_model


def convert_to_points(model):
    n, m = len(model), len(model[0])

    visited = set()

    for i in range(n):
        for j in range(m):
            if model[i][j] == 1:
                base_x, base_y = i, j
                dfs((i, j), model, visited)
                return [(x - base_x, y - base_y) for x, y in visited]


def dfs(current, model, visited):
    n, m = len(model), len(model[0])
    if current in visited:
        return

    x, y = current

    if not (0 <= x < n and 0 <= y < m):
        return

    if model[x][y] != 1:
        return

    visited.add(current)

    candidates = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

    for candidate in candidates:
        dfs(candidate, model, visited)


if __name__ == "__main__":
    t = 3
    for i in range(t):
        matrix = [[int(string) for string in input().split()]
                  for j in range(6)]
        answer = solution(matrix)
        if answer == True:
            print("yes")
        else:
            print("no")


# 2차원 배열에 정육면체 전개도 11개 저장
# 11개를 사방으로 돌리고, 뒤집은 다음에 다시 사방으로 돌린 것들 저장
# 11 * 6 * 6 * (4 + 4)
# 최상위, 좌측 좌표를 중심으로 상대 좌표 위치로 변환해서 저장
# 입력으로 주어진 이차원 배열을 위부터 순회하면서, 각 도형별로 좌표가 모두 매칭되는지 확인
# 완전히 맞는 게 있으면 True 반환, 없으면 False 반환
