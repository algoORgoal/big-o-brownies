const findGcd = (num1, num2) => {
    if (num1 < num2) [num1, num2] = [num2, num1];
    while (num2 !== 0) {
        [num1, num2] = [num2, num1 % num2];
    }
    return num1;
};

const findArrayGcd = (args) => args.reduce((accumulator, num) => findGcd(accumulator, num));

function solution(arrayA, arrayB) {
    const gcdA = findArrayGcd(arrayA);
    const gcdB = findArrayGcd(arrayB);
    const isGcdADividable = arrayB.some((element) => element % gcdA === 0);
    const isGcdBDividable = arrayA.some((element) => element % gcdB === 0);
    if (!isGcdADividable && !isGcdBDividable) {
        return Math.max(gcdA, gcdB)
    }
    if (!isGcdADividable) {
        return gcdA;
    }
    if (!isGcdBDividable) {
        return gcdB;
    }
    return 0;
}