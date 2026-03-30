

def solution(k, students):
    line = []
    sum = 0
    for student in students:
        if len(line) == 0:
            line.append(student)
        elif line[len(line) - 1] < student:
            line.append(student)
        else:
            for i in range(len(line)):
                student_in_line = line[i]
                if student_in_line > student:
                    sum += len(line) - i  # 번째 인덱스이 경우 앞에 i명의 사람이 있음
                    line.insert(i, student)
                    break

    return sum


if __name__ == "__main__":
    p = int(input())
    for i in range(p):
        nums = [int(string) for string in input().split()]
        k, students = nums[0], nums[1:]
        answer = solution(k, students)
        print(f"{k} {answer}")

# 1 <= p <= 1000
# k <= 20
# k ** 2 * p <= 400 000
# 모든 학생에 대해 선형탐색 후 집어넣기


# 0 1 2 3 4
# 2번 학생이 더 크다 => 2번에 집어넣고, 2 3 4 뒤로 밀기
# 5 - i
