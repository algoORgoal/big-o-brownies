

def solution(h, w, columns):
    matrix = [[0 for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            column = columns[j]
            if column - 1 >= i:
                matrix[i][j] = 1

    sum = 0
    for i in range(h):
        start = 0
        end = 0
        while start < w and end < w:
            if matrix[i][start] == 0:
                start += 1
                end = start
            else:
                while end + 1 < w and matrix[i][end + 1] == 0:
                    end += 1
                if start < end and end + 1 < w and matrix[i][start] == matrix[i][end + 1] == 1:
                    length = (end - start)
                    sum += length
                start = end + 1
                end = start

    return sum


if __name__ == "__main__":
    h, w = [int(string) for string in input().split()]
    columns = [int(string) for string in input().split()]
    answer = solution(h, w, columns)
    print(answer)

# 제일 큰 기둥 찾기
# 기둥 사이의 구간에 채워지는 빗물 각각 계산하기

# 8 3 2 4 4 3 2 4
# 끝부분: 한 쪽보다 더 높기만 해도 ok
# arr[start] > arr[start + 1] >= ... <= arr[end - 1] < arr[end] >= arr[end + 1]인 (start,end) 찾기
# min(start, end) 찾아서 빗물 채우기

# 투포인터 알고리즘 활용
# 1. start: start > [start + 1]이 처음으로 등장하는 start를 찾음
# 2. start + 1부터 시작하여, arr[end] >= arr[end + 1]이 처음으로 등장하는 end를 찾음
# 3. start + 1부터, end - 1까지 빗물 채워지는 양 계산
# 4. end = start로 설정하고 다시 진행


# 제일 큰 기둥의 기준
#


# 3 2 1 2 => 1

# 3 1 2 1 4
# 0 ~ 4 최대 높이: 3
# 4 1 2 1 3
# 1 ~ 5 최대 높이: 3


# (높이: 4, 5번째) (높이: 3, 4번째), (높이 3, 1번째), (높이 2, 2번째), (높이 2, 마지막 번째)
# 높이 4 ~ 높이 3 사이 표시
# 5 3 3 3 3
# 높이 5 ~ 3사이 표시 => X


# 반례 5 3 2 1 2

# 정답: 아랫층부터,
# black인 칸 사이를 칠하기
# 투포인터로 가능 =>
# 검정색이 되는 곳이 start, start + 1 부터 시작해서 검정색이 되는 곳이 end
# (end - start) - 1 더하고, start = end
