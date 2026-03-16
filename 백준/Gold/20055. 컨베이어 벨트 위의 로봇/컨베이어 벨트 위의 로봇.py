from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10 ** 5)


# 언제든지 내리는 위치에 로봇이 도달하면 즉시 내림
# 로봇을 올리는 위치에 올리거나 어떤 칸으로 이동시 내구도 1 감소


# 내구도 0인 칸의 개수 k개인 경우 종료

def solution(n, k, endurances):
    step = 1
    conveyer_belt = deque([[endurance, False] for endurance in endurances])

    count = 0

    while True:
        rotate(conveyer_belt)

        conveyer_belt[n - 1][1] = False

        for i in range(n - 2, -1, -1):
            if conveyer_belt[i][1] == True and conveyer_belt[i + 1][0] > 0 and conveyer_belt[i + 1][1] == False:
                conveyer_belt[i][1] = False
                conveyer_belt[i + 1][1] = True

                conveyer_belt[i + 1][0] -= 1

                if conveyer_belt[i + 1][0] == 0:
                    count += 1

        conveyer_belt[n - 1][1] = False

        if conveyer_belt[0][0] > 0:
            conveyer_belt[0][1] = True
            conveyer_belt[0][0] -= 1
            if conveyer_belt[0][0] == 0:
                count += 1

        conveyer_belt[n - 1][1] = False

        if count >= k:
            break

        step += 1

    return step


def rotate(arr):
    last = arr.pop()
    arr.appendleft(last)


if __name__ == "__main__":
    n, k = [int(string) for string in input().split()]
    endurances = [int(string) for string in input().split()]
    answer = solution(n, k, endurances)
    print(answer)

# 2 <= n <= 100
# 1 <= a <= 1000
# O(2n * a)

# 각 칸에 저장되어야 하는 값
# 1. 내구도
# 2. 로봇 존재 여부

# 현재 내구도가 0인 칸의 개수

# 단계의 정의
# 1, 2, 3, 4를 묶은 것

# 200개에 1000개가 들어있음 => 200_000
# 한번 돌릴 때 1_000번 배열 연산 => 200_000_000
# 시간 1초 초과 가능
# O(2n * 1000 ** 2)
# O(2n * 1000)
