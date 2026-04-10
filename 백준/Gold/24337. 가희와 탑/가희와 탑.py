from collections import deque


def solution(n, a, b):
    if a + b > n + 1:
        return -1

    queue = deque()

    if a >= b:
        for i in range(1, a + 1):
            queue.append(i)
        for i in range(b - 1, 0, -1):
            queue.append(i)
    else:
        for i in range(1, b + 1):
            queue.appendleft(i)
        for i in range(a - 1, 0, -1):
            queue.appendleft(i)

    rest_count = n - (a + b - 1)

    if a == 1:
        # a = 1일 경우, 1을 앞에 채워넣을 수 없음
        # 가장 큰 요소 다음에 1을 채워넣는 게 답
        top = queue.popleft()
        for i in range(rest_count):
            queue.appendleft(1)
        queue.appendleft(top)
    else:
        for i in range(rest_count):
            queue.appendleft(1)

    return queue


if __name__ == "__main__":
    n, a, b = [int(string) for string in input().split()]
    answer = solution(n, a, b)
    if answer == -1:
        print(answer)
    else:
        for i, num in enumerate(answer):
            if i == len(answer) - 1:
                print(num, end="\n")
            else:
                print(num, end=" ")


# 무조건 안 되는 것: a + b > n + 1
# n = 5, a = 3, b = 3
# 1 2 3 2 1

# n = 4, a = 3, b = 1
# 1 1 2 3

# n = 4, a = 3, b = 2
# 1 2 3 1

# n = 4, a = 1, b = 1
# 1 1 1 1

# n = 5, a = 2, b = 2
# 1 1 1 2 1

# n = 5, a = 2, b = 3
# 1 1 3 2 1

# n = 6, a = 3, b = 3
# 1 1 2 3 2 1

# n = 6,  a = 3, b = 4
# 1 2 4 3 2 1

# n = 6, a = 2, b = 2
# 1 1 1 1 2 1

# n = 6, a = 2, b = 1
# 1 1 1 1 1 2

# n = 6, a = 1, b = 2
# 2 1 1 1 1 1 x

# n = 6, a = 4, b = 1
# 1 1 1 2 3 4

# n = 6, a = 1, b = 4
# 1 1 4 3 2 1

# n = 10, a = 3, b = 5
# (1 1) (1 2) (5 4 3 2 1)

# n = 10, a = 5, b = 3
# 1 1 1 1 2 3 4 5 2 1

# a + b > n + 1 => -1 반환

# b가 더 크다
#   1. 1, 2, ... b 나열
#   2. 1, 2, ... a - 1 나열
#   3. 남은 공간에 1 나열

# a가 더 크다
#   1. 1, 2, 3, ..., a 나열
#   2. 1, 2, ..., b - 1 나열
#   3. 남은 공간에 1 나열


# b가 더 클 경우 => b를 먼저 채워서 확보, 자동으로 1, ... a - 1로 정해짐
# a가 더 클 경우 => a를 먼저 채워서 확보, 자동으로 b - 1, ..., 1로 정해짐
# 남은 공간은 무조건 1로 채우기
# 왼쪽에 1을 넣을 수 있는 경우 => 1을 넣기
# 못넣는 경우(a == 1) => 오른쪽에 1을 채워넣기
#   =>오른쪽에 무조건 1 채워넣으면 안 됌, 4 3 2 1 => 이런식일 때는 가장 b에서 채워진 가장 큰 수 옆에 채워넣어야함

# 시간복잡도 O(n)
# 공간복잡도 O(n)

# 반례 10 1 3
# 3 2 1 1 1 1 1 1 1 1
# 정답: 3 1 1 1 1 1 1 1 2 1
