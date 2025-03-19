// 110을 모두 제거했을 때, 남은 0 앞에 있는 수는 00 || 01 || 10이므로,
// 110을 뒤에 붙였을 때가 110을 앞에 붙였을 때보다 사전순으로 앞선다.
// 가장 마지막 0 뒤에 나오는 모든 수는 1이므로, 0 바로 뒤에 110을 붙이는 것이 사전 순으로 아펏ㄴ다.
// 사전 순으로 가장 앞서기 위해서는 가장 마지막에 나온 0 뒤에다가 붙여야 한다.
// string 구간 산정하고 새로운 string 만들기
// 만든 string 안에서 가장 마지막 0 찾고 거기에 110 붙이기

function solution(strings) {
    
    const answer = [];
    for (let str of strings) {
        const stack = [];
        let patternCount = 0;
        for (let char of str) {
            stack.push(char);
            const top = stack.length - 1;
            if (stack[top - 2] === "1" && stack[top - 1] === "1" && stack[top] === "0") {
                stack.pop();
                stack.pop();
                stack.pop();
                patternCount += 1;
            }
        }
        const filtered = stack.join("");
        const lastIndex = filtered.lastIndexOf("0");
        const result = filtered.slice(0, lastIndex + 1) + "110".repeat(patternCount) + filtered.slice(lastIndex + 1);
        answer.push(result);
    }
    
    return answer;
}