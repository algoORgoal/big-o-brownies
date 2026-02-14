from itertools import product

def solution(word):
    
    alphabet = ["A", "E", "I", "O", "U"]
    
    
    words = []
    for i in range(1, 6):
        words +=  [ ''.join(array) for array in list(product(alphabet, repeat=i)) ]
    words.sort()
    
    for index, w in enumerate(words):
        if word == w:
            return index + 1
    
    
    return -1
    
    
    

    
    



# 5 ** 1 + ... + 5 ** 5 = 3905
# 만들 수 있는 상태를 모두 만들고, 정렬한다. 그리고 몇번째 인덱스인지 찾고 + 1를 더한다.