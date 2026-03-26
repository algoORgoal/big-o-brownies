import heapq
from sys import stdin

input = stdin.readline

pq = []


def solution(n, row):
    for num in row:
        heapq.heappush(pq, num)

    while len(pq) > n:
        heapq.heappop(pq)

    return pq[0]


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        row = [int(string) for string in input().strip().split()]
        answer = solution(n, row)
    print(answer)

# 시간복잡도 O(nlogn)
# 공간복잡도: O(n ** 2)
# 메모리 소모량: 28 * 1500 * 1500 byte
# 12MB = 12 * 1_000 * 1_000 byte
# 메모리 초과

# 극복 방법
# 각 루프 때마다 제일 큰 n개의 숫자만 priority queue에 남겨 놓기
# heapq에 저장할 때는 오름차순만 지원되므로 - 붙이고, 꺼낼 때 - 붙이기
# 항상 n개 요소만 담고, 가장 작은 요소 반환하기

# 메모리 소모량: 28 * 1500 byte
