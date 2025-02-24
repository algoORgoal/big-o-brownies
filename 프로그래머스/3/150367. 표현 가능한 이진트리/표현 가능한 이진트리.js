// binary tree => full binary tree => binary representation of a number => dicimal number
// full binary tree always has a 2^k - number of elements
// pad the minimal number of zeros to get a full binary tree representation
// check if any child is 1 while the parent is 0
function solution(numbers) {
    const binaries = numbers.map((number) => number.toString(2));
    const fullBinaries = binaries.map((binary) => {
        const len = Math.pow(2, Math.floor(Math.log2(binary.length)) + 1) - 1;
        return binary.padStart(len, '0');
    });
    
    const isValid = fullBinaries.map((fullBinary) => isSatisfied(fullBinary, 0, fullBinary.length - 1) ? 1 : 0);
    return isValid;
}

function isSatisfied(fullBinaries, start, end) {
    if (start === end) return true;
    const middle = (start + end) / 2;
    const subtreeMiddle1 = (start + (middle - 1)) / 2;
    const subtreeMiddle2 = ((middle + 1) + end) / 2;
    if (fullBinaries[middle] === '0' && fullBinaries[subtreeMiddle1] === '0' && fullBinaries[subtreeMiddle2] === '0') return isSatisfied(fullBinaries, start, middle - 1) && isSatisfied(fullBinaries, middle + 1, end);
    if (fullBinaries[middle] === '1') return isSatisfied(fullBinaries, start, middle - 1) && isSatisfied(fullBinaries, middle + 1, end);
    
    return false;
}