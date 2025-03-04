// available[i] = max(stones[i - k + 1], stones[i - k + 2], ..., stones[i])  (i >= k - 1)
// 주변 i - k + 1, i - k + 2, i번째까지의 돌 중 하나가 존재하는 동안 해당 칸을 건널 수 있다.
// available[i] = max(stones[i], stones[i + 1], ..., stones[i + k - 1])
// k <= n이므로 그대로 실행하면 O(n^2)의 시간복잡도를 가진다.
// 따라서, 이진탐색을 사용하여 O(nlogn)의 시간복잡도로 줄인다.


function binarySearch(stones, ) {
    
}

function solution(stones, k) {
    const available = Array.from({ length: stones.length }, () => 0);
    const table = stones.reduce((accumulator, stone, index) => {
        if (!(stone in accumulator)) accumulator[stone] = new Set();
        accumulator[stone].add(index);
        return accumulator;
    }, {});
    console.log(table);
//     for (let i = 0; i < stones.length - k +  1;){
//         let maxIndex = i + 1;
//         for (let j = 0; j < k; j++) {
//             if (stones[i + j] > available[i]) {
//                 available[i] = Math.max(available[i], stones[i + j]);
//                 maxIndex = i + j;      
//             }
//         }
//         i = maxIndex;
//     }
    
//     let minimum = available[0];
//     for (let i = 0; i < available.length; i++) {
//         if (available[i] === 0) continue;
//         if (minimum > available[i]) minimum = available[i];
//     }
//     return minimum;
}