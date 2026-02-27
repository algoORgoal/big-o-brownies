from collections import deque

def solution(tickets):
    graph = {}
    for source, destination in tickets:
        if source not in graph:
            graph[source] = []
        graph[source].append(destination)
    for vertex in graph:
        graph[vertex] = deque(sorted(graph[vertex]))
    
    stack = []
    dfs("ICN", graph, stack)
    
    stack.reverse()
    
    return stack


def dfs(current, graph, stack):
    if current in graph:
        while len(graph[current]) > 0:
            next_node = graph[current].popleft()
            dfs(next_node, graph, stack)
    stack.append(current)
        
    
    
    
    
    
    
    

# SFO -> ATL -> SFO -> ICN -> ATL -> ICN

# 오일러 경로를 찾는 문제
# 오일러 경로의 조건: 모두 짝수이거나, 두개 홀수 빼고 전부 짝수

# 사이클이 생겼을 때 처리를 잘 해줘야할 듯
# 뭔가 거꾸로 넣어진 순서를 뒤집어야 했던 것은 기억함
# 9 8 7 6 5 10 9 8 7 6 5 4 3 2 1
# post order traversal일 경우

# 


# ICN - JFK - HND - IAD
# IAD - HND - JFK - ICN

# 

# {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
# ICN - ATL - SFO - ICN
# 

# ICN - ATL - SFO - ATL 
# ICN - 

# ICN - ATL
# [ SFO ]

# ICN - SFO - ATL
# [ SFO ATL ]


# 일직선으로 갔다가 -> 사이클 쪽 숫자가 작아서 거기서 한번 돌고 -> 다시 일직선
# 일직선으로 갔다가 -> 일직선 쪽 숫자가 작아서 일직선 한번 가고 -> 사이클 돌기

# - 숫자가 작든 크든 일직선 -> 사이클 -> 일직선이 정답이다.
# - 막혀서 갈 곳 없을 때까지 돌고, 막히면 pop시키기
# - 막히는 기준: edge 전부 다 사용했는가?