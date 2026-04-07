def solution(n, positions):
    floors = [y for x, y in positions]
    stack = []

    count = 0

    for floor in floors:
        while len(stack) > 0 and floor < stack[len(stack) - 1]:
            stack.pop()

        if floor > 0:
            # 첫번째 출몰
            if len(stack) == 0:
                count += 1
            # 더 낮은 층이 나온 뒤로 첫번째 출몰
            elif len(stack) > 0 and floor > stack[len(stack) - 1]:
                count += 1

        stack.append(floor)

    return count


if __name__ == "__main__":
    n = int(input())
    positions = [[int(string) for string in input().split()]for i in range(n)]
    answer = solution(n, positions)
    print(answer)


# 도형이 있을 때, 해당 도형을 채울 수 있는 직사각형의 최소 개수 구하기

# 도형을 2차원 배열로 표현한 경우
# 도형을 2차원 배열로 바꾸기는 힘들다. => 메모리 제한

# 0 이후의 다각형은 0 이전의 직사각형으로 채울 수 없음
# floor가 동일한 건물 재출현시 이전 직사각형으로 채울 수 있음
# floor가 동일하지 않은 건물 출현시 이전 직사각형으로 채울 수 없음

# 시간복잡도 O(nlogn)
# 공간복잡도 O(n)


# 반례
# 5
# 1 1
# 2 2
# 3 1
# 4 2
# 3

# 3

# 5
# 1 2
# 2 3
# 3 2

# 2

# 3
# 1 1
# 2 3
# 3 2

# 4
# 1 100
# 2 200
# 3 100
# 4 200

# 2 1 2 => 카운트 O
# 5 2 1 2 5
# 3 1 3

# 1 2 1 => 카운트 X
# 1 2 1 2 => 카운트 O
# 4 3 2 => 카운트 O

# 0 1 2 1 2 0
# [1] 1 => 1보다 작은 0이 나온적 있음 => O
# [3] 1 => 1이 나온적 있음 => X
# 0 =>
# 4 3 2 1 0

#


# 첫번째로 출몰 => 포함시킴
# 첫번째로 출몰하는 것이 아님 => 포함 X
# 더 낮은 층이 나옴 => 초기화

# 5 4 3 2 1 => 전부 첫번째로 출몰 => 증가
# 1 2 1 2 1 =>
# [0] 1 => 첫번째 출몰 => 증가
# [1] 2 => 첫번째 출몰 => 증가
# [2] 1 => 첫벗째 출몰 아님
# [3] 2 => 더 낮은 층이 나온 뒤로 첫번째 출몰 => 증가
# [4] 1 => 첫번째 출몰 아님


# stack을 유지
# for floor in floors:
#   while floor < stack.top:
#     stack.pop()
#   if floor != stack.top:
#     count += 1
#
#   stack.append()

# 시간복잡도 O(n)
