def solution(arr):
    stack = []
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            top = stack[len(stack) - 1]
            if top != i:
                stack.append(i)
    return stack
            