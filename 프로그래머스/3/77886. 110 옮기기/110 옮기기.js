function solution(strings) {
    const result = strings.map((string) => {
        const stack = [];
        let patternCount = 0;
        [ ...string ].forEach((char) => {
            stack.push(char);
            const top = stack.length - 1;
            if (stack.length >= 3 && stack[top - 2] === "1" && stack[top - 1] === "1" && stack[top] === "0") {
                stack.pop();
                stack.pop();
                stack.pop();
                patternCount += 1;
            }
        });
        
        const filtered = stack.join('');
        const lastIndex = filtered.lastIndexOf("0");
        return filtered.slice(0, lastIndex + 1) + "110".repeat(patternCount) + filtered.slice(lastIndex + 1);
        
    });
    
    return result;
}