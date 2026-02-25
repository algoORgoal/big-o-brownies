def solution(number, k):
    digits = [ int(i)  for i in number ]
    stack = []
    for digit in digits:
        if len(stack) == 0:
            stack.append(digit)
        else:
            while len(stack) > 0 and stack[len(stack) - 1] < digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
    
    for i in range(0, k):
        stack.pop()
    return "".join([ str(i) for i in stack ])
        
    
    
    
    return answer