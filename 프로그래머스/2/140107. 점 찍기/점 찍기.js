function solution(k, d) {
    let total = 0;
    for (let b = 0; Math.sqrt(Math.pow(d / k, 2) - Math.pow(b, 2)) >= 0; b++) {
        total += (Math.floor(Math.sqrt(Math.floor(Math.pow(d / k, 2) - Math.pow(b, 2)))) + 1);
    } 
    return total;
} 