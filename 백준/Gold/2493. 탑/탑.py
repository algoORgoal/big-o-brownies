from sys import stdin
from sys import stdout

input = stdin.readline


def solution(n, arr):
    order_arr = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        num = arr[i]

        if len(stack) == 0 or num < stack[len(stack) - 1][1]:
            stack.append((i, num))
        else:
            while len(stack) > 0 and num > stack[len(stack) - 1][1]:
                top_index, top_num = stack.pop()
                order_arr[top_index] = i

            stack.append((i, num))

    for i in range(n):
        order_arr[i] += 1

    return order_arr


def print(string="", end="\n"):
    stdout.write(f"{string}{end}")


if __name__ == "__main__":
    n = int(input())
    arr = [int(string) for string in input().strip().split()]
    answer = solution(n, arr)
    for index, num in enumerate(answer):
        if index < len(answer) - 1:
            print(num, end=" ")
        else:
            print(num, end="")
# 거꾸로 순서로 순회, stack 유지
# top보다 더 작은 숫자가 들어온다 => 쌓기 (push)
# top보다 더 큰 숫자가 들어올 때까지: pop시켜버리면서 해당 인덱스에 부서뜨린 놈의 current의 index 기록

# 1_000_000 => 8 byte * 1_000_000 = 8mb
