from sys import stdin, stdout

input = stdin.readline


def solution(n, weights, parents_input):
    children = [[] for _ in range(n + 1)]
    for child in range(2, n + 1):
        parent = parents_input[child - 2]
        children[parent].append(child)

    # iterative preorder to get traversal order
    order = []
    stack = [1]
    while stack:
        u = stack.pop()
        order.append(u)
        # children are already increasing; reverse push to preserve natural order if needed
        for v in reversed(children[u]):
            stack.append(v)

    # dp
    dp0 = [0] * (n + 1)  # selected
    dp1 = [0] * (n + 1)  # not selected

    for u in reversed(order):
        dp0[u] = weights[u]
        total1 = 0
        for v in children[u]:
            dp0[u] += dp1[v]
            if dp0[v] >= dp1[v]:
                total1 += dp0[v]
            else:
                total1 += dp1[v]
        dp1[u] = total1

    # reconstruct when root is selected
    selected_root_in = [False] * (n + 1)
    selected_root_in[1] = True
    stack = [(v, True)
             for v in reversed(children[1])]  # parent_selected = True
    while stack:
        u, parent_selected = stack.pop()
        take = False
        if not parent_selected and dp0[u] >= dp1[u]:
            take = True
            selected_root_in[u] = True
        for v in reversed(children[u]):
            stack.append((v, take))

    # reconstruct when root is not selected
    selected_root_out = [False] * (n + 1)
    stack = [(v, False)
             for v in reversed(children[1])]  # parent_selected = False
    while stack:
        u, parent_selected = stack.pop()
        take = False
        if not parent_selected and dp0[u] >= dp1[u]:
            take = True
            selected_root_out[u] = True
        for v in reversed(children[u]):
            stack.append((v, take))

    line1 = f"{dp0[1]} {dp1[1]}\n"

    route_in = [str(i) for i in range(1, n + 1) if selected_root_in[i]]
    route_in.append("-1")
    line2 = " ".join(route_in) + "\n"

    route_out = [str(i) for i in range(1, n + 1) if selected_root_out[i]]
    route_out.append("-1")
    line3 = " ".join(route_out) + "\n"

    stdout.write(line1)
    stdout.write(line2)
    stdout.write(line3)


if __name__ == "__main__":
    n = int(input())
    weights = [0] + list(map(int, input().split()))
    parents_input = list(map(int, input().split()))
    solution(n, weights, parents_input)
