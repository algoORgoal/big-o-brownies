from collections import deque

def solution(people, limit):
    
    sorted_people = sorted(people, reverse = True)
    elements = deque(sorted_people)
    
    count = 0
    while len(elements) > 0:
        first = elements.popleft()
        if len(elements) > 0 and first + elements[len(elements) - 1] <= limit:
            second = elements.pop()
        count += 1
        
    return count
        
    
#     partners = set()
#     count = 0
#     for index, person_weight in enumerate(sorted_people):
#         if index in partners:
#             continue
#         rest = limit - person_weight
#         target = bisect_left(sorted_people, rest)
#         print(person_weight, target, sorted_people[target], rest)
#         count += 1
    


# 25 * 10 ** 8 => 25억: O(n^2) 시간초과

# 50 50 70 80

# arr 정렬  nlogn (n <= 50_000)
# while arr is not empty:
#   element = arr.deque
#   rest = capacity - element
#   find biggest i such that i <= rest
#   문제: arr에 중복값이 있을 수 있음

# 내림차순으로 정렬 후,
# 각 요소에 대하 popleft할 때 가장 작은 것도 같이 담을 수 있으면 담기
# exchange argument
# a0, ai
# ai가 들어가는 곳에 bi가 들어간다고 하면, ai와 bi를 교체 가능






