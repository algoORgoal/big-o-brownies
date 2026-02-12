from collections import deque

def solution(priorities, location):
    processes = deque([ [ priorities[i], i]  for i in range(0, len(priorities)) ])
    
    
    history = []
    while len(processes) > 0:
        targetPriority, targetIndex = processes.popleft()
        
    
        print(targetPriority, targetIndex)
        
        shouldAppend = True
        for priority, index in processes:
            if targetPriority < priority:
                shouldAppend = False
        
        if shouldAppend:
            history.append([ targetPriority, targetIndex ])
        else:
            processes.append([ targetPriority, targetIndex ])
        
    for i in range(0, len(history)):
        priority, index = history[i]
        if index == location:
            return i + 1
        
        
        
    
    

    
    return 0

# 2 1 3 2
# A B C D
# [] A(2) B(1) C(3) D(2)
# [] C(3) D(2) A(2) B(1)
# [C(3) ] D(2) A(2) B(1)
# [C(3) D(2)] A(2) B(1)
# [C(3) D(2) A(2) ] B(1)
# [C(3) D(2) A(2) B(1) ]

# 1, 2, ..., n - 1, 100
# O(n ** 2) n <= 100

# priorities / location
# process = [ priority, index(location) ]
# queue에서 하나 pop
# 남아있는 모든 요소보다 priority 크다 => history에 push
# 아니다 => queue 뒤에 push

