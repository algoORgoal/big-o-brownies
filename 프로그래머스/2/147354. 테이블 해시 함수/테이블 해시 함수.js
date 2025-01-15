function solution(data, col, rowBegin, rowEnd) {
    const sortedData = data.sort((row1, row2) => {
        if (row1[col - 1] === row2[col - 1]) {
            return row2[0] - row1[0];
        }
        return row1[col - 1] - row2[col - 1];
    });
    console.log(sortedData);
    const s = sortedData.slice(rowBegin - 1, rowEnd).map((row, index) => {
        return row.reduce((accumulator, element) => accumulator + (element % (rowBegin + index)) , 0);
    });
    
    const result = s.reduce((accumulator, element) => accumulator ^ element);
    
    return result;
}