from bisect import bisect_right
from math import inf


def solution(n, k, history):
    cache = set()
    access_time_table = {}

    replacement_count = 0

    for time, item in enumerate(history):
        if item not in access_time_table:
            access_time_table[item] = []
        access_time_table[item].append(time)

    for time, item in enumerate(history):
        if item in cache:
            continue

        if len(cache) < n:
            cache.add(item)
            continue

        furthest_access_time = -inf
        furthest_item = -1

        for cache_item in cache:
            next_access_time_index = bisect_right(
                access_time_table[cache_item], time)

            if next_access_time_index >= len(access_time_table[cache_item]):
                cache.remove(cache_item)
                replacement_count += 1
                cache.add(item)
                break

            next_access_time = access_time_table[cache_item][next_access_time_index]
            if furthest_access_time < next_access_time:
                furthest_access_time = next_access_time
                furthest_item = cache_item

        if item not in cache:
            cache.remove(furthest_item)
            replacement_count += 1
            cache.add(item)

    return replacement_count


if __name__ == "__main__":
    n, k = [int(string) for string in input().split()]
    history = [int(string) for string in input().split()]
    answer = solution(n, k, history)
    print(answer)


# 현재 상태: 무엇이 꽂혀있는지 저장
# 구멍 10개이고 사용 횟수 100인 경우
# 각 시행마다 어떤 탭에서 뺄지 결정 => 10 ** 100

# 3 6
# 1 2 3 4 1 2

# 3 10
# 1 2 3 4 5 6 7 8 9 1
# 2 3 4 5 6 7 8 9 <= 겹치지 않음
# 3 10
# 1 2 3 4 2 3 4 1 1 1
# 2 3 4 2 3 4 사용
# 1 1 1 캐싱

# 1. 현재를 기준으로 n - 1번 내에 쓰일 것
# 2. 가장 많이 사용되는 것

# 완전탐색에서 최적화
# 4 2 3 / 2 3 4 / 1 2 4
# (현재 숫자의 리스트), 교체 횟수
# 현재 숫자의 리스트가 동일한데, 교체 횟수가 더 크면 볼 필요 없음


# Min page replacement algorithm
# 빈 공간 있으면 넣기
# 교체
# 1. 앞으로 안 쓰일 데이터 아이템을 교체
# 2. 모두 앞으로 쓰일 예정이라면, 그 중에서 가장 앞으로 가장 늦게 쓰일 데이터 아이템을 교체

# replacement_count = 0
# for time, item in enumerate(history):
#   if len(cache) < size:
#      cache.add(item)
#   else:
#     for cache_item in cache:
#       if access_time_table[cache_item] doesn't have k such that k > time:
#           cache.remove(cache_item)
#           replacement_count += 1
#           cache.add(item)
#           break
#     if item not in cache:
#         latest_time = inf
#         latest_item = -1
#         for cache_item in cache:
#           next_time = access_time_table[bisect.right(access_time_table[cache_item], time)]
#           if latest_time > next_time:
#              latest_time, latest_item = next_time, cache_item
#         cache.remove(latest_item)
#         replacement_count += 1
#         cache.add(item)
# return replacement_count


# 시간복잡도: k * n logn
# 공간복잡도: O(k + n)
