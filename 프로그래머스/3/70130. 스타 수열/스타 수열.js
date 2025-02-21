// 교집합이되는 수 b_1, b_2, ..., b_k에 대하여
// i = 0...n에 대하여
// (1) a[i] === a[i + 1] => 어떠한 후보군에도 포함될 수 없는 쌍이므로 건너뜀
// (2) a[i] !== a[i + 1] => a[i] = b_o, a[i + 1] = b_p이므로 b_o를 교집합으로 가지는 배열, b_p를 교집합으로 가지는 배열의 길이를 각각 2씩 증가시킨다.
// P(n): 알고리즘은 len(X) = n일 때, X의 어떤 원소 x_i를 교집합으로 가지는 스타수열의 최대 길이를 찾는다.
// i = 0 => P(0) = 0
// induction step: P(k)이 성립한다고 가정하자.
// lastIndex(p_k): 알고리즘에 사용되었던 x_k와 다른 마지막 원소의 인덱스
// lastIndex(p_k) <= lastIndex(o_k) => 항상 알고리즘이 더 찾음
// time complexity: O(n)
// space complexity: O(n)


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