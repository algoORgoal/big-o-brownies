import heapq
from collections import deque

def solution(jobs):
    todos = deque(sorted([ [ jobs[index][1], jobs[index][0], index ] for index in range(0, len(jobs)) ], key=lambda todo: todo[1]))
    
    # 소요 시간 오름차순, 요청 시각 오름차순, 번호 오름차순
    
    queue = []
    current = None
    trunaround_history = []
    
    time = 0
    
    while len(queue) > 0 or len(todos) > 0 or current != None:
        while len(todos) > 0 and todos[0][1] == time:
            heapq.heappush(queue, todos.popleft())
            
            
        if current != None:
            current[0] -= 1
            if current[0] == 0:
                trunaround_history.append(time - current[1])
                current = None if len(queue) == 0 else heapq.heappop(queue)
        else:
            current = None if len(queue) == 0 else heapq.heappop(queue)

        
        time += 1
        
    
    
    return sum(trunaround_history) // len(trunaround_history)
    



# 대기 큐에 있거나 할일에 있으면
#  현재 시점에 요청된 작업 push
#  현재 실행중인 작업의 남은 시간 -= 1
#  현재 실행중인 작업의 남은 시간 === 0
#    history에 기록(작업 종료 시각, 즉 time)
#    대기 큐에서 우선순위가 높은 작업 꺼내서 현재 실행중인 작업으로 할당 (작업 소요시간 작은 것, 작업 요청 시각이 빠른 것, 작업 번호가 작은 것)
#  time += 1