// Bruteforce: exploring every possible state
// it runs in O(n^2) time
// 

function solution(s)
{
    let maximum = -Infinity;
    let count = 0; 
    for (let i = 0; i < s.length; i++) {
        for (let j = 0; i + j < s.length && i - j >= 0; j++) {
            if (j === 0) {
                count += 1;
                continue;
            }
            if (s[i + j] !== s[i - j]) break;
            count += 2;
            
        }
        maximum = Math.max(maximum, count);
        count = 0;
    }
    
    
    for (let i = 0; i < s.length; i++) {
        for (let j = 0; i + j + 1 < s.length && i - j >= 0; j++) {
            const pair = [ i - j, i + j + 1 ];
            if (s[pair[0]] !== s[pair[1]]) break;
            count += 2;   
        }
        maximum = Math.max(maximum, count);
        count = 0;
    }
    
    return maximum;
}