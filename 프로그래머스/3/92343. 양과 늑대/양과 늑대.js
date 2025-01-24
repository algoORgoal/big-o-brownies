function solution(info, edges) {
    const graph = Array.from({ length: info.length, }, () => Array.from({ length: info.length }, () => 0));
    edges.forEach(([ source, destination ]) => {
        graph[source][destination] = 1;
    });
    
    
    const root = {
        visitBitMap: 1,
        shipCount: 1,
        wolfCount: 0,
    };
    
    
    const stack = [ root ];

    let maxShipCount = 0;
    
    while (stack.length) {
        const node = stack.pop();
        const { visitBitMap, shipCount, wolfCount } = node;
        maxShipCount = Math.max(maxShipCount, shipCount);
        
        for (let i = 0; i < info.length; i++) {
            if (visitBitMap & (1 << i)) {
                continue;
            }
            if ((info[i] === 1) && (shipCount <= wolfCount + 1)) {
                continue;
            }
            
            const isAdjacent = visitBitMap.toString(2).split('').map(Number).reverse().some((isVisited, index) => isVisited && graph[index][i]);
            
            if (!isAdjacent) {
                continue;
            }
            
            const newVisitBitMap = visitBitMap | (1 << i);
            stack.push({ 
                visitBitMap: newVisitBitMap,
                shipCount: info[i] === 0 ? shipCount + 1 : shipCount,
                wolfCount: info[i] === 1 ? wolfCount + 1 : wolfCount,
            });   
        }
    }
    
    return maxShipCount;
}