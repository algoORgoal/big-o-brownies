from math import ceil
from sys import stdin

input = stdin.readline


def solution(n, cities, total):
    sum_of_cities = sum(cities)
    if sum_of_cities <= total:
        return max(*cities)

    start = 1
    end = 1_000_000_000

    while start < end:
        mid = int(ceil((start + end) / 2))  # 정수 상한액

        required = 0
        for city in cities:
            required += min(mid, city)

        if required <= total:  # [mid, end], 현재 정수 상한액일 때 예산으로 커버 가능
            start = mid
        else:  # [start, mid), 현재 정수 상한액일 때 예산으로 커버 불가능
            end = mid - 1

    return start


if __name__ == "__main__":
    n = int(input().strip())
    cities = [int(string) for string in input().strip().split()]
    total = int(input().strip())
    answer = solution(n, cities, total)
    print(answer)


# 모든 요청이 배정될 수 있는 경우: sum of cities <= total
#   return max of cities
# 아닌 경우
#   m(n ~ 1,000,000,000) 중에서 줄 수 있는 최대값을 찾아야 함
#   O(nm) => 시간초과
#   m + 1일 때 모두 min(m + 1, cities[i]) 만큼 분배 가능 => m일 때 무조건 가능
#   이진탐색 => O(nlogm)
#     sum = min(cities[i]), m)
#   최대값 찾기


# 시간복잡도 O(nlogm)
# 공간복잡도 O(n)


# 틀린 부분: 총예산 m이 n 이상이라고 해서, 우리가 찾는 정수 상한선도 n 이상이라고 가정할 수 없음.
# min(정수 상한선, cities[i]의 합이 n 이상인 것일 뿐임.
