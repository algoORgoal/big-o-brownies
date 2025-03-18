from collections import deque
# prefix sum을 사용해도 rotateshift 연산으로 인해 너무 복잡해져버리기 때문에, matrix를 deque로 관리하기
# 첫번째, 마지막 column, 이를 제외한 rows를 따로 관리하기
# shift row 연산: O(1)
# rotate 연산: O(1)
# O((r + 1) * n) = O(rn), r <= 50,000, n <= 100,000

def solution(rc, operations):
    row_count, column_count = len(rc), len(rc[0])
    first_column = deque([ rc[i][0] for i in range(len(rc)) ])
    last_column = deque([ rc[i][column_count - 1] for i in range(len(rc))])
    rows = deque([ deque(rc[i][1: column_count - 1]) for i in range(len(rc)) ])
    for operation in operations:
        if operation == "ShiftRow":
            first_column.appendleft(first_column.pop())
            last_column.appendleft(last_column.pop())
            rows.appendleft(rows.pop())
        else:
            rows[0].appendleft(first_column.popleft())
            last_column.appendleft(rows[0].pop())
            rows[row_count - 1].append(last_column.pop())
            first_column.append(rows[row_count - 1].popleft())

    result = [ [ first_column[i], *rows[i] ,last_column[i] ]  for i in range(row_count)]
    return result
    
        