

def atonum(a):
    return 2 ** (ord(a) - ord('A'))


def solution(r, c, matrix):
    return dfs((0, 0), matrix, atonum(matrix[0][0]), r, c, {}) + 1


def dfs(current, matrix, visited, r, c, table):
    if (current, visited) in table:
        return table[current, visited]

    x, y = current

    candidates = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

    max_distance = 0

    for candidate in candidates:
        candidate_x, candidate_y = candidate
        if 0 <= candidate_x < r and 0 <= candidate_y < c:
            num = atonum(matrix[candidate_x][candidate_y])
            if visited & num != 0:
                continue
            max_distance = max(
                dfs(candidate, matrix, visited | num, r, c, table) + 1, max_distance)

    table[current, visited] = max_distance
    return table[current, visited]


if __name__ == "__main__":
    r, c = [int(string) for string in input().split()]
    matrix = [[string for string in input()] for i in range(r)]
    answer = solution(r, c, matrix)
    print(answer)


# player는 A부터 Z를 한번만 방문 가능
# 탐색공간은 tree로 표현 가능하며, depth는 26까지만 가능
# 상, 하, 좌, 우 (반드시 한 방향은 이미 방문) => 3 ** 25 = 1125899906842624


# 백트래킹을 통해서, 특정 branch로 갔을 때 얼마나 방문할 수 있는지 최대값을 방문함.
# 필요한 상태: current, matrix, visited

# depth: 25
# branch가 생길 확률: 각 방향에 선택한 문자의 개수
# n가 depth이면, branch 개수 4 * ( (26 - n) /26)

# 1가 depth이면, 해당 노드의 branch 개수 4 * ( (26 - 1) /26)
# 2가 depth이면, 4 * ( (26 - 2) /26)
# 3가 depth이면, 4 * ( (26 - 3) /26)
# 4가 depth이면, 4 * ( (26 - 4) /26)
# 3가 depth이면, 4 * ( (26 - 5) /26)

# def complexity(n):ㄷ
#     if n == 26:
#         return 1
#     b = (4 * ((26 - n) / 26))
#     return 1 + b * complexity(n + 1)

# 49_059_813.42308704
# 평균 노드 개수 5천만개 => 쌉가능

# 다른 방법: 각각의 route가 어떤 알파벳을 방문하는지 확인 => 반환
