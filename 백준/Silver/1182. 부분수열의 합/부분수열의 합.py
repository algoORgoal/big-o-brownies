from itertools import combinations


def solution(n, s, integers):
    count = 0
    for i in range(1, n + 1):
        for combination in combinations(integers, i):
            if sum(combination) == s:
                count += 1

    return count


if __name__ == "__main__":
    n, s = [int(string) for string in input().split()]
    integers = [int(string) for string in input().split()]
    answer = solution(n, s, integers)
    print(answer)


# prefix sum을 통해 해결 가능
# i: -1 ~ len(arr) - 2
# j : i + 1 ~ len(arr) - 1

# 시간복잡도 O(n ** 2)

# 부분수열의 경우 연속된 요소를 포함하지 않아도 된다. 이는 연속 부분수열에 해당한다.
# 해결 방안
# n개 중에 1개, 2개, ..., 20개 선택했을 때 합을 확인해서 s가 되는지 확인
# combinations(arr, k) (1 <= k <= 20)
