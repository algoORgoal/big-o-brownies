from bisect import bisect_left
from math import inf


def solution(n, sorted_nums):
    min_sum = inf
    two_nums = [inf, inf]

    for num in sorted_nums:
        index = bisect_left(sorted_nums, -num)

        candidates = []
        # 부호 바꿨을 때, num == nums[index - 1] or num == nums[index + 1] 가능

        indices = [index - 2, index - 1, index, index + 1, index + 2]

        for nearby_index in indices:
            if 0 <= nearby_index < len(sorted_nums):
                if sorted_nums[nearby_index] != num:
                    candidates.append(sorted_nums[nearby_index])

        closest = candidates[0]

        for candidate in candidates:
            if abs(candidate + num) < abs(closest + num):
                closest = candidate

        sum = abs(num + closest)

        if sum <= min_sum:
            min_sum = sum
            two_nums = [num, closest]

    return sorted(two_nums)


if __name__ == "__main__":
    n = int(input())
    nums = [int(string) for string in input().split()]
    two_nums = solution(n, nums)
    print(*two_nums)


# 100_000 * 100_000 => 10 ** 10 => TLE
# 각 음수별로 해당 숫자에 절대값이 가장 가까운 양수 찾기
# nlogn

# 0 10 20 30 40
# 50 => 40이 제일 가까운
# 34 => 30이 제일 가까움
# 46 => 40이 제일 가까움
# bisect_right 쓰고, 양 옆 값 중에 더 가까운 값 선택

# 시간복잡도: 정렬 + 이진탐색 => nlogn
# 공간복잡도: O(n)
