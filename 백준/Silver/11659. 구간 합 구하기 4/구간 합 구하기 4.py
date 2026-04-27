
def solution(n, m, nums, queries):

    prefix_sums = [0 for i in range(len(nums))]
    for index, num in enumerate(nums):
        if index == 0:
            continue
        elif index == 1:
            prefix_sums[index] = nums[index]
        else:
            prefix_sums[index] = prefix_sums[index - 1] + nums[index]

    results = []

    for start, end in queries:
        if start == 1:
            results.append(prefix_sums[end])
        else:
            results.append(prefix_sums[end] - prefix_sums[start - 1])

    return results


if __name__ == "__main__":
    n, m = [int(string) for string in input().split()]
    nums = [0] + [int(string) for string in input().split()]
    queries = [[int(string) for string in input().split()] for i in range(m)]
    answer = solution(n, m, nums, queries)
    for num in answer:
        print(num)


# 완전탐색 => O(nm)
# prefix sum 관리 => O(n)
# 각 구간합 계산시 시간복잡도 O(1)로 실행 가능
# results = []
# for start, end in queries:
#   if start == 0:
#     results.append(prefix_sum[end])
#   else:
#     results.append(prefix_sum[end] - prefix_sum[start - 1])
