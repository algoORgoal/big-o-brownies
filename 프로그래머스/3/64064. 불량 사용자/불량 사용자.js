// Create a lookup table whose keys are bannedId and values are userIds
// Run dfs with bitmask to see if each node has been visited or not
// When all bits are masked, increase count

// Create a lookup table whose keys are bannedId and values are userIds
// Run dfs with bitmask to see if each node has been visited or not
// When all bits are masked, increase count

function generateIdTable(userIds, bannedIds) {
    return bannedIds.reduce((accumulator, bannedId, bannedIdIndex) => {
        const word = bannedId.split(/([*]+)/).map((token) => token[0] === '*' ? `.{${token.length}}` : token).join("");
        const regex = new RegExp(`^${word}$`);
        
        const matchedUserIds = userIds.reduce((accumulator, userId, userIdIndex) => regex.test(userId) ? accumulator.concat(userIdIndex) : accumulator, []);
        accumulator[bannedIdIndex] = matchedUserIds;
        return accumulator;
    }, {});
}

function solution(userIds, bannedIds) {
    const idTable = generateIdTable(userIds, bannedIds);
    
    const root = bannedIds[0];
    const stack = [{ 
        nodeIndex: 0, 
        visited: 0,
    }];
    
    let count = 0;
    const visitedSet = new Set();
    
    while (stack.length) {
        const { nodeIndex, visited } = stack.pop();
        
        if (nodeIndex === bannedIds.length) {
            count += 1;
            continue;
        }
        
        const matchedUserIdIndices = idTable[nodeIndex].filter((userIdIndex) => !(visited.has & (1 << userIdIndex)));
        matchedUserIdIndices.forEach((userIdIndex) => {
            if (!visitedSet.has(visited | (1 << userIdIndex))) {
                stack.push({
                nodeIndex: nodeIndex + 1,
                visited: visited | (1 << userIdIndex),
                });
                visitedSet.add(visited | (1 << userIdIndex));
            }
        });
    }
    
    return count;
}

function solution(userIds, bannedIds) {
    const idTable = generateIdTable(userIds, bannedIds);
    
    const root = bannedIds[0];
    const stack = [{ 
        nodeIndex: 0, 
        combination: 0,
    }];
    
    let count = 0;
    const visitedSet = new Set();
    
    while (stack.length) {
        const { nodeIndex, combination } = stack.pop();
        
        if (nodeIndex === bannedIds.length) {
            count += 1;
            continue;
        }
        
        const userIdIndices = idTable[nodeIndex]
        userIdIndices.forEach((userIdIndex) => {
            if (!visitedSet.has(combination | (1 << userIdIndex))) {
                stack.push({
                nodeIndex: nodeIndex + 1,
                combination: combination | (1 << userIdIndex),
                });
                visitedSet.add(combination | (1 << userIdIndex));
            }
        });
    }
    
    return count;
}

