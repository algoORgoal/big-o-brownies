from sys import stdin
from sys import stdout

input = stdin.readline


def print(string, end="\n"):
    stdout.write(f"{string}{end}")


def solution(n, heights):
    table = {i: 0 for i in range(n)}
    left = {}
    right = {}

    stack = []
    for i, height in enumerate(heights):
        while len(stack) > 0 and stack[len(stack) - 1][0] <= height:
            stack.pop()

        if len(stack) > 0:
            table[i] += len(stack)
            left[i] = stack[len(stack) - 1][1]

        stack.append((height, i))

    stack = []
    for i in range(len(heights) - 1, -1, -1):
        height = heights[i]
        while len(stack) > 0 and stack[len(stack) - 1][0] <= height:
            stack.pop()

        if len(stack) > 0:
            table[i] += len(stack)
            right[i] = stack[len(stack) - 1][1]

        stack.append((height, i))

    answer = []
    for i in table:
        if table[i] == 0:
            answer.append([table[i]])
        else:
            if i in left and i in right:
                # 거리가 가장 가까운 것 중에서 번호가 작은 것
                if abs(left[i] - i) <= abs(right[i] - i):
                    answer.append([table[i], left[i] + 1])
                else:
                    answer.append([table[i], right[i] + 1])
            elif i in left:
                answer.append([table[i], left[i] + 1])
            else:
                answer.append([table[i], right[i] + 1])

    return answer


if __name__ == "__main__":
    n = int(input().strip())
    heights = [int(string) for string in input().strip().split()]
    answer = solution(n, heights)
    for row in answer:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print(num, end="\n")
            else:
                print(num, end=" ")


# 각 건물별로 높이 탐색 => O(n ** 2) n <= 10 ** 5
# n ** 2 <= 10 ** 10 = 10_000_000_000 => TLE

# 왼쪽 방향에서 볼 수 있는 건물, 오른쪽 방향에서 볼 수 있는 건물 따로 계산

# while len(stack) > 0 and stack[len(stack) - 1] <= heights[i]:
#   stack.pop()
# table[i] = len(stack)  every stack[i] > heights[i]
# stack.append(heights[i])

# 시간복잡도 O(n)
# 공간복잡도 O(n)
