function solution(s) {
    return binaryConvert(s);
}


function binaryConvert(s, conversionCount = 0, zeroCount = 0) {
    if (s === '1') {
        return [ conversionCount, zeroCount ];
    }
    const oneCount = [ ...s ].reduce((accumulator, character) => character === "1" ? accumulator + 1 : accumulator, 0);
    const removedZeroCount = s.length - oneCount;
    const convertedString = oneCount.toString(2);
    return binaryConvert(convertedString, conversionCount + 1, zeroCount + removedZeroCount);
}