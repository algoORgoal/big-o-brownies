function canEnter(n, times, duration) {
    const capacity = times.reduce((accumulator, time) => accumulator + Math.floor(duration / time), 0);
    return capacity >= n;
}

function binarySearch(n, times) {
    let [ start, end ] = [ 0, 10_000_000_000_000_000 ];
    while (start !== end) {
        const middle = Math.floor((start + end) / 2);
        if (canEnter(n, times, middle)) { 
            end = middle;
            continue;
        }
        start = middle + 1;
    }
    return start;
}

function solution(n, times) {
    return binarySearch(n, times);
}







