def solution(prices):
    time_lapse_map = {}
    stack = []

    for index in range(0, len(prices)):
        time = index + 1
        price = prices[index]
        
        while (len(stack) > 0 and stack[len(stack) - 1][0] > price):
            last_price, last_time = stack.pop()
            diff = (time - last_time)
            time_lapse_map[last_time] = diff
            
        stack.append([price, time])
        
         
    while len(stack) > 0:
        price, time = stack.pop()
        diff = len(prices) - time
        time_lapse_map[time] = diff
    
    result = [ time_lapse_map[time] for time in range(1, len(prices) + 1)]
    
    return result
        
    
        
        
        

    
    
    
            


    
#     originalIndex = len(prices) - 1
#     smallestIndex = originalIndex
#     smallest = prices[smallestIndex]
#     answer = []
    
#     while(prices):
#         element = prices.pop()
#         elementIndex = len(prices)
#         if (element <= smallest): 
#             smallest = element
#             smallestIndex = elementIndex
#             answer.insert(0, originalIndex - elementIndex)
#         else:
#             answer.insert(0, smallestIndex - elementIndex)
#     return answer