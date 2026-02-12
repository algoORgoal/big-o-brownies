from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    waiting_trucks = deque(truck_weights)
    on_bridge_timeline = deque()
    weight_sum = 0
    
    while len(waiting_trucks) > 0 or len(on_bridge_timeline) > 0:
        time += 1
        
        for i in range(0, len(on_bridge_timeline)):
            on_bridge_timeline[i][1] += 1
    
        if len(on_bridge_timeline) > 0:
            last_on_bridge_truck, last_on_bridge_time  = on_bridge_timeline[len(on_bridge_timeline) - 1]
            if last_on_bridge_time == bridge_length:
                on_bridge_timeline.pop()
                weight_sum -= last_on_bridge_truck
        
        if len(waiting_trucks) > 0:
            first_waiting_truck = waiting_trucks[0]
            if weight_sum + first_waiting_truck <= weight:
                waiting_trucks.popleft()
                on_bridge_timeline.appendleft([ first_waiting_truck, 0 ])
                weight_sum += first_waiting_truck

            
        
        
                
        
    return time    



# 10_000 * 10_000 = 100_000_0000
# 10초 => 대략 가능

# 각 시간마다:
# 각 다리를 지나는 트럭에 대해:
#  마지막 위치에 있는 것 제거
#  현재 위치를 1 증가시킴

#  현재 무게 합 + 다음 트럭 가능하면 첫번째에 올려놓음
# 다리를 지나는 트럭 개수 == 0, 대기 트럭 개수 == 0인 시간 반환