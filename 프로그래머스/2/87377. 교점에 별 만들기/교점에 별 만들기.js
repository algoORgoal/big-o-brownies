function solution(line) {
    const intersections = new Set();
    for (let i = 0; i < line.length; i++) {
        for (let j = i + 1; j < line.length; j++) {
            const [ a, b, e ] = line[i];
            const [ c, d, f ] = line[j];
            
            if (a * d - b * c === 0) {
                continue;
            }
            if (((b * f - e * d) !== 0 || (e * c - a * f) !== 0) && ((b * f - e * d) % (a * d - b * c)) || ((e * c - a * f) % (a * d - b * c))) {
                continue;
            }
            
            [ x, y ] = [ (b * f - e * d) / (a * d - b * c), (e * c - a * f) / (a * d - b * c)];
            intersections.add(JSON.stringify([ x, y ]));
        }
    }
    
    const intersectionList = [ ...intersections ].map((intersectionJSON) => JSON.parse(intersectionJSON));
    console.log(intersectionList);
    
    const { minX, maxX, minY, maxY } = intersectionList.reduce((accumulator, [ x, y ]) => {
        if (accumulator.minX > x) {
            accumulator.minX = x;
        }
        if (accumulator.maxX < x) {
            accumulator.maxX = x;
        }
        if (accumulator.minY > y) {
            accumulator.minY = y;
        }
        if (accumulator.maxY < y) {
            accumulator.maxY = y;
        }
        return accumulator;
    }, {
        minX: Infinity,
        maxX: -Infinity,
        minY: Infinity,
        maxY: -Infinity
    });
    
    
    const minimalSquare = Array.from({ length: maxY - minY + 1, }, (_, i) => Array.from({ length: maxX - minX + 1, }, (_, j) => {

        if (intersections.has(JSON.stringify([ minX + j, maxY - i ]))) {
            return '*';
        }
        return '.';
    }).join(''));
    
    return minimalSquare;
    
    
}