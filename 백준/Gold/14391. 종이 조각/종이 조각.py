from collections import deque
from math import inf


def solution(n, m, matrix):
    return dfs((0, 0), matrix, dict())


def calculate_score(matrix, table):
    visited = set()

    height, width = len(matrix), len(matrix[0])

    sum = 0
    for i in range(height - 1, -1, - 1):
        for j in range(width - 1, -1, - 1):
            queue = deque()
            current = i, j
            if current in visited:
                continue

            visited.add(current)

            queue.appendleft(current)

            # 테이블에 없는 경우 => 1 * 1 cell
            # 테이블에 있는 경우 => (0,0)될 때까지 탐색
            while current in table and table[current] != (0, 0):
                next = current[0] - \
                    table[current][0], current[1] - table[current][1]
                queue.appendleft(next)
                visited.add(next)
                current = next
            str_num = ""
            for x, y in queue:
                str_num += str(matrix[x][y])

            sum += int(str_num)

    return sum


def dfs(current, matrix, table):

    height, width = len(matrix), len(matrix[0])
    x, y = current

    if x >= height or y >= width:
        return calculate_score(matrix, table)

    next = (x + 1, 0) if y == width - 1 else (x, y + 1)

    sum = -inf

    sum = max(dfs(next, matrix, table), sum)

    candidates = (x - 1, y), (x, y - 1)
    # (x - 1, y)와 (x, y)를 한 직사각형에 배치하는 경우
    # (x, y - 1)와 (x, y)를 한 직사각형에 배치하는 경우
    # 1 * 1 직사각형으로 배치하는 경우

    for candidate in candidates:
        candidate_x, candidate_y = candidate

        if 0 <= candidate_x < height and 0 <= candidate_y < width:
            t = (x - candidate_x, y - candidate_y)
            # 방향이 동일하거나, 합쳐지지 않음
            if candidate not in table or (candidate in table and table[candidate] == t):
                if candidate not in table:
                    table[candidate] = (0, 0)
                    table[current] = t  # key: 자식, value: 부모
                    sum = max(dfs(next, matrix, table), sum)
                    table.pop(candidate)
                    table.pop(current)
                else:
                    table[current] = t  # key: 자식, value: 부모
                    sum = max(dfs(next, matrix, table), sum)
                    table.pop(current)

    return sum


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    matrix = [[int(char) for char in input()]
              for i in range(0, n)]
    answer = solution(n, m, matrix)
    print(answer)


# 1. start state
# 2. ends state
# 3. transition function
# 4. alphabet
# 5. a set of states


# (좌표), (연결된 이전 좌표 방향성)
# 문제: 1 * 1짜리랑, 직사각형의 시작 부분이랑 구분이 안 된다.
#      그래서 주변 좌표 기준으로 해당 좌표로 연결이 되는지 안 되는지 확인이 불가능하다.
# 해결 방법:
# 1. 아예 사용이 안 됐다 => table에 담지 않기
# 2. 사용이 됐다 => table에 담기 (0, 0)
#    이미 직사각형의 시작 부분으로 사용이 되었으면 연결하지 않음 (0, 0)
