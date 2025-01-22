const isPrime = (n) => {
    if (n === 1) {
        return false;
    }
    
    for(let i = 2; i <= Math.sqrt(n); i++ ){
        if (n % i === 0) return false;
    }
    
    return true;
}

function solution(n, k) {
    const numberList = n.toString(k).replace(/^0+|0+$/g, '').split(/0+/).map((numberString) => Number(numberString));
    const primeCount = numberList.filter((number) => isPrime(number)).length;
    return primeCount;
}
