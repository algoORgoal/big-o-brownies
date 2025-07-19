function solution(s){
    const stack = [];
    
    for (char of s.split("")) {
        if (stack.length === 0 && char === ')') {
            return false;
        }
        else if (char === '(') stack.push(char)
        else stack.pop();
    }
    
    if (stack.length > 0) return false;
    
    return true;
}


// stack에 '('일 때는 요소를 삽입 / ')'일 때는 요소를 삭제
// stack이 비어있는 상태인데 ')'일 경우 false
// stack이 비어있지 않다면 false
// 시간복잡도: O(n)
