from itertools import combinations
from math import inf


def solution(n, d, shortcuts):

    min_distance = inf
    for i in range(0, n + 1):
        for candidate in combinations(shortcuts, i):
            total_distance = d

            is_valid = True

            for j in range(len(candidate)):
                start_1, end_1, distance_1 = candidate[j]
                if start_1 < 0 or end_1 > d:
                    is_valid = False

                for k in range(j + 1, len(candidate)):

                    start_2, end_2, distance_2 = candidate[k]
                    if not (end_1 <= start_2 or end_2 <= start_1):
                        is_valid = False

            if is_valid == True:
                for start, end, distance in candidate:
                    total_distance -= ((end - start) - distance)

                min_distance = min(min_distance, total_distance)

    return min_distance


if __name__ == "__main__":
    n, d = [int(string) for string in input().split()]
    shortcuts = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, d, shortcuts)
    print(answer)

# 1. 지름길을 선택하는 모든 경우의 수 만들기 => combinations
# 2. 해당 지름길 집합이 유효한지 확인
# 모든 지름길을 순회하여 해당 지름길의 end <= 다른 지름길의 start or 다른 지름길의 end <= 해당 지름길의 start인지 확인
# 지름길 집합을 선택했을 때 주행 거리 계산
# 원래 거리 - ((도착 지점) - (시작 지점) - 주행 거리)

# 시간복잡도: O((2 ** n) * (n ** 2)) (n <= 12)
# 589824 => 가능
# 공간복잡도: O((2 ** n))
