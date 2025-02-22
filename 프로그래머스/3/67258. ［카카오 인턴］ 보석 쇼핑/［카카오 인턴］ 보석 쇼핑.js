// find all the types gems
// find the first minimum sequence of gems starting from i to j(i === 0)
// increament i by 1. if there is not enough types of gems increase j
// run until j === gems.length - 1

function solution(gems) {
    const gemTypes = gems.reduce((accumulator, element) => {
        accumulator.add(element);
        return accumulator;
    }, new Set());
    
    let [ i, j ] = [ 0, 0 ];
    const selectedGems = new Map();
    selectedGems.set(gems[0], 1);

    while (selectedGems.size < gemTypes.size) {
        j += 1;
        if (selectedGems.get(gems[j])) {
            selectedGems.set(gems[j], selectedGems.get(gems[j]) + 1);
            continue;
        }
        selectedGems.set(gems[j], 1);
    }
    
    const arrangements = [];
    arrangements.push([ i, j ]);
    
    for (let i = 1; i < gems.length && i <= j; i++) {
        selectedGems.set(gems[i - 1], selectedGems.get(gems[i - 1]) - 1);
        if (selectedGems.get(gems[i - 1]) === 0) selectedGems.delete(gems[i - 1]);
        while (selectedGems.size < gemTypes.size && j < gems.length - 1) {
            j += 1;
            if (selectedGems.get(gems[j])) {
                selectedGems.set(gems[j], selectedGems.get(gems[j]) + 1);
            } else {
                selectedGems.set(gems[j], 1);    
            }
        }
        
        if (selectedGems.size === gemTypes.size) arrangements.push([ i, j ]);
    }
    const adjustedArrangements = arrangements.map(([ start, end ]) => [ start + 1, end + 1 ]).sort(([ start1, end1 ], [ start2, end2 ]) => ((end1 - start1) - (end2 - start2)) || (start1 - start2));
    return adjustedArrangements[0];
}