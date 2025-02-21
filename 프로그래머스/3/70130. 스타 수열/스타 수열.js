// 교집합이되는 수 b_1, b_2, ..., b_k에 대하여
// i = 0...n에 대하여
// (1) a[i] === a[i + 1] => 어떠한 후보군에도 포함될 수 없는 쌍이므로 건너뜀
// (2) a[i] !== a[i + 1] => a[i] = b_o, a[i + 1] = b_p이므로 b_o를 교집합으로 가지는 배열, b_p를 교집합으로 가지는 배열의 길이를 각각 2씩 증가시킨다.


function solution(a) {
    const table = a.reduce((accumulator, element) => {
        if (element in accumulator) return accumulator;
        accumulator[element] = [ 0, -1 ];
        return accumulator;
    }, {});
    
    if (a.length === 1) {
        return 0;
    }
    
    if (a.length === 2) {
        return a[0] !== a[1] ? 2 : 0;
    }
     

    
    for (let i = 0; i < a.length; i++) {
        if (i > 0 && table[a[i]][1] !== i - 1) {
            const pair = [ a[i - 1], a[i] ];
            if (pair[0] !== pair[1]) {
                table[a[i]] = [ table[a[i]][0] + 2 , i - 1 ];
                continue;
            }
        }
        if (i < a.length - 1 && table[a[i]][1] !== i + 1){
            const pair = [ a[i], a[i + 1], ];
            if (pair[0] !== pair[1]) {
                table[a[i]] = [  table[a[i]][0] + 2, i + 1 ];
            }
        } 
    }
    
    return a.reduce((accumulator, element) => {
        const [ count ] = table[element];
        return Math.max(accumulator, count);
    }, 0);
}