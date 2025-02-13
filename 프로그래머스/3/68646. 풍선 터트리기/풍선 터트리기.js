function solution(a) {
    const smallestNumbers = a.reduce((accumulator, element, index, array) => {
        if (index === 0) {
            accumulator.push(array[index]);
            return accumulator;;
        }
        const lastElement = accumulator[index - 1];
        accumulator.push(Math.min(lastElement, element));
        return accumulator;
    }, []);
    
    const reversedSmallestNumbers = [ ...a ].reverse().reduce((accumulator, element, index, array) => {
        if (index === 0) {
            accumulator.push(array[index]);
            return accumulator;;
        }
        const lastElement = accumulator[index - 1];
        accumulator.push(Math.min(lastElement, element));
        return accumulator;
    }, []).reverse();
    
    const survivedElements = a.filter((element, index, array) => {
        if (index === 0) return true;
        if (index === array.length - 1) return true;
        if (element > smallestNumbers[index - 1] && element > reversedSmallestNumbers[index + 1]) return false;
        return true;
    });
    
    return survivedElements.length;
}

// 양 끝 요소들은 무조건 마지막까지 남아있을 수 있다.
// 가장 값이 작은 요소는 마지막까지 남아있을 수 있다.
// 양 끝 옆 요소들은 해당 요소 기준으로
// 왼쪽에서 가장 작은 값 > 현재 요소 > 오른쪽에서 가장 작은 값 또는
// 왼쪽에서 가장 작은 값 < 현재 요소 < 오른쪽에서 가장 작은 값이면 고를 수 있다.
// 왼쪽에서 가장 작은 값 > 현재 요소 < 오른쪽에서 가장 작은 값이면 고를 수 있다.
// 왼쪽에서 가장 작은 값 < 현재 요소 > 오른쪽에서 가장 작은 값이면 못고른다.
// -16 27 65 -2 58 -92 -71 -68 -61 -33
// -5 -1 9
// -5와 -1비교할 때 -5 제거 => -1
// 

// 10 4 8 6
// 10 제거
// 4 제거
// 8 제거
// => 6
// 4 6 8 10

// [0, 1] [1, 2], ... [n, n + 1]
// 3개의 원소
// -16 27
// -16, 27

// -16, 27, 65


// 9 -1 -5
// => -1(-1, -5)
// => -5(9, -5)

// => 9(9, -1)
// => -5(-1, -5)

// => 9(9, -1)
// => -1(-1, -5)