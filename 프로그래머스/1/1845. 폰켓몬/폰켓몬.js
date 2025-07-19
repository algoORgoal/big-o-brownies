function solution(nums) {
    const table = nums.reduce((acc, num) => {
        if (!acc.has(num)) acc.set(num, 0);
        acc.set(num, acc.get(num) + 1);
        return acc;
    }, new Map());
    return [ ...table ].reduce((acc, pair) => {
        if (acc == nums.length / 2) {
            return acc;
        }
        return acc + 1;
    }, 0);
}

// 각 요소의 출현 횟수를 카운트
// key를 바탕으로 각 key별로 1 추가
// 2/n에 도달한 경우 더이상 추가 X
// 시간복잡도: O(n)