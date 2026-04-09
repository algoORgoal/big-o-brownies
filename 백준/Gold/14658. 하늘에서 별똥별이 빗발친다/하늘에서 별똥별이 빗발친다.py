from sys import stdin
from math import inf

input = stdin.readline


def solution(n, m, l, k, stardusts):
    max_points_count = -inf

    for i in range(len(stardusts)):
        for j in range(len(stardusts)):
            stardust_x, stardust_y = stardusts[i][0], stardusts[j][1]

            count1 = count_points_in_range((stardust_x, stardust_x + l),
                                           (stardust_y, stardust_y + l), stardusts)

            count2 = count_points_in_range((stardust_x, stardust_x + l),
                                           (stardust_y - l, stardust_y), stardusts)

            count3 = count_points_in_range((stardust_x - l, stardust_x),
                                           (stardust_y, stardust_y + l), stardusts)

            count4 = count_points_in_range((stardust_x - l, stardust_x),
                                           (stardust_y - l, stardust_y), stardusts)

            max_points_count = max(max_points_count, count1,
                                   count2, count3, count4)

    return k - max_points_count


def count_points_in_range(x_range, y_range, points):
    min_x, max_x = x_range
    min_y, max_y = y_range

    count = 0
    for x, y in points:
        if min_x <= x <= max_x and min_y <= y <= max_y:
            count += 1

    return count


if __name__ == "__main__":
    n, m, l, k = [int(string) for string in input().strip().split()]
    stardusts = [[int(string) for string in input().strip().split()]
                 for i in range(k)]
    answer = solution(n, m, l, k, stardusts)
    print(answer)

# l >= 100_000 => 입출력 이슈 있을 수 있으므로 stdin 활용

# search space의 모든 상태공간을 방문
#  모든 별똥별 조합을 방문 => 2 ** 100 => time limit error
#  각 점을 꼭짓점으로해서, 최대 몇개까지 방문할 수 있는지 확인
#  각 꼭짓점의 (왼쪽 위 / 오른쪽 위 / 왼쪽 아래 / 오른쪽 아래) * 방문 개수 =>
#  O(n ** 2)
#  정답이 (x, y)를 포함하면서 x가 더 왼쪽에 있음 => greedy의 점 포함 개수 >= optimal의 점 포함 개수
#  정답이 (x, y)를 포함하면서 y가 더 위에 있음 => greedy의 점 포함 개수 >= optimal의 점 포함 개수
#  점을 가장 많이 포함하는 경우에 n - (점 포함 개수)가 정답

# 반례
# 10 10 4 4
# 10 7
# 13 6
# 13 7
# 14 10
# 정답: 0 그런데 1 반환

# 시간복잡도 O(n ** 2)
# 공간복잡도 O(n)


# 100 100 1 2
# 1 1
# 2 2
