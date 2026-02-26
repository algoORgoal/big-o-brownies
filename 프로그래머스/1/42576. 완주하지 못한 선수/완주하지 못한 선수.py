def solution(participant, completion):
    table = {}
    for runner in participant:
        if runner not in table:
            table[runner] = 0
        table[runner] += 1
    
    for runner in completion:
        table[runner] -= 1
    
    for i in table:
        if table[i] > 0:
            return i
        
    return ""