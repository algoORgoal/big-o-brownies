memo = {}

def solution(triangle):
    return dfs(triangle, 0, 0)

def dfs(triangle, depth, index):
    if (depth, index) in memo:
        return memo[(depth, index,)]
    if depth == len(triangle) - 1:
        memo[(depth, index,)] = triangle[depth][index]
        return memo[(depth, index,)]
    
    left_subtree_max = dfs(triangle, depth + 1, index)
    right_subtree_max = dfs(triangle, depth + 1, index + 1)
    memo[(depth, index,)] = triangle[depth][index] + max(left_subtree_max, right_subtree_max)
    return memo[(depth, index,)]
    
    

# triangle[depth][index] + max(왼쪽 서브트리 최댓값, 오른쪽 서브트리 최댓값)
# 탐색 공간 안 노드의 수: 2 ** 500
# 특정 노트에서의 트리 최댓값을 캐싱 => 500