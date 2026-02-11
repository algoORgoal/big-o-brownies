def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0 and i == ')':
            return False
        elif i == '(':
            stack.append(s)
        elif i == ')':
            stack.pop()
        else:
            print("에러")
        
    if len(stack) != 0:
        return False
    return True
    
# stack을 유지
# '(': append
# ')': pop

# 1. len(stack) == 0인데 ')'이 들어오는 경우
# 2. loop를 끝냈는 데 len(stack) != 0인 경우

# 시간복잡도 O(n)
# 공간복잡도 O(n)