import heapq
from sys import stdin

input = stdin.readline


def solution(n, edges, nodes):
    queue = []

    sum = 0

    for i in range(0, len(edges)):
        heapq.heappush(queue, nodes[i])

        lowest_cost_per_distance = queue[0]
        lowest_cost = lowest_cost_per_distance * edges[i]
        sum += lowest_cost

    return sum


if __name__ == "__main__":
    n = int(input().strip())
    edges = [int(string) for string in input().strip().split()]
    nodes = [int(string) for string in input().strip().split()]
    answer = solution(n, edges, nodes)
    print(answer)


# k번째 도로를 갈 때, 0 ~ max(0, k)번째 노드 가장 싼 노드에서 충전하기
# n <= 100_000 => 완전탐색시 O(n ** 2)


# priority queue 활용시 가장 낮은 리터당 가격 찾고, 거기에 거리 곱해서 더하기

# 시간복잡도: O(nlogn)
# 공간복잡도: O(n)
