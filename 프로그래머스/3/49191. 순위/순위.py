def solution(n, results):
    graph = {}
    reversed_graph = {}
    nodes = set([ i for i in range(1, n + 1) ])
    
    for source, destination in results:
        if source not in graph:
            graph[source] = []
        if destination not in reversed_graph:
            reversed_graph[destination] = []
        graph[source].append(destination)
        reversed_graph[destination].append(source)
    
        
    children_table = get_children_table(graph, nodes)
    parent_table = get_children_table(reversed_graph, nodes)
    
    
    # 한번 visited된건 다시 visited하면 안 됌.
    # 예: 4 => 3 => 2, 4 => 2 둘 다 가능
    # visited 유지할 경우 조상 개수는 업데이트해주기 힘듦. 왜냐하면 매번 조상 방문했을 때 visited된 후손까지 업데이트해줘야 하기 때문
    # 후손 개수만 제대로 세보자
    # 근데 후손 개수 셀때도 4는 3, 2 중에 3만 골라야 함
    # 해답: 3이 reachable하는 노드 set, 2에서 recahble하는 노드 set 별도로 가지고 있자.
    
    count = 0
    for node in nodes:
        if len(children_table[node]) + len(parent_table[node]) == n - 1:
            count += 1
    return count
            
    
    
    
    
    answer = 0
    return answer

def get_children_table(graph, nodes):
    children_table = {}
    visited = set()
    for node in nodes:
        visited.add(node)
        dfs(graph, node, visited, children_table)
    return children_table
    

def dfs(graph, current, visited, children_table):
    if current in graph:
        adjacent_nodes = graph[current]

        children_table[current] = set()
        for adjacent_node in adjacent_nodes:
            if adjacent_node in visited:
                children_table[current] = children_table[current] | set([ adjacent_node ])
                children_table[current] = children_table[current] | children_table[adjacent_node]
                continue
            visited.add(adjacent_node)
            dfs(graph, adjacent_node, visited, children_table)
            children_table[current] = children_table[current] | set([ adjacent_node ])
            children_table[current] = children_table[current] | children_table[adjacent_node]
    else:
        children_table[current] = set()
        
        
        

    


# 방향성이 있는데 사이클이 없음 => DAG
# dag에서, 조상 노드가 몇개 있고 자손 노드가 몇개 있는지 세야하는 문제
# 일반 위상 정렬을 했을 때, 항상 왼쪽 => 오른쪽으로 방향성 보장
# 방향성만으로는 부족하다.




# ingree 0인 노드들에 대해서 모두 dfs를 수행
# 4 => 3 => 2 => 5
# 4 => 2
# 1 => 2
# if 앞에 있는 노드 개수 + 뒤에 있는 노드 == n - 1
#   count += 1