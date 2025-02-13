
const calculatePrefixMaxArray = (array) => array.reduce((accumulator, element, index, array) => {
        if (index === 0) {
            accumulator.push(array[index]);
            return accumulator;;
        }
        const lastElement = accumulator[index - 1];
        accumulator.push(Math.min(lastElement, element));
        return accumulator;
    }, []);

function solution(a) {
    const smallestNumbers = calculatePrefixMaxArray(a);
    const reversedSmallestNumbers = calculatePrefixMaxArray([ ...a ].reverse()).reverse();
    
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