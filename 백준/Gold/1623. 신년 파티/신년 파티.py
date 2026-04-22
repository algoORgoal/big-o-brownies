from sys import stdin, stdout

input = stdin.readline


def print(string, end="\n"):
    stdout.write(f"{string}{end}")


def solution(n, weights, parents):
    tree = create_tree(parents, n)

    root = 1
    dp = [[0, 0] for _ in range(n + 1)]
    dfs_iterative(root, tree, weights, dp)

    route1 = reconstruct_iterative(root, True, tree, dp)
    route1.sort()
    route1.append(-1)

    route2 = reconstruct_iterative(root, False, tree, dp)
    route2.sort()
    route2.append(-1)

    print(f"{dp[1][0]} {dp[1][1]}")
    print(" ".join(str(num) for num in route1))
    print(" ".join(str(num) for num in route2))


def create_tree(parents, n):
    tree = [[] for _ in range(n + 1)]

    for child in range(2, n + 1):
        parent = parents[child]
        tree[parent].append(child)

    return tree


def dfs_iterative(root, tree, weights, dp):
    order = []
    stack = [root]

    while stack:
        current = stack.pop()
        order.append(current)
        for child in tree[current]:
            stack.append(child)

    for current in reversed(order):
        dp[current][0] = weights[current]
        dp[current][1] = 0

        for child in tree[current]:
            dp[current][0] += dp[child][1]
            if dp[child][0] >= dp[child][1]:
                dp[current][1] += dp[child][0]
            else:
                dp[current][1] += dp[child][1]


def reconstruct_iterative(root, root_selected, tree, dp):
    route = []

    if root_selected:
        route.append(root)

    stack = []
    for child in tree[root]:
        stack.append((child, root_selected))

    while stack:
        current, parent_selected = stack.pop()

        if not parent_selected and dp[current][0] >= dp[current][1]:
            selected = True
            route.append(current)
        else:
            selected = False

        for child in tree[current]:
            stack.append((child, selected))

    return route


if __name__ == "__main__":
    n = int(input().strip())
    weights = [0] + [int(string) for string in input().strip().split()]
    parents = [0, 0] + [int(string) for string in input().strip().split()]
    solution(n, weights, parents)
