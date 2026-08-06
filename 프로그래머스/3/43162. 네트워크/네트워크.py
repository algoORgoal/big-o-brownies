from collections import deque
def solution(n, computers):
    answer = 0
    
    # BFS 메서드 정의
    def bfs(graph, start, visited):
        queue = deque([start])
        
        visited[start] = True
        while len(queue)>0:
            v = queue.popleft()
            for node, edge in enumerate(graph[v]):
                print(v, node, edge)
                if (not visited[node]) and edge==1:
                    queue.append(node)
                    visited[node] = True
    
    visited = [False]*n
    
    
    for i in range(0,n):
        if visited[i] == False:
            bfs(computers, i ,visited)
            answer+=1
        
    
    return answer


