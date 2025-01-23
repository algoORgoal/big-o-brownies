function solution(n, left, right) {
    const stack = [];
    for (let i = left; i <= right; i++) {
        const [ x, y ] = [ Math.floor(i / n), i % n ];
        stack.push(Math.max(x, y) + 1);
    }
    return stack;
}