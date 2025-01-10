const getCollatzNumbers = (sequence) => {
    const lastNumber = sequence[sequence.length - 1];
    if (lastNumber === 1) {
        return sequence;
    }
    if (lastNumber % 2 === 0) {
        sequence.push(lastNumber / 2);
        return getCollatzNumbers(sequence);
    }
    
    sequence.push(lastNumber * 3 + 1);
    return getCollatzNumbers(sequence);
}

const getCollatzAreaTable = (sequence) => {
    return sequence.reduce((accumulator, element, index, array) => {
        if (index === 0) {
            accumulator[index] = 0;
            return accumulator;
        }
        const previousElement = array[index - 1];
        const area = (element + previousElement) / 2;
        
        accumulator[index] = accumulator[index - 1] + area;
        return accumulator;
    }, {});
}

function solution(k, ranges) {
    const collatzNumbers = getCollatzNumbers([ k ]);
    const collatzAreaTable = getCollatzAreaTable(collatzNumbers);
    const lastElementIndex = collatzNumbers.length - 1;
    const areaList = ranges.map(([ start, offset ]) => {
        const end = lastElementIndex + offset;
        if (start > end) {
            return -1;
        }
        return collatzAreaTable[lastElementIndex + offset] - collatzAreaTable[start];
    });
    
    
    return areaList;
}