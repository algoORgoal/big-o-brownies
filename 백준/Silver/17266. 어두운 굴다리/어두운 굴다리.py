from math import ceil


def is_within_range(street_lamps, n, m):
    first = street_lamps[0]
    last = street_lamps[len(street_lamps) - 1]

    left_distance = first
    right_distance = n - last

    if left_distance > m:
        return False
    if right_distance > m:
        return False

    for i in range(len(street_lamps) - 1):
        first, second = street_lamps[i], street_lamps[i + 1]
        distance = second - first
        if distance > 2 * m:
            return False

    return True


def solution(n, m, street_lamps):
    start = 1
    end = 100_000

    while start < end:
        mid = (start + end) // 2

        if is_within_range(street_lamps, n, mid):
            end = mid
        else:
            start = mid + 1

    return start


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    street_lamps = [int(string) for string in input().split()]
    answer = solution(n, m, street_lamps)
    print(answer)


# 모든 가로등 사이의 차이가 2 * h 이하인지 확인하기
# 왼쪽 거리 - 가로등 거리가 h 이하, 가로등 - 오른쪽 거리 거리가 h이하

# O(nm) <= O(n ** 2) 10_000_000_000 => 시간 초과
# 이진탐색 활용
# 높이 h일 때 True => 높이 h + 1일 때 True
# True가 되는 최솟값 찾기


# 3
