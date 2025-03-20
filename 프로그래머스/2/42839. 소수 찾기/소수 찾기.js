// 각 숫자를 쪼개기
// 방문되지 않은 index에 대해서 탐색

function isPrime(num) {
    if (num === 0) return false;
    if (num === 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

function dfs(numbers) {
    console.log(numbers);
    const root = "";
    const bitmask = 0;
    const stack = [];
    stack.push([ root, bitmask ]);
    const visited = new Set();
    while (stack.length) {
        const [ current, bitmask ] = stack.pop();
        visited.add(current);
        for (let i = 0; i < numbers.length; i++) {
            if ((bitmask & (1 << i)) === 0) {
                stack.push([ current + numbers[i], (bitmask | (1 << i)) ]);
            }
        }
    }
    const visitedNumbers = [ ...visited ].reduce((acc, numberStr) => {
        if (numberStr === "") return acc;
        const number = Number(numberStr);
        acc.add(number);
        return acc;
    }, new Set());
    return [ ...visitedNumbers ].filter((number) => isPrime(number)).length;
}

function solution(numberStr) {
    const numbers = numberStr.split('');
    return dfs(numbers);
}
