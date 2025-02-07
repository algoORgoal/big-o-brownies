function solution(n, computers) {
    return dfs(n, computers);
}

function dfs(n, computers) {
    const visited = new Set();
    
    let componentCount = 0;
    for (let i = 0; i < computers.length; i++) {
        const root = i;
        if (visited.has(root)) continue;
        
        const stack = [ root ];
        while (stack.length) {
            const node = stack.pop();
            
            const nextNodes = computers[node].reduce((accumulator, isConnected, nextNode) => {
                if (!isConnected) return accumulator;
                if (visited.has(nextNode)) return accumulator;
                visited.add(nextNode);
                accumulator.push(nextNode);
                return accumulator;
            }, []);
            
            nextNodes.forEach((nextNode) => stack.push(nextNode));                                                                     
        }
        componentCount += 1;
    }
    
    return componentCount;
}