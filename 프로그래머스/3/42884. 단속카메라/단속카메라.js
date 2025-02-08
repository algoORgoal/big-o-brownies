function solution(routes) {
    const sortedRoutes = routes.sort(([ start1, end1 ], [ start2, end2 ]) => end1 - end2);
    const { pointCount } = sortedRoutes.reduce((accumulator, [ start, end ], index) => {
        if (index === 0) {
            accumulator.max = end;
            accumulator.pointCount += 1;
            return accumulator;
        }
        if (start <= accumulator.max) {
            return accumulator;
        }
        accumulator.max = end;
        accumulator.pointCount += 1;
        return accumulator;
    }, {
        max: -Infinity,
        pointCount: 0,
    });
    
    return pointCount;
}