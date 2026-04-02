from math import ceil
from sys import stdin

input = stdin.readline


def solution(n, c, positions):
    sorted_positions = sorted(positions)
    start = 0
    end = 1_000_000_000
    while start < end:
        middle = ceil((start + end) / 2)
        minimum_distance = middle

        pointer1 = 0
        pointer2 = 0
        count = 1

        while pointer1 < len(sorted_positions) and pointer2 < len(sorted_positions):
            while pointer2 < len(sorted_positions) and sorted_positions[pointer2] - sorted_positions[pointer1] < minimum_distance:
                pointer2 += 1
            if pointer2 < len(positions):
                count += 1

            pointer1 = pointer2

        if count >= c:  # >= middle 가능, 그 이상으로 거리 벌려도 됨
            start = middle
        else:  # < middle 가능, 그 미만으로 거리 줄어야 함
            end = middle - 1

    return start


if __name__ == "__main__":
    n, c = [int(string) for string in input().strip().split()]
    positions = [int(input().strip()) for i in range(n)]
    answer = solution(n, c, positions)
    print(answer)


# 완전탐색 => nCc (n <= 200_000) , (c <= n) => 불가능

# position 간에 n 이상의 거리를 유지하도록 할 때, 최대 몇개의 cow를 배치할 수 있냐?
# f(n-1) >= f(n) >= f(n+1)
# 처음으로 f(k) = c가 되는 f(k) 중 k 최댓값 찾기
# => 이진탐색 가능
#    각 이진탐색시마다 투포인터로 cow 배치 가능

# 시간복잡도 O(n log 1,000,000,000)
# 공간복잡도 O(n)
