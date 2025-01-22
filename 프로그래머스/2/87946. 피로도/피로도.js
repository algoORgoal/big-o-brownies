const setDifference = (set1, set2) => new Set([ ...set1 ].filter((element) => !set2.has(element)));

function solution(k, dungeons) { 
    const visitedDungeonIndexSumSet = new Set();
    visitedDungeonIndexSumSet.add(0);
    
    const allDungeonIndexSet = new Set(Array.from({ length: dungeons.length }, (_, index) => index));
    
    
    const root = {
        dungeonIndexSet: new Set(),
        stamina: k,
    };
    
    const stack = [ root ];
    
    let max = -Infinity;
    
    while (stack.length) {
        const { dungeonIndexSet, stamina } = stack.pop();
        max = Math.max(max, dungeonIndexSet.size);
        
        const unvisitedDungeonIndexSet = setDifference(allDungeonIndexSet, dungeonIndexSet);
        
        if (unvisitedDungeonIndexSet.size === 0) {
            return allDungeonIndexSet.size;
        }
        
        const visitedIndexSum = [ ...dungeonIndexSet, ].reduce((accumulator, dungeonIndex) => accumulator + Math.pow(2, dungeonIndex), 0);
        
        [ ...unvisitedDungeonIndexSet ].forEach((unvisitedDungeonIndex) => {
            const newVisitedDungeonIndexSum = visitedIndexSum + Math.pow(2, unvisitedDungeonIndex);
            const [ requiredStamina, comsumingStamina ] = dungeons[unvisitedDungeonIndex];
            if (stamina >= requiredStamina && !visitedDungeonIndexSumSet.has(newVisitedDungeonIndexSum)) {
                visitedDungeonIndexSumSet.add(newVisitedDungeonIndexSum);
                stack.push({
                    dungeonIndexSet: new Set(dungeonIndexSet).add(unvisitedDungeonIndex),
                    stamina: stamina - comsumingStamina,
                });
            }
        });
    }
    return max;

}