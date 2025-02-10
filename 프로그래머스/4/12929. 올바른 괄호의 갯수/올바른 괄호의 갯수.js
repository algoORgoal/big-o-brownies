function solution(n) {
    const root = "()";
    const stack = [ root ];
    let count = 0;
    
    function backtrack(current, open, close) {
        if (current.length === 2 * n) {
            count++;
            return;
        }
        if (open < n) {
            backtrack(current + "(", open + 1, close);
        }
        if (close < open) {
            backtrack(current + ")", open, close + 1);
        }
        return count;
    }
    
    backtrack("", 0, 0);
    return count;

    
}