// sort A in an ascending order
// sort B in an ascending order
// if a[i] < b[j], i += 1 && j += 1 및 승점 획득
// if a[i] > b[i], j += 1
// if a[i] === b[i], j += 1
// exchange argument: 정답의 선택과 바꿔도 여전히 a[i] > b[i]가 성립한다.

function solution(A, B) {
    A.sort((a, b) => a - b);
    B.sort((a, b) => a - b);
    let [ i, j ] = [ 0, 0 ];
    let score = 0;
    while (j < B.length) {
        if (A[i] >= B[j]) {
            j += 1;
            continue;
        }
        if (A[i] < B[j]) {
            i += 1;
            j += 1;
            score += 1;
            continue;
        }
    }
    
    return score;
}

