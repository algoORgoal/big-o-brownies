def solution(n, words):
    past_words = set()
    
    past_word = ""
    
    for i in range(len(words)):
        person = (i % n) + 1
        round = (i // n) + 1
        
        if words[i] in past_words:
            return [person, round]
        
        if i > 0 and past_word[-1] != words[i][0]:
            return [person, round]
        
        past_word = words[i]
        past_words.add(words[i])
        
        
    return [0, 0]


    return answer


# 1. 현재 나왔던 단어들을 집합에 저장
# 2. (현재 단어의 인덱스 % 사람 수) + 1 = 현재 단어를 말하는 사람의 번호
# 3. (현재 단어의 인덱스 // 사람 수) + 1 = 현재 round

# words 배열의 길이 = n <= 100
# 시간복잡도 O(n)
# 공간복잡도 O(n)