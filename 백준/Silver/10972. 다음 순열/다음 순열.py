


def solution(n, sequence):
    i = len(sequence) - 1

    while i > 0:
        if sequence[i - 1] < sequence[i]:
            # sequence[current] > ... > sequence[n]

            j = n - 1
            while j > i - 1:
                if sequence[i - 1] < sequence[j]:
                    sequence[i - 1], sequence[j] = sequence[j], sequence[i - 1] # 정렬 필요 없음. a[i] > a[i + 1] > a[j] > a[i - 1] > a[j + 1] 유지
                    break
                j -= 1
            start_part = sequence[:i]
            end_part = list(reversed(sequence[i:]))

            return start_part + end_part
        i -= 1

    return -1


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
# 다만 항상 가장 큰 값 heap이 찾아주고, 이진탐색 bisect_right가 현재 값보다 큰 값 중 가장 작은값 찾아줘서 구현이 쉬움

# heapq를 사용할 필요 없음. i번째까지 왔으면 이미 a[i] > ... > a[n]이므로 a[i - 1]과 a[i]끼리만 비교하면 됌
