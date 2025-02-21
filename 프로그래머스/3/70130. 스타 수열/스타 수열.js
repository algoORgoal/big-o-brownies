function solution(a) {
    const table = a.reduce((accumulator, element, index) => {
        if (accumulator[element] === undefined) {
            accumulator[element] = 0;
            return accumulator;
        }
        const previousElement = accumulator[index - 1];
        if (element === previousElement) return accumulator;
        accumulator[element] += 1;
        return accumulator;
    }, {});
    console.log(table);
    return Math.min(...Object.values(table))
}