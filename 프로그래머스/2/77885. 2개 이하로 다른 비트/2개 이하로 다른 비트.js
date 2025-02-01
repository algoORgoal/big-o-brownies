function solution(numbers) {
    const binaryStirngNumbers = numbers.map((number) => number.toString(2).padStart(50, '0'));
    
    const largerBinaryStringNumbers = binaryStirngNumbers.map((binaryString) => {
        const lsb0Index = binaryString.length - 1 - [ ...binaryString ].reverse().findIndex((character) => character === '0');
        if (lsb0Index === binaryString.length - 1) {
            return binaryString.slice(0, lsb0Index).concat('1');
        }
        
        const msb1Index = lsb0Index + 1 + [ ...binaryString.slice(lsb0Index + 1) ].findIndex((character) => character === '1');
        
        if (msb1Index === -1) {
            console.log("??")
            return binaryString.slice(0, lsb0Index).concat('1').concat(binaryString.slice(lsb0Index + 1));
        }
        
        return binaryString.slice(0, lsb0Index).concat('1').concat(binaryString.slice(lsb0Index + 1, msb1Index), '0', binaryString.slice(msb1Index + 1));
    });
    
    const largerNumbers = largerBinaryStringNumbers.map((binaryStringNumber) => parseInt(binaryStringNumber, 2));
    
    return largerNumbers;
    
}