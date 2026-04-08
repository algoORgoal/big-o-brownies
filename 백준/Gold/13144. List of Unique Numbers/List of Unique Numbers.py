def solution(n, nums):

    sum = 0
    start = 0
    end = 0
    seen = set()
    # [start, end)
    for start in range(n):
        while end < n and nums[end] not in seen:
            seen.add(nums[end])
            end += 1

        count = end - start
        sum += count
        seen.remove(nums[start])

    return sum


if __name__ == "__main__":
    n = int(input())
    nums = [int(string) for string in input().split()]
    answer = solution(n, nums)
    print(answer)


# nums[0]으로 시작하는 수열 중 중복 없는 수열 세기
# nums[1]으로 시작하는 수열 중 중복 없는 수열 세기
# ...

# nums[1]~nums[end]는 중복 없는 수열 보장됌 따라서 여기서부터 시작 가능
# nums[2]~nums[end]는 중복 없는 수열 보장됌 따라서 여기서부터 시작 가능
# nums[k] ~ nums[end]까지 중복 없는 수열 => nums[k + 1] ~ nums[end]까지 중복 없는 수열


# start에 대해, 중복 없을 때까지 세기
# 요소의 개수가 곧 경우의 수의 합
