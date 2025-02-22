// pulse series either multiples [ -1, 1, -1, ... ] or [ 1, -1, 1, ... ]
// multiply sequence by pulse serie(both)
// find the largest subsequence sum using prefix sum
// 32byte * 1_500_000 = 48MB => 

const getPulseSum = (sequence, isEven) => sequence.reduce((accumulator, element, index) => {
    const sign = (isEven && index % 2 === 0) || (!isEven && index % 2 === 1) ? 1 : -1;
    const resolvedElement = element * sign;
    if (index === 0) {
        accumulator = {
            value: resolvedElement,
            best: resolvedElement,
            worst: resolvedElement,
        };
        return accumulator;
    }
    accumulator.value = accumulator.value + resolvedElement;
    accumulator.best = Math.max(accumulator.best, accumulator.value);
    accumulator.worst = Math.min(accumulator.worst, accumulator.value);
    return accumulator;
}, {
    value: 0,
    best: 0,
    worst: 0,
});

function solution(sequence) {
    const pulseSumInfo1 = getPulseSum(sequence, true);
    const pulseSumInfo2 = getPulseSum(sequence, false);
    const largestSum1 = pulseSumInfo1.best - Math.min(pulseSumInfo1.worst, 0);
    const largestSum2 = pulseSumInfo2.best - Math.min(pulseSumInfo2.worst, 0);
    return Math.max(largestSum1, largestSum2);
}
