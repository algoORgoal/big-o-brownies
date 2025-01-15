function solution(elements) {
    const sumSet = new Set();
    const memo = Array.from({ length: elements.length }, () => Array.from({ length: elements.length}).fill(0));
    
    for (let i = 0; i < elements.length; i++) {
        for (let j = 0; j < elements.length; j++) {
            if (i === 0) {
                memo[i][j] = elements[j];
                sumSet.add(memo[i][j]);
            } else {
                memo[i][j] = memo[i - 1][j] + elements[(i + j) % elements.length];
                sumSet.add(memo[i][j]);
            }
        }
    }
    
    return sumSet.size;
}