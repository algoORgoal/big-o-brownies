const findGcd = (num1, num2) => {
    if (num1 < num2) [num1, num2] = [num2, num1];
    while (num2 !== 0) {
        [num1, num2] = [num2, num1 % num2];
    }
    return num1;
};

const findArrayGcd = (arr) => arr.reduce(findGcd);

function solution(arrayA, arrayB) {
    const gcdA = findArrayGcd(arrayA);
    const gcdB = findArrayGcd(arrayB);

    const canDivide = (array, gcd) => array.every((num) => num % gcd === 0);
    const cannotDivide = (array, gcd) => array.every((num) => num % gcd !== 0);

    let result = 0;

    if (canDivide(arrayA, gcdA) && cannotDivide(arrayB, gcdA)) {
        result = Math.max(result, gcdA);
    }
    if (canDivide(arrayB, gcdB) && cannotDivide(arrayA, gcdB)) {
        result = Math.max(result, gcdB);
    }

    return result;
}