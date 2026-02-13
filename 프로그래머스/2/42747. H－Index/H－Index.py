from bisect import bisect_left

def solution(citations):
    
    
    for i in range(10_000, -1, -1):
        count_citation = 0
        count_no_citation = 0
        for citation in citations:
            if citation >= i:
                count_citation += 1
            else:
                count_no_citation += 1
        
        if count_citation >= i and count_no_citation <= i:
            return i
        
    return 0
    

# 10_000 * 1_000 = 10_000_000
# 논문 인용 횟수 * 논문 개수
# 논문 인용 횟수가 i편 이상인 게 i개 있는지 / 나머지 논문이 i번 이하 인용되었는지 확인

# i번 이상 인용된 논문이 i편 이상이고 나머지 가 i번 이하 =>
# 0 - i - 1에 대해서도 참 => 이진탐색 가능
