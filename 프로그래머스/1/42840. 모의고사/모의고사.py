def solution(answers):
    tester_1_pattern = [ 1, 2, 3, 4, 5 ]
    tester_2_pattern = [ 2, 1, 2, 3, 2, 4, 2, 5 ]
    tester_3_pattern = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ]
    
    tester_1_score = 0
    tester_2_score = 0
    tester_3_score = 0
    
    for index, answer in enumerate(answers):
        tester_1_choice = tester_1_pattern[index % len(tester_1_pattern)]
        tester_2_choice = tester_2_pattern[index % len(tester_2_pattern)]
        tester_3_choice = tester_3_pattern[index % len(tester_3_pattern)]
        
        if tester_1_choice == answer:
            tester_1_score += 1
        if tester_2_choice == answer:
            tester_2_score += 1
        if tester_3_choice == answer:
            tester_3_score += 1
    
    result = []
    scores = [ tester_1_score, tester_2_score, tester_3_score ]
    max_score = max(scores)
    for index, score in enumerate(scores):
        if score == max_score:
            result.append(index + 1)
    return result
    