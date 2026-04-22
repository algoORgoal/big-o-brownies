from sys import stdin
from sys import stdout

input = stdin.readline


def print(string, end="\n"):
    stdout.write(f"{string}{end}")


def solution(n, weights, parents):
    tree = create_tree(parents)

    root = 1
    dp = {}
    dfs_iterative(tree, weights, dp, root)

    route1 = []
    route1.append(root)
    if root in tree:
        for child in tree[root]:
            reconstruct_iterative(child, True, tree, dp, route1)

    route1.sort()
    route1.append(-1)

    route2 = []
    if root in tree:
        for child in tree[root]:
            reconstruct_iterative(child, False, tree, dp, route2)

    route2.sort()
    route2.append(-1)

    for index, max_sum in enumerate(dp[1]):
        if index == len(dp[1]) - 1:
            print(max_sum, end="\n")
        else:
            print(max_sum, end=" ")

    for index, num in enumerate(route1):
        if index == len(route1) - 1:
            print(num, end="\n")
        else:
            print(num, end=" ")

    for index, num in enumerate(route2):
        if index == len(route2) - 1:
            print(num, end="\n")
        else:
            print(num, end=" ")


def create_tree(parents):
    tree = {}
    for index, parent in enumerate(parents):
        child = index + 1
        if parent not in tree:
            tree[parent] = []

        tree[parent].append(child)

    return tree


def dfs(current, tree, weights, dp):
    dp[current] = [weights[current], 0]

    if current not in tree:
        return

    for child in tree[current]:
        dfs(child, tree, weights, dp)
        dp[current][0] += dp[child][1]
        dp[current][1] += max(dp[child][0], dp[child][1])


def dfs_iterative(tree, weights, dp, root):
    stack = []
    stack.append(root)

    history = []

    while len(stack) > 0:
        current = stack.pop()
        history.append(current)

        if current not in tree:
            continue

        for child in tree[current]:
            stack.append(child)

    for current in reversed(history):
        dp[current] = [weights[current], 0]

        if current not in tree:
            continue

        for child in tree[current]:
            dp[current][0] += dp[child][1]
            dp[current][1] += max(dp[child][0], dp[child][1])


def reconstruct(current, parent_selected, tree, dp, route):
    if parent_selected == False:
        if dp[current][0] >= dp[current][1]:
            route.append(current)
            selected = True
        else:
            selected = False
    else:
        selected = False

    if current in tree:
        for child in tree[current]:
            reconstruct(child, selected, tree, dp, route)


def reconstruct_iterative(node, root_selected, tree, dp, route):
    stack = []
    stack.append((node, root_selected))

    while len(stack) > 0:
        current, parent_selected = stack.pop()

        if parent_selected == False:
            if dp[current][0] >= dp[current][1]:
                route.append(current)
                selected = True
            else:
                selected = False
        else:
            selected = False

        if current not in tree:
            continue

        for child in tree[current]:
            stack.append((child, selected))


if __name__ == "__main__":
    n = int(input().strip())
    weights = [0] + [int(string) for string in input().strip().split()]
    parents = [-1] + [int(string) for string in input().strip().split()]
    solution(n, weights, parents)


# 1. generate a tree using child - parent relation
# 2. calculate dp by visiting all the nodes from the root to the leaves
# 3. reconstruct route using dp array

# time complexity: O(n)
# space complexity: O(n)

# sum(weights) <= 2 000 000 000
# dp[parent][0] = sum(dp[child][1])
# dp[parent][1] = sum(max(dp[child][0], dp[child][1]))

# should_exclude
# dfs(current, should_exclude, tree, dp, route):
#   if should_exclude == False:
#     route.add(current)
#     if dp[current][0] >= dp[current][1]:
#       route.add(current)
#       for child in tree[current]:
#         dfs(child, True, tree, dp, route)
#     else:
#       for child in tree[current]:
#         dfs(child, False, tree, dp, route)
#   if should_exclude == True:
#     for child in tree[current]:
#        dfs(child, False, tree, dp, route)
