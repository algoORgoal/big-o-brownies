def solution(n, lost, reserve):
    arr = [ 0 for i in range(0, n) ]
    for person in lost:
        arr[person - 1] -= 1
    for person in reserve:
        arr[person - 1] += 1
        
    
    for i, person in enumerate(arr):
        if person == 1 and i - 1 >= 0 and arr[i - 1] == -1:
            arr[i - 1] = 0
            arr[i] = 0
        elif person == 1 and i + 1 < len(arr) and arr[i + 1] == -1:
            arr[i + 1] = 0
            arr[i] = 0
    count = 0
    for i in arr:
        if i == 0 or i == 1:
            count += 1
    return count


# f(g_1) <= f(o_1)
# f(g_k) <= f(o_k)
# 1. f(o_k+1) == 
