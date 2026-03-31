from sys import stdin

input = stdin.readline


def solution(n, matrix):
    heart = find_heart(n, matrix)
    x, y = heart
    left_arm_start, right_arm_start, back_start = (
        x, y - 1), (x, y + 1), (x + 1, y)
    left_arm_length = calculate_part_length(matrix, left_arm_start, 0)
    right_arm_length = calculate_part_length(matrix, right_arm_start, 1)
    back_length = calculate_part_length(matrix, back_start, 2)
    back_end = back_start[0] + back_length - 1, back_start[1]
    left_leg_start = back_end[0] + 1, back_end[1] - 1
    right_leg_start = back_end[0] + 1, back_end[1] + 1
    left_leg_length = calculate_part_length(matrix, left_leg_start, 2)
    right_leg_length = calculate_part_length(matrix, right_leg_start, 2)
    return [[heart[0] + 1, heart[1] + 1], [left_arm_length, right_arm_length, back_length, left_leg_length, right_leg_length]]


def find_heart(n, matrix):
    for i in range(n):
        for j in range(n):
            nearby = (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
            if all([0 <= x < n and 0 <= y < n and matrix[x][y] == "*" for x, y in nearby]):
                return i, j


def calculate_part_length(matrix, start, direction):
    n = len(matrix)
    x, y = start
    length = 1
    if direction == 0:
        while 0 <= x < n and 0 <= y - 1 < n and matrix[x][y - 1] == "*":
            x, y = x, y - 1
            length += 1
    elif direction == 1:
        while 0 <= x < n and 0 <= y + 1 < n and matrix[x][y + 1] == "*":
            x, y = x, y + 1
            length += 1
    elif direction == 2:
        while 0 <= x + 1 < n and 0 <= y < n and matrix[x + 1][y] == "*":
            x, y = x + 1, y
            length += 1
    return length


if __name__ == "__main__":
    n = int(input().strip())
    matrix = [[char for char in input().strip()] for i in range(n)]
    answer = solution(n, matrix)
    heart, lengths = answer

    for index, value in enumerate(heart):
        if index == len(heart) - 1:
            print(value, end="\n")
        else:
            print(value, end=" ")

    for index, length in enumerate(lengths):
        if index == len(lengths) - 1:
            print(length, end="\n")
        else:
            print(length, end=" ")

# 심장 찾기: 사방에 *가 있음
# 심장을 기준으로 왼쪽=> 왼쪽 팔, 오른쪽, 오른쪽 팔, 아래 => 허리
# 허리 끝 좌표 계산하기
# 허리 끝 좌표 기준으로 왼쪽 아래 => 왼쪽 다리, 오른쪽 아래 => 오른쪽 다리
# 길이 계산 완료
# 시간복잡도 O(n ** 2)
# 공간복잡도 O(n ** 2)
