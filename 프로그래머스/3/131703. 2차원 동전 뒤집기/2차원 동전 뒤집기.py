from math import inf

def solution(beginning, target):
    result = dfs(0, 0, 0, beginning, target)
    if result == inf:
        return -1
    return result
    

def check_is_same(matrix, target):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] != target[i][j]:
                return False
    
    return True

def dfs(row_count, col_count, switch_count, matrix, target):
    
    if (row_count == len(matrix) and col_count == len(matrix[0])):
        is_same = check_is_same(matrix, target)
        if is_same:
            return switch_count
        else:
            return inf
    
    min_count = inf
    
    if row_count < len(matrix):
        for i in range(0, len(matrix[0])):
            matrix[row_count][i] ^= 1
        min_count = min(min_count, dfs(row_count + 1, col_count, switch_count + 1, matrix, target))
        for i in range(0, len(matrix[0])):
            matrix[row_count][i] ^= 1
        
        min_count = min(min_count, dfs(row_count + 1, col_count, switch_count, matrix, target))
        return min_count
    else:
        for i in range(0, len(matrix)):
            matrix[i][col_count] ^= 1
        min_count = min(min_count, dfs(row_count, col_count + 1, switch_count + 1, matrix, target))
        for i in range(0, len(matrix)):
            matrix[i][col_count] ^= 1
            
        min_count = min(min_count, dfs(row_count, col_count + 1, switch_count, matrix, target))
        return min_count
    
    
    

    
    
    
            
        
        
    
    
                
    
                
    
                
    
    
    dfs(row_count,)
    

# 초기상태: 10111
# 목표상태: 11100