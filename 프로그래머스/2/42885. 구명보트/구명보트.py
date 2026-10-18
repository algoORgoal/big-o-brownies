import bisect

def solution(people, limit):
    people.sort()
    
    start = 0
    end = len(people) - 1
    
    
    total = 0
    
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            total += 1
        else:
            end -= 1
            total += 1
    
    return total


# 구출된 사람의 인덱스: rescued (set)
# 1. 정렬
# 반복문(n)
# 1. 큰 사람부터 태움
# 2. 남은 kg에서 태울 수 있는 사람 중 가장 큰 사람 선택(이진탐색, logn)
# 3. rescued에 추가
# 4. total += 1

# 시간복잡도: O(nlogn)
# 공간복잡도: O(n)

# 문제점: 이미 탈출한 놈을 이진탐색에서 선택할 수 있음

# 새로운 알고리즘
# 탈출 못한 놈들 중 가장 낮은 값의 인덱스 start 기억하기
# if people[start] + people[end] <= limit:
#   start += 1
#   end -= 1
#   total += 1
# else:
#   end -= 1
#   total += 1