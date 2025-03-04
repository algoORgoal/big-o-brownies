// available[i] = max(stones[i - k + 1], stones[i - k + 2], ..., stones[i])  (i >= k - 1)
// 주변 i - k + 1, i - k + 2, i번째까지의 돌 중 하나가 존재하는 동안 해당 칸을 건널 수 있다.
// available[i] = max(stones[i], stones[i + 1], ..., stones[i + k - 1])
// k <= n이므로 그대로 실행하면 O(n^2)의 시간복잡도를 가진다.
// 따라서, 이진탐색을 사용하여 O(nlogn)의 시간복잡도로 줄인다.

// i, i + k - 1 이내에서 이진탐색을 활용하여 최댓값을 구해야 한다.

// binary search takes => O(log m) , m <= 200_000_000

function binarySearch(stones, k) {
    let maxStone = 0;
    for (const stone of stones) {
        maxStone = Math.max(maxStone, stone);
    }
    let [ left, right ] = [ 0, maxStone ];
    while (left < right) {
        const mid = Math.ceil((left + right) / 2);
        
        if (canCross(stones, k, mid)) {
            left = mid;
            continue;
        }
        right = mid - 1;
    }
    return left;
}

function canCross(stones, k, mid) {
    let zeroCount = 0;
    for (const stone of stones) {
        if (stone - mid < 0) {
            zeroCount++;
            if (zeroCount >= k) return false;
        } else {
            zeroCount = 0;
        }
    }
    return true;
}

 

function solution(stones, k) {
    return binarySearch(stones, k);
}