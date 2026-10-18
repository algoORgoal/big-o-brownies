def solution(phoneBook):
    phoneBook.sort()
    
    for i in range(len(phoneBook) - 1):
        current, after = phoneBook[i], phoneBook[i + 1]
        if after.startswith(current):
            return False
    
    return True
    
    
# 각 문자열이 다른 문자열의 접두어가 되는지 확인
# 각 단어를 다른 모든 단어와 비교 => O(n ** 2) (n <= 1_000_000) => 시간초과
#
# 정렬 => 다음 단어가 접두어인지 확인
# 다음 단어의 접두어가 되지 못한다 => 전체 문자열에 접두어 없음
# 119, 1192, 1193가 있음 => 119로 시작하는 단어는 무조건 119 다음에 연속으로 온다. (사전순 정렬의 정의)

# 사전순 정렬의 정의?
# 1. 길이 짧은 것부터
# 2. 크기 작은 순으로
# 3. 해당 substring으로 시작하는 것중 크기 가장 작은 것부터

    