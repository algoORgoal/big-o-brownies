def solution(n, parents):
    tree = {}
    for child, parent in enumerate(parents):
        if parent not in tree:
            tree[parent] = []

        tree[parent].append(child)

    return dfs(0, tree)


def dfs(current, tree):
    if current not in tree:
        return 0

    times = sorted([dfs(child, tree) for child in tree[current]], reverse=True)
    return max([time + i + 1 for i, time in enumerate(times)])


if __name__ == "__main__":
    n = int(input())
    parents = [int(string) for string in input().split()]
    answer = solution(n, parents)
    print(answer)


# time(k)를 루트로 하는 subtree가 전달하는데 걸리는 시간의 최솟값
# 1. children을 걸리는 시간 최댓값 순으로 정렬
# 2. return max([child1 + 1, child2 + 2, ... ]) 반환
# 시간복잡도: O(n)
# 공간복잡도: O(n)
