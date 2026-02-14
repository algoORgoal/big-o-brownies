from itertools import permutations

def solution(numbers):
    number_set = set()
    number_list = [ number for number in numbers ]
    for i in range(1, len(numbers) + 1):
        for number_tuple in permutations(number_list, i):
            number = int(''.join(number_tuple))
            number_set.add(number)
            
    count = 0
    for number in number_set:
        if isPrime(number):
            count += 1
    return count
    
    
    
    
    answer = 0
    return answer

def generateNumber(str):
    if str == "":
        return []
    result = []
    for index, character in enumerate(str):
        print(character)
        result += [ character + token for token in generateNumber(str[0:index] + str[index + 1:]) ]
        
    
    return result
        
def isPrime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# 7! = 5040
# 1! + ... + 7! = 5913
# 5913개의 숫자에 대해 소수인지 확인 => O(n^2)
