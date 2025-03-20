// 블럭 개수의 총합 => 면적
// 가능한 가로 세로 길이를 확인해보면서,
// brown === 테두리 개수, yellow === 안에 있는 거 개수면 리턴
// 테두리 개수 = (column * 2) + (row - 2) * 2

function solution(brown, yellow) {
    const total = brown + yellow;
    for (let i = 1; i < total; i++) {
        if (total % i !== 0) continue;
        const [ row, column ] = [ i, total / i];
        const border = (column * 2) + (row - 2) * 2;
        if (border === brown) {
            return [ column, row ];
        }
    }
}