function solution(arr) {
    return divideAndConquer(arr, 0, 0, arr.length);
}

function divideAndConquer(arr, i, j, size) {
    if (size === 1) {
        if (arr[i][j]) {
            return [ 0, 1 ];
        }
        return [ 1, 0 ];
    }

    const topLeft = divideAndConquer(arr, i, j, size / 2);
    const topRight = divideAndConquer(arr, i, j + size / 2, size / 2);
    const bottomLeft = divideAndConquer(arr, i + size / 2, j, size / 2);
    const bottomRight = divideAndConquer(arr, i + size / 2, j + size / 2, size / 2);
    
    const squares = [ topLeft, topRight, bottomLeft, bottomRight ];
    
    const isAllZero = squares.every((square) => square[1] === 0);
    const isAllOne = squares.every((square) => square[0] === 0);
    
    if (isAllZero) {
        return [ 1, 0 ];
    }
    if (isAllOne) {
        return [ 0, 1 ];
    }
    
    const totalSquare = squares.reduce((accumulator, square) => {
        accumulator[0] += square[0];
        accumulator[1] += square[1];
        return accumulator;
    }, [ 0, 0 ]);
    
    return totalSquare;
}