from math import inf


def get_func(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    a = (y1 - y2) / (x1 - x2)
    b = ((y1 + y2) - a * (x1 + x2)) / 2

    return a, b


def get_y(x, a, b):
    return a * x + b


def solution(n, buildings):
    positions = [(i, building) for i, building in enumerate(buildings)]

    max_count = -inf
    for i in range(n):
        point1 = positions[i]

        count = 0

        for j in range(n):
            if i == j:
                continue

            point2 = positions[j]

            a, b = get_func(point1, point2)

            blocked = False
            for k in range(min(i, j) + 1, max(i, j)):
                x, y = positions[k]
                if get_y(x, a, b) <= y:
                    blocked = True
                    break

            if blocked == False:
                count += 1

        max_count = max(max_count, count)

    return max_count


if __name__ == "__main__":
    n = int(input())
    buildings = [int(string) for string in input().split()]
    answer = solution(n, buildings)
    print(answer)


# a = (y1 - y2) / (x1 - x2)
# b = ((y1 + y2) - a * (x1 + x2)) / 2

# time complexity: O(n ** 3)
# space complexity: O(n)
