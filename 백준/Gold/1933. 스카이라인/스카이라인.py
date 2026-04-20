import heapq
from math import inf


def solution(n, buildings):
    timetable = {}

    for start, height, end in buildings:
        if start not in timetable:
            timetable[start] = []
        if end not in timetable:
            timetable[end] = []

        timetable[start].append([0, height, end])
        timetable[end].append([1, height, end])

    timeline = sorted([[time, timetable[time]] for time in timetable])

    queue = []
    time = -inf

    skyline = []

    for time, events in timeline:
        for event in events:
            type, height, end = event

            if type == 0:
                heapq.heappush(queue, (-height, end))
            else:
                while len(queue) > 0 and queue[0][1] <= time:
                    heapq.heappop(queue)

        if len(skyline) == 0:
            skyline.append(time)
            skyline.append(-queue[0][0] if len(queue) > 0 else 0)
        elif len(skyline) > 0:
            if len(queue) == 0:
                skyline.append(time)
                skyline.append(0)
            elif skyline[-1] != -queue[0][0]:
                skyline.append(time)
                skyline.append(-queue[0][0] if len(queue) > 0 else 0)

    return skyline


if __name__ == "__main__":
    n = int(input())
    buildings = [[int(string) for string in input().split()]for i in range(n)]
    answer = solution(n, buildings)
    print(*answer)


# 발생 지점, 시작/종료 여부(0/1), 높이
# 발생 지점 오름차순으로 정렬
# 지점 별 방문
# 종료시: 현재 가장 높은 건물의 높이, 종료 지점 == 목표 건물의 높이, 종료 지점 =>
#       pop시키기
#       종료 지점이 현재 지점 전인 모든 것들도 전부다 pop시키기
# 시작시: priority queue에 넣기 (높이, 종료 지점)
# 현재 좌표, 높이 추가

# 시간복잡도 O(nlogn) (n <= 100_000)
# 공간복잡도 O(n)
