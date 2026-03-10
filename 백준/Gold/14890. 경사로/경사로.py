

def solution(matrix, n, l):
    rotated_matrix = rotate_matrix(matrix, n)
    return count_road(matrix, n, l) + count_road(rotated_matrix, n, l)


def rotate_matrix(matrix, n):
    rotated_matrix = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[n - 1 - j][i] = matrix[i][j]

    return rotated_matrix


def count_road(matrix, n, l):
    reversed_matrix = reverse_matrix(matrix, n)
    used1, passed1 = check_available(matrix, n, l)
    used2, passed2 = check_available(reversed_matrix, n, l)

    count = 0

    for i in range(n):
        for j in range(n):
            # 경사로 겹치게 설치해야 지나갈 수 있는 상태가 되는 경우 => 지나갈 수 없음
            if used1[i][j] == True and used2[i][n - 1 - j] == True:
                passed1[i] = False
                passed2[i] = False
                break
        if passed1[i] == True and passed2[i] == True:
            count += 1

    return count


def check_available(matrix, n, l):
    last = None
    used = [[False for j in range(n)] for i in range(n)]
    passed = [False for i in range(n)]

    i = 0
    while i < n:
        j = 0
        while j < n:
            current = matrix[i][j]
            if last != None:
                if last - current > 1:
                    break
                elif last - current == 1:
                    # l 길이의 경사로로 커버 가능, 높이 균일
                    if all([j + k < n and matrix[i][j + k] == current for k in range(l)]):
                        for k in range(l):
                            used[i][j + k] = True
                        last = matrix[i][j + l - 1]
                        j += l
                        continue
                    else:
                        break

            last = current
            j += 1

        if j == n:
            passed[i] = True

        i += 1
        last = None

    return used, passed


def reverse_matrix(matrix, n):
    reversed_matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            reversed_matrix[i][n - 1 - j] = matrix[i][j]

    return reversed_matrix


if __name__ == "__main__":
    n, l = [int(string) for string in input().split()]
    matrix = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(matrix, n, l)
    print(answer)


# 1. last - current > 1 => 불가능
# 2. last - current == 0 => continue
# 3. last - current == 1 => x ~ x + l - 1이 current인지 확인
# 끝에 도달, reverse 시켰을 때도 끝에 도달하면서, 두 과정에서 경사 설치 영역 겹치지 않으면 길 하나 추가
#
