function solution(a, b, g, s, w, t) {
    return binarySearch({
        required: [ a, b ],
        goldQuantities: g,
        silverQuantities: s,
        weights: w,
        times: t,
    });
}

function binarySearch(deliveryPlan, upperbound = 1_000_000_000_000_000) {
    // a, b = 1_000_000_000
    // g.length = s.length = w.lenght = t.length = 1, g[0] = 1, s[1] = 1
    // O(max(a, b));
    // log(max(a, b) / min(g[i] + s[i]))
    let [ start, end ] = [ 0, upperbound ];
    
    while (start !== end) {
        const middle = Math.floor((start + end) / 2);
        if (canLoadTargetQuantity(deliveryPlan, middle)) {
            end = middle;
            continue;
        }
        start = middle + 1;
    }
    
    return start;
}
    
function canLoadTargetQuantity(deliveryPlan, current) {
    const { required, goldQuantities, silverQuantities, weights, times } = deliveryPlan;
    const capacities = times.map((time, index) => {
        if (current < time) {
            return {
                maxGold: 0,
                maxSilver: 0,
                maxTotal: 0,
            };
        }
        const deliveryCount = Math.floor((current - time) / (2 * time)) + 1;
        const maxGold = Math.min(deliveryCount * weights[index], goldQuantities[index]);
        const maxSilver = Math.min(deliveryCount * weights[index], silverQuantities[index]);
        const maxTotal = Math.min(deliveryCount * weights[index], goldQuantities[index] + silverQuantities[index]);
        return {
            maxGold,
            maxSilver,
            maxTotal,
        };
    });
    
    const { maxGold, maxSilver, maxTotal } = capacities.reduce((accumulator, { maxGold, maxSilver, maxTotal }) => {
        return {
            maxGold: accumulator.maxGold + maxGold,
            maxSilver: accumulator.maxSilver + maxSilver,
            maxTotal: accumulator.maxTotal + maxTotal,
        };
    }, {
        maxGold: 0,
        maxSilver: 0,
        maxTotal: 0,
    });
    
    const [ requiredGold, requiredSilver ] = required;
    return maxGold >= requiredGold && maxSilver >= requiredSilver && maxTotal >= requiredGold + requiredSilver;
}