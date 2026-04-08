def solution(n, nums):
    start = 0
    end = 0
    sum = 0

    num_set = set()

    # [start, end): 중복되는 요소가 들어있지 않은 구간
    # 각 start에 대해서, 중복되지 않게 몇번 담을 수 있는지 확인
    # 새로운 요소 추가되는 것 없다면, 기존 수열에 담기는 경우의 수만 있음
    # 새로운 요소 추가되었을 경우 => 새로운 요소로 인해
    # (총 길이로 만들 수 있는 경우의 수) - (기존 요소로 만들 수 있는 경우의 수) 추가됌
    # 시간복잡도: O(n)

    while start < len(nums) and end <= len(nums):
        old_count = end - start
        new_count = 0
        while end < len(nums) and nums[end] not in num_set:
            num_set.add(nums[end])
            end += 1
            new_count += 1

        if new_count > 0:  # 기존의
            total_count = (end - start)
            sum += ((total_count * (total_count + 1) -
                    old_count * (old_count + 1)) // 2)

        num_set.remove(nums[start])
        start += 1

    return sum


if __name__ == "__main__":
    n = int(input())
    nums = [int(string) for string in input().split()]
    answer = solution(n, nums)
    print(answer)


# 4 + 3 + 2 + 1 = 10

# 1 2 3 4 5
# 12 23 34 45
# 123 234 345
# 1234 2345
# 12345

# 5 + 4 + 3 + 2 + 1 = 5

# 모든 수열을 계산 => O(2 ** n) = O(2 ** 100_000) => 시간초과 발생

# start, end 두고
# end + 1 포함시키기 가능 => end += 1
# end 포함시키기 불가능 => end + 1이 빠질 때까지 start += 1
# subarray 만드는 경우의 수: 3 + 2 + 1 = 1 + ... + n = n(n + 1) / 2


# 1 2 3
#   2 3 1
#     3 1 2


# 1
# 2
# 3
# 1 2
# 2 3
# 1 2 3

# 2 (x)
# 3 (x)
# 1 (o)
# 2 3 (x)
# 3 1 (o)
# 2 3 1 (o)

# 3 (x)
# 1 (x)
# 2 (o)
# 3 1 (x)
# 1 2 (o)
# 3 1 2 (o)


# 1 2 3 4
# 4 + 3 + 2 + 1 = 10
# 1 + 2 + 3 + 4 = 4 * 5 / 2 = 10
# 1 + ... + n = n * (n + 1) / 2

# 원래 2개가 사용됐고, 2개를 더한다
# 2 * 3 / 2 = 3
# 4 * 5 / 2 = 10
# 4 * 5 - 2 * 3 / 2 = (20 - 6) / 2 = 7

# start 0, end = 0, sum = 0
# while start < len(num) - 1 and end < len(num) - 1:
#   old_count = end - start + 1
#   while num[end + 1] not in num_set:
#     end += 1
#   total_count = end - start + 1
#   sum = (total_count * total_count + 1 - old_count * old_count + 1) // 2
# return sum


# 6
# 2 1 3 4 1 2


# 4 + 3 + 2 + 1 = 10
# (4 + 3 + 2 + 1) - (2 + 1) = 7
