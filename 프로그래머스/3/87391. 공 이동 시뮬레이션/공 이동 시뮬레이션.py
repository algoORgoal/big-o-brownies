# n * m
# 최종적으로 좌/우로 얼마나 움직이는지, 상/하로 얼마나 움직이는지가 중요함.
# 예) 4 * 4에서, 좌로 2, 상으로 2 이동
# (0, 0)에서 오른쪽으로 2, 아래로 2 까지의 점들은 모두 (0, 0)으로 이동 가능하다.

# 1. 움직이는 방향에 따라 offset_x, offset_y 계산
# 2. span_x = min(max(0, x + offset_x), n - 1)
#    span_y = min(max(y + offset_y), m - 1)
#    reachable_area_size = abs(x - span_x + 1) * abs(y - span_y + 1)
#    reachable_area_size


# x x x *
# x x x *
# x x x * 
# * * * *



def solution(n, m, x, y, queries):

    # 최종적으로 (x, y)에 도착할 수 있는 시작점의 범위

    r1 = r2 = x

    c1 = c2 = y

    # 쿼리를 역순으로 처리

    for direction, count in reversed(queries):

        if direction == 0:

            # 정방향: 왼쪽

            # 역방향: 오른쪽

            if c1 != 0:

                c1 += count

            c2 = min(c2 + count, m - 1)

            if c1 > m - 1:

                return 0

        elif direction == 1:

            # 정방향: 오른쪽

            # 역방향: 왼쪽

            if c2 != m - 1:

                c2 -= count

            c1 = max(c1 - count, 0)

            if c2 < 0:

                return 0

        elif direction == 2:

            # 정방향: 위쪽

            # 역방향: 아래쪽

            if r1 != 0:

                r1 += count

            r2 = min(r2 + count, n - 1)

            if r1 > n - 1:

                return 0

        else:

            # 정방향: 아래쪽

            # 역방향: 위쪽

            if r2 != n - 1:

                r2 -= count

            r1 = max(r1 - count, 0)

            if r2 < 0:

                return 0

    return (r2 - r1 + 1) * (c2 - c1 + 1)


# 문제점
# 2 위치에서 2억번 왼쪽 => 0, 다시 1억번 오른쪽 이동 => 위치 n으로 된다
# 따라서 offset만을 기준으로 계산하는 것은 부족하다.
# 최종목적지 기준으로 


    