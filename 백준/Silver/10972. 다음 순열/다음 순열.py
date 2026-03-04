import heapq
from bisect import bisect_right


def solution(n, sequence):
    arr = []

    while len(sequence) > 0:
        node = sequence.pop()
        heapq.heappush(arr, -node)

        if len(arr) > 0 and -arr[0] > node:
            sorted_arr = sorted([-num for num in arr])
            target_index = bisect_right(sorted_arr, node)
            target = sorted_arr.pop(target_index)
            sequence.append(target)
            for num in sorted_arr:
                sequence.append(num)
            break

    if len(sequence) == 0:
        return -1

    return sequence


if __name__ == "__main__":
    n = int(input())
    sequence = [int(string) for string in input().split(' ')]
    answer = solution(n, sequence)
    if answer == -1:
        print(answer)
    else:
        for index, num in enumerate(answer):
            if index == len(answer) - 1:
                print(num, end="")
            else:
                print(num, end=" ")


# n개를 n번 배치하는 경우의 수: nPn = n! (n <= 10_000) => 시간 초과
# arr를 유지
# 뒤에서부터 빼면서, 현재 더 큰 게 발견되면 그 중 '최소값'으로 세팅
# 나머지 값은 오름차순으로 채워넣기
# 이걸 못했다면 -1 반환

# 공간복잡도 O(n)
# 시간복잡도 O(nlogn) (heap push) + O(nlogn) (sort) + O(n) (pop) + O(n) (push) = O(nlogn)

# O(n ** 2)으로도 가능
