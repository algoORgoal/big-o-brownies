from collections import deque

def solution(word):
    sorted_word_list = bfs()
    for i, candidate in enumerate(sorted_word_list):
        if candidate == word:
            return i
    


def bfs():
    queue = deque()
    queue.append('')
    
    visited = set()
    
    while len(queue) > 0:
        node = queue.popleft()
        
        if node in visited:
            continue
            
        visited.add(node)
        
        if len(node) < 5:
            for char in [ 'A' , 'E' , 'I', 'O', 'U' ]:
                adjacent_node = node + char
                queue.append(adjacent_node)
    
    return sorted(visited)
        
        
    
    