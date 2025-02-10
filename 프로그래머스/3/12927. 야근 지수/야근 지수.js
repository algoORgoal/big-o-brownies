function solution(n, works) {
    const lowerBound = binarySearch(n, works);
    const cost = calculateCost(works, lowerBound);
    if (cost < n) {
        const left = n - cost;
        const reducedWorks = works.map((work) => lowerBound < work ? lowerBound : work);
        const { extraReducedWorks } = reducedWorks.reduce((accumulator, work) => {
            if (accumulator.left > 0 && work === lowerBound && work >= 1) {
                accumulator.left -= 1;
                accumulator.extraReducedWorks.push(work - 1);
                return accumulator;
            }
            accumulator.extraReducedWorks.push(work);
            return accumulator;
        }, {
            left,
            extraReducedWorks: [],
        });
        const minimizedSum = extraReducedWorks.reduce((accumulator, work) => accumulator + work * work, 0);
        return minimizedSum;
    }
    
    const reducedWorks = works.map((work) => lowerBound < work ? lowerBound : work);
    const minimizedSum = reducedWorks.reduce((accumulator, work) => accumulator + work * work, 0);
    return minimizedSum;
    
}

function binarySearch(n, works) {
    let [ start, end ] = [ 0, 50_000 ];
    
    while (start !== end) {
        const middle = Math.floor((start + end) / 2);
        if (canFormValue(works, n, middle)) {
            end = middle;
            continue;
        }
        start = middle + 1;
    }   
    return start;
}

const calculateCost = (works, value) => works.reduce((accumulator, work) => {
    if (value < work) {
        return accumulator + (work - value);
    }
    return accumulator;
}, 0);
    
function canFormValue(works, n, value) {
    const sum = calculateCost(works, value);
    return sum <= n;
}

// a, b such that a < b,
// a^2 - (a-1)^2 < b^2 - (b-1) ^ 2
// 2a - 1 < 2b - 1
// Therefore, always lower down the biggest number first
// Using binary search, check find minimum m that every element can form using n
// the maximum value of element: s, the length of array t     t log(s)
