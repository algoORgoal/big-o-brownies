from functools import cmp_to_key




def cmp(a, b):
    if len(a) == len(b):
        return int(b) - int(a)
    if len(a) > len(b):
        sliced_a = a[0:len(b)]
        if int(sliced_a) != int(b):
            return int(b) - int(sliced_a)
        else:
            return cmp(a[len(b):], b)
        
    sliced_b = b[0:len(a)]
    if int(sliced_b) != int(a):
        return int(sliced_b) - int(a)
    else:
        return cmp(a, b[len(a):])
        
def solution(numbers):
    strNumbers = [ str(number) for number in numbers ]
    
    isAllZero = all([ str == "0" for str in strNumbers])
    
    if (isAllZero):
        return "0"

    
    strNumbers.sort(key=cmp_to_key(cmp))
    return ''.join(strNumbers)
    

# 브루트포스
# 시간복잡도: O(2**n)

# dp[i][i] = a[i][i]
# dp[i][j]= max(d[i][i] + dp[i+1][j], dp[i][i + 1] + dp[i + 2][j], ..., dp[i][j-1] + dp[j][j])
# 시간복잡도: O(n^2) 10_000_000_000


# 사전순

# abc abd => abc 승
# abc abcd => abc 승
# abc abca => abc 승

# 123 1231 => 1231231 > 1231123
# 123 1234 => 1231234 < 1234123


# 길이 같으면 => 숫자 절대값 비교
# 길이 다르면 =>
#    => 짧은 것 기준으로 잘라서, 절대값 더 큰 것 선정
#    => 두 절대값이 동일하다면, 긴 것의 slice되고 첫 시작부분 앞자리와 짧은 것의 앞자리를 비교
