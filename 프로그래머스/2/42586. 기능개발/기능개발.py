from math import ceil

def solution(progresses, speeds):
    timeline_pairs = list(zip(progresses, speeds))
    timeline = []
    for progress, speed in timeline_pairs:
        time = ceil((100 - progress) / speed);
        timeline.append(time)
    stack = []
    
    for time in timeline:
        if len(stack) == 0:
            stack.append([ time, 1 ])
        else:
            top = stack[len(stack) - 1]
            if top[0] >= time:
                top[1] += 1
            else:
                stack.append([ time, 1 ])
    
    return [ count for time, count in stack ]
    

# 30 1 3 5 3 1
# [ [ 30, 1 ] ] 1 30 배포할 때 같이
# [ [ 30, 2 ] ] 3 30 배포할 때 같이
# [ [ 30, 3 ] ] 5 30 배포할 때 같이
# [ [ 30, 4 ] ] 3 30 배포할 때 같이
# [ [ 30, 5 ] ] 1 30 배포할 때 같이
# top과 비교해서, 같거나 작으면 같이 배포
