// 탐색
// 유저의 현재 피로도, 현재 상태가 방문한 던전을 비트마스킹으로 나타냄
// 132와 312의 피로도 소모는 같기는 함, 근데 가능 여부가 달라짐
// 현재 선택한 subtree의 방문이 모두 끝났을 때, 체력을 회복시켜줄 수 있어야 함 => 회복 안 시켜주고 그냥 이전 상태 복원
// 따라서 필요한 상태는 [ 현재 피로도, 현재 상태가 방문한 던전, 방문 여부 ]
// 방문 가능한 상태: 8!

function dfs(maxHp, dungeons) {
    const root = {
        hp: maxHp,
        bitmask: 0,
        dungeonCount: 0,
    };
    const stack = [];
    stack.push(root);
    
    let maxDungeonCount = 0;
    while (stack.length) {
        const { hp, bitmask, dungeonCount } = stack.pop();
            
        let bitmaskString = bitmask.toString(2);
        
        maxDungeonCount = Math.max(maxDungeonCount, dungeonCount);

        for (let i = 0; i < dungeons.length; i++) {
            if ((bitmask & (1 << i)) !== 0) continue;
            const [ requiredHp, spentHp ] = dungeons[i];
            if (hp < requiredHp || hp < spentHp) continue;
            stack.push({ hp: hp - spentHp, bitmask: bitmask | (1 << i), dungeonCount: dungeonCount + 1 });
        }  
        
    }
    return maxDungeonCount;
}

function solution(k, dungeons) {
    return dfs(k, dungeons);
}