from itertools import combinations


def solution(n, nums):
    table = {}
    for i, num in enumerate(nums):
        if num not in table:
            table[num] = set()
        table[num].add(i)

    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            # 합이되는 원소가 존재하지 않는 경우
            if sum not in table:
                continue
            # i와 j를 제외한 다른 인덱스의 합원소가 없는 경우
            if len(table[sum] - set([i, j])) == 0:
                continue

            # i와 j를 제외한 다른 인덱스는 모두 처리
            count += len(table[sum] - set([i, j]))
            # i와 j가 들어있었을 경우 이는 여전히 포함시키기
            table[sum] = table[sum] & set([i, j])

    return count


if __name__ == "__main__":
    n = int(input())
    nums = [int(string) for string in input().split()]
    answer = solution(n, nums)
    print(answer)

# 2000C2 = 2000 * 1999 / 2
# 고른 두 수의 합이 set(nums)에 있을 경우:
# good_set에 추가하기
# nums에 있는 수 중 good_set에 있는 수의 개수 반환
# 시간복잡도 O(n ** 2)
# 공간복잡도 O(n)

# 반례: 중복되는 수 두개로 새로운 수를 만들 수도 있음
# 해결 방법: num_set으로 조합하는 게 아닌 nums에서 2개를 조합한다.

# 반례:
# 0 -5 5
# 0과 -5를 더해서, -5를 만들 수 있으나 이는 곧 자기 자신
# 정답: 1

# 0 -5 -5
# 0과 -5를 더해서 실제로 자기 자신이 아닌 -5를 만들 수 있음


# 전략
# hash table 각 숫자별로 어떤 인덱스에 있는지 계산 num -> set()
# arr[i] + arr[j] in table이면서,
# len(table[arr[i] + arr[j]] - i - j) > 0인지 확인
# (i + j가 i,j가 아닌 다른 인덱스의 수) => 다른 수 두개의 합으로 표현됌
